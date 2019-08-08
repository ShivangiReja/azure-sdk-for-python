# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DatabaseUpdate(Model):
    """A database resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param sku: The name and tier of the SKU.
    :type sku: ~azure.mgmt.sql.models.Sku
    :param create_mode: Specifies the mode of database creation.
     Default: regular database creation.
     Copy: creates a database as a copy of an existing database.
     sourceDatabaseId must be specified as the resource ID of the source
     database.
     Secondary: creates a database as a secondary replica of an existing
     database. sourceDatabaseId must be specified as the resource ID of the
     existing primary database.
     PointInTimeRestore: Creates a database by restoring a point in time backup
     of an existing database. sourceDatabaseId must be specified as the
     resource ID of the existing database, and restorePointInTime must be
     specified.
     Recovery: Creates a database by restoring a geo-replicated backup.
     sourceDatabaseId must be specified as the recoverable database resource ID
     to restore.
     Restore: Creates a database by restoring a backup of a deleted database.
     sourceDatabaseId must be specified. If sourceDatabaseId is the database's
     original resource ID, then sourceDatabaseDeletionDate must be specified.
     Otherwise sourceDatabaseId must be the restorable dropped database
     resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime
     may also be specified to restore from an earlier point in time.
     RestoreLongTermRetentionBackup: Creates a database by restoring from a
     long term retention vault. recoveryServicesRecoveryPointResourceId must be
     specified as the recovery point resource ID.
     Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for
     DataWarehouse edition. Possible values include: 'Default', 'Copy',
     'Secondary', 'PointInTimeRestore', 'Restore', 'Recovery',
     'RestoreExternalBackup', 'RestoreExternalBackupSecondary',
     'RestoreLongTermRetentionBackup', 'OnlineSecondary'
    :type create_mode: str or ~azure.mgmt.sql.models.CreateMode
    :param collation: The collation of the database.
    :type collation: str
    :param max_size_bytes: The max size of the database expressed in bytes.
    :type max_size_bytes: long
    :param sample_name: The name of the sample schema to apply when creating
     this database. Possible values include: 'AdventureWorksLT',
     'WideWorldImportersStd', 'WideWorldImportersFull'
    :type sample_name: str or ~azure.mgmt.sql.models.SampleName
    :param elastic_pool_id: The resource identifier of the elastic pool
     containing this database.
    :type elastic_pool_id: str
    :param source_database_id: The resource identifier of the source database
     associated with create operation of this database.
    :type source_database_id: str
    :ivar status: The status of the database. Possible values include:
     'Online', 'Restoring', 'RecoveryPending', 'Recovering', 'Suspect',
     'Offline', 'Standby', 'Shutdown', 'EmergencyMode', 'AutoClosed',
     'Copying', 'Creating', 'Inaccessible', 'OfflineSecondary', 'Pausing',
     'Paused', 'Resuming', 'Scaling', 'OfflineChangingDwPerformanceTiers',
     'OnlineChangingDwPerformanceTiers'
    :vartype status: str or ~azure.mgmt.sql.models.DatabaseStatus
    :ivar database_id: The ID of the database.
    :vartype database_id: str
    :ivar creation_date: The creation date of the database (ISO8601 format).
    :vartype creation_date: datetime
    :ivar current_service_objective_name: The current service level objective
     name of the database.
    :vartype current_service_objective_name: str
    :ivar requested_service_objective_name: The requested service level
     objective name of the database.
    :vartype requested_service_objective_name: str
    :ivar default_secondary_location: The default secondary region for this
     database.
    :vartype default_secondary_location: str
    :ivar failover_group_id: Failover Group resource identifier that this
     database belongs to.
    :vartype failover_group_id: str
    :param restore_point_in_time: Specifies the point in time (ISO8601 format)
     of the source database that will be restored to create the new database.
    :type restore_point_in_time: datetime
    :param source_database_deletion_date: Specifies the time that the database
     was deleted.
    :type source_database_deletion_date: datetime
    :param recovery_services_recovery_point_id: The resource identifier of the
     recovery point associated with create operation of this database.
    :type recovery_services_recovery_point_id: str
    :param long_term_retention_backup_resource_id: The resource identifier of
     the long term retention backup associated with create operation of this
     database.
    :type long_term_retention_backup_resource_id: str
    :param recoverable_database_id: The resource identifier of the recoverable
     database associated with create operation of this database.
    :type recoverable_database_id: str
    :param restorable_dropped_database_id: The resource identifier of the
     restorable dropped database associated with create operation of this
     database.
    :type restorable_dropped_database_id: str
    :param catalog_collation: Collation of the metadata catalog. Possible
     values include: 'DATABASE_DEFAULT', 'SQL_Latin1_General_CP1_CI_AS'
    :type catalog_collation: str or
     ~azure.mgmt.sql.models.CatalogCollationType
    :param zone_redundant: Whether or not this database is zone redundant,
     which means the replicas of this database will be spread across multiple
     availability zones.
    :type zone_redundant: bool
    :param license_type: The license type to apply for this database. Possible
     values include: 'LicenseIncluded', 'BasePrice'
    :type license_type: str or ~azure.mgmt.sql.models.DatabaseLicenseType
    :ivar max_log_size_bytes: The max log size for this database.
    :vartype max_log_size_bytes: long
    :ivar earliest_restore_date: This records the earliest start date and time
     that restore is available for this database (ISO8601 format).
    :vartype earliest_restore_date: datetime
    :param read_scale: The state of read-only routing. If enabled, connections
     that have application intent set to readonly in their connection string
     may be routed to a readonly secondary replica in the same region. Possible
     values include: 'Enabled', 'Disabled'
    :type read_scale: str or ~azure.mgmt.sql.models.DatabaseReadScale
    :param read_replica_count: The number of readonly secondary replicas
     associated with the database.
    :type read_replica_count: int
    :ivar current_sku: The name and tier of the SKU.
    :vartype current_sku: ~azure.mgmt.sql.models.Sku
    :param auto_pause_delay: Time in minutes after which database is
     automatically paused. A value of -1 means that automatic pause is disabled
    :type auto_pause_delay: int
    :param min_capacity: Minimal capacity that database will always have
     allocated, if not paused
    :type min_capacity: float
    :ivar paused_date: The date when database was paused by user configuration
     or action (ISO8601 format). Null if the database is ready.
    :vartype paused_date: datetime
    :ivar resumed_date: The date when database was resumed by user action or
     database login (ISO8601 format). Null if the database is paused.
    :vartype resumed_date: datetime
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'status': {'readonly': True},
        'database_id': {'readonly': True},
        'creation_date': {'readonly': True},
        'current_service_objective_name': {'readonly': True},
        'requested_service_objective_name': {'readonly': True},
        'default_secondary_location': {'readonly': True},
        'failover_group_id': {'readonly': True},
        'max_log_size_bytes': {'readonly': True},
        'earliest_restore_date': {'readonly': True},
        'current_sku': {'readonly': True},
        'paused_date': {'readonly': True},
        'resumed_date': {'readonly': True},
    }

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'create_mode': {'key': 'properties.createMode', 'type': 'str'},
        'collation': {'key': 'properties.collation', 'type': 'str'},
        'max_size_bytes': {'key': 'properties.maxSizeBytes', 'type': 'long'},
        'sample_name': {'key': 'properties.sampleName', 'type': 'str'},
        'elastic_pool_id': {'key': 'properties.elasticPoolId', 'type': 'str'},
        'source_database_id': {'key': 'properties.sourceDatabaseId', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'database_id': {'key': 'properties.databaseId', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'current_service_objective_name': {'key': 'properties.currentServiceObjectiveName', 'type': 'str'},
        'requested_service_objective_name': {'key': 'properties.requestedServiceObjectiveName', 'type': 'str'},
        'default_secondary_location': {'key': 'properties.defaultSecondaryLocation', 'type': 'str'},
        'failover_group_id': {'key': 'properties.failoverGroupId', 'type': 'str'},
        'restore_point_in_time': {'key': 'properties.restorePointInTime', 'type': 'iso-8601'},
        'source_database_deletion_date': {'key': 'properties.sourceDatabaseDeletionDate', 'type': 'iso-8601'},
        'recovery_services_recovery_point_id': {'key': 'properties.recoveryServicesRecoveryPointId', 'type': 'str'},
        'long_term_retention_backup_resource_id': {'key': 'properties.longTermRetentionBackupResourceId', 'type': 'str'},
        'recoverable_database_id': {'key': 'properties.recoverableDatabaseId', 'type': 'str'},
        'restorable_dropped_database_id': {'key': 'properties.restorableDroppedDatabaseId', 'type': 'str'},
        'catalog_collation': {'key': 'properties.catalogCollation', 'type': 'str'},
        'zone_redundant': {'key': 'properties.zoneRedundant', 'type': 'bool'},
        'license_type': {'key': 'properties.licenseType', 'type': 'str'},
        'max_log_size_bytes': {'key': 'properties.maxLogSizeBytes', 'type': 'long'},
        'earliest_restore_date': {'key': 'properties.earliestRestoreDate', 'type': 'iso-8601'},
        'read_scale': {'key': 'properties.readScale', 'type': 'str'},
        'read_replica_count': {'key': 'properties.readReplicaCount', 'type': 'int'},
        'current_sku': {'key': 'properties.currentSku', 'type': 'Sku'},
        'auto_pause_delay': {'key': 'properties.autoPauseDelay', 'type': 'int'},
        'min_capacity': {'key': 'properties.minCapacity', 'type': 'float'},
        'paused_date': {'key': 'properties.pausedDate', 'type': 'iso-8601'},
        'resumed_date': {'key': 'properties.resumedDate', 'type': 'iso-8601'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(DatabaseUpdate, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.create_mode = kwargs.get('create_mode', None)
        self.collation = kwargs.get('collation', None)
        self.max_size_bytes = kwargs.get('max_size_bytes', None)
        self.sample_name = kwargs.get('sample_name', None)
        self.elastic_pool_id = kwargs.get('elastic_pool_id', None)
        self.source_database_id = kwargs.get('source_database_id', None)
        self.status = None
        self.database_id = None
        self.creation_date = None
        self.current_service_objective_name = None
        self.requested_service_objective_name = None
        self.default_secondary_location = None
        self.failover_group_id = None
        self.restore_point_in_time = kwargs.get('restore_point_in_time', None)
        self.source_database_deletion_date = kwargs.get('source_database_deletion_date', None)
        self.recovery_services_recovery_point_id = kwargs.get('recovery_services_recovery_point_id', None)
        self.long_term_retention_backup_resource_id = kwargs.get('long_term_retention_backup_resource_id', None)
        self.recoverable_database_id = kwargs.get('recoverable_database_id', None)
        self.restorable_dropped_database_id = kwargs.get('restorable_dropped_database_id', None)
        self.catalog_collation = kwargs.get('catalog_collation', None)
        self.zone_redundant = kwargs.get('zone_redundant', None)
        self.license_type = kwargs.get('license_type', None)
        self.max_log_size_bytes = None
        self.earliest_restore_date = None
        self.read_scale = kwargs.get('read_scale', None)
        self.read_replica_count = kwargs.get('read_replica_count', None)
        self.current_sku = None
        self.auto_pause_delay = kwargs.get('auto_pause_delay', None)
        self.min_capacity = kwargs.get('min_capacity', None)
        self.paused_date = None
        self.resumed_date = None
        self.tags = kwargs.get('tags', None)
