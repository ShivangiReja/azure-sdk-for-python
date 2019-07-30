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

from .dataset_py3 import Dataset


class AzureSqlDWTableDataset(Dataset):
    """The Azure SQL Data Warehouse dataset.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param schema: Columns that define the physical type schema of the
     dataset. Type: array (or Expression with resultType array), itemType:
     DatasetSchemaDataElement.
    :type schema: object
    :param linked_service_name: Required. Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param folder: The folder that this Dataset is in. If not specified,
     Dataset will appear at the root level.
    :type folder: ~azure.mgmt.datafactory.models.DatasetFolder
    :param type: Required. Constant filled by server.
    :type type: str
    :param table_name: This property will be retired. Please consider using
     schema + table properties instead.
    :type table_name: object
    :param azure_sql_dw_table_dataset_schema: The schema name of the Azure SQL
     Data Warehouse. Type: string (or Expression with resultType string).
    :type azure_sql_dw_table_dataset_schema: object
    :param table: The table name of the Azure SQL Data Warehouse. Type: string
     (or Expression with resultType string).
    :type table: object
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'schema': {'key': 'schema', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'folder': {'key': 'folder', 'type': 'DatasetFolder'},
        'type': {'key': 'type', 'type': 'str'},
        'table_name': {'key': 'typeProperties.tableName', 'type': 'object'},
        'azure_sql_dw_table_dataset_schema': {'key': 'typeProperties.schema', 'type': 'object'},
        'table': {'key': 'typeProperties.table', 'type': 'object'},
    }

    def __init__(self, *, linked_service_name, additional_properties=None, description: str=None, structure=None, schema=None, parameters=None, annotations=None, folder=None, table_name=None, azure_sql_dw_table_dataset_schema=None, table=None, **kwargs) -> None:
        super(AzureSqlDWTableDataset, self).__init__(additional_properties=additional_properties, description=description, structure=structure, schema=schema, linked_service_name=linked_service_name, parameters=parameters, annotations=annotations, folder=folder, **kwargs)
        self.table_name = table_name
        self.azure_sql_dw_table_dataset_schema = azure_sql_dw_table_dataset_schema
        self.table = table
        self.type = 'AzureSqlDWTable'
