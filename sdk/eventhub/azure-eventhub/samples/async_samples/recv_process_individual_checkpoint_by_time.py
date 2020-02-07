#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import asyncio
import os
import logging
import time
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore

CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]
STORAGE_CONNECTION_STR = os.environ["AZURE_STORAGE_CONN_STR"]
BLOB_CONTAINER_NAME = "your-blob-container-name"  # Please make sure the blob container resource exists.

logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s | %(asctime)s | %(name)-12s | %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M:%S',)
log = logging.getLogger(__name__)

task_semaphor = asyncio.Semaphore(100)  # For back pressure control. At most 100 concurrent upload_doc() are running.

async def upload_doc(doc):
    async with task_semaphor:  # blocking if there are already 100 upload_doc() are running
        await asyncio.sleep(0.1)  # http request to upload a doc

# checkpoint by time
async def on_event(partition_context, event):
    log.info(f"<check> batch process pid:{partition_context.partition_id} last sq {event.sequence_number}")
    task = asyncio.create_task(upload_doc(event.body_as_str()))
    if getattr(partition_context, "last_checkpoint_time", time.time()) + 10 >= time.time():  # every 10 seconds
        await partition_context.update_checkpoint()
        partition_context.last_checkpoint_time = time.time()

async def receive(client):
    await client.receive_batch(
        on_event=on_event,
        starting_position="-1",  # optional, "-1" is from the beginning of the partition.
    )

async def main():
    checkpoint_store = BlobCheckpointStore.from_connection_string(STORAGE_CONNECTION_STR, BLOB_CONTAINER_NAME)
    client = EventHubConsumerClient.from_connection_string(
        CONNECTION_STR,
        consumer_group="$Default",
        checkpoint_store=checkpoint_store,  # For load-balancing and checkpoint. Leave None for no load-balancing.
    )
    async with client:
        await receive(client)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
