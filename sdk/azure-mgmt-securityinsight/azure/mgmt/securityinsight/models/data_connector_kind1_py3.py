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


class DataConnectorKind1(Model):
    """Describes an Azure resource with kind.

    :param kind: The kind of the data connector. Possible values include:
     'AzureActiveDirectory', 'AzureSecurityCenter',
     'MicrosoftCloudAppSecurity', 'ThreatIntelligence', 'Office365',
     'AmazonWebServicesCloudTrail'
    :type kind: str or ~azure.mgmt.securityinsight.models.DataConnectorKind
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, *, kind=None, **kwargs) -> None:
        super(DataConnectorKind1, self).__init__(**kwargs)
        self.kind = kind
