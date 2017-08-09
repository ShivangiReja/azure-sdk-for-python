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


class AADObject(Model):
    """The properties of an Active Directory object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param object_id: The ID of the object.
    :type object_id: str
    :param object_type: The type of AAD object.
    :type object_type: str
    :param display_name: The display name of the object.
    :type display_name: str
    :param user_principal_name: The principal name of the object.
    :type user_principal_name: str
    :param mail: The primary email address of the object.
    :type mail: str
    :param mail_enabled: Whether the AAD object is mail-enabled.
    :type mail_enabled: bool
    :ivar mail_nickname: The mail alias for the user.
    :vartype mail_nickname: str
    :param security_enabled: Whether the AAD object is security-enabled.
    :type security_enabled: bool
    :param sign_in_name: The sign-in name of the object.
    :type sign_in_name: str
    :param service_principal_names: A collection of service principal names
     associated with the object.
    :type service_principal_names: list of str
    :param user_type: The user type of the object.
    :type user_type: str
    :ivar usage_location: A two letter country code (ISO standard 3166).
     Required for users that will be assigned licenses due to legal requirement
     to check for availability of services in countries. Examples include:
     "US", "JP", and "GB".
    :vartype usage_location: str
    :ivar app_id: The application ID.
    :vartype app_id: str
    :ivar app_permissions: The application permissions.
    :vartype app_permissions: list of str
    :ivar available_to_other_tenants: Whether the application is be available
     to other tenants.
    :vartype available_to_other_tenants: bool
    :ivar identifier_uris: A collection of URIs for the application.
    :vartype identifier_uris: list of str
    :ivar reply_urls: A collection of reply URLs for the application.
    :vartype reply_urls: list of str
    :ivar homepage: The home page of the application.
    :vartype homepage: str
    """

    _validation = {
        'mail_nickname': {'readonly': True},
        'usage_location': {'readonly': True},
        'app_id': {'readonly': True},
        'app_permissions': {'readonly': True},
        'available_to_other_tenants': {'readonly': True},
        'identifier_uris': {'readonly': True},
        'reply_urls': {'readonly': True},
        'homepage': {'readonly': True},
    }

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'mail': {'key': 'mail', 'type': 'str'},
        'mail_enabled': {'key': 'mailEnabled', 'type': 'bool'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
        'security_enabled': {'key': 'securityEnabled', 'type': 'bool'},
        'sign_in_name': {'key': 'signInName', 'type': 'str'},
        'service_principal_names': {'key': 'servicePrincipalNames', 'type': '[str]'},
        'user_type': {'key': 'userType', 'type': 'str'},
        'usage_location': {'key': 'usageLocation', 'type': 'str'},
        'app_id': {'key': 'appId', 'type': 'str'},
        'app_permissions': {'key': 'appPermissions', 'type': '[str]'},
        'available_to_other_tenants': {'key': 'availableToOtherTenants', 'type': 'bool'},
        'identifier_uris': {'key': 'identifierUris', 'type': '[str]'},
        'reply_urls': {'key': 'replyUrls', 'type': '[str]'},
        'homepage': {'key': 'homepage', 'type': 'str'},
    }

    def __init__(self, object_id=None, object_type=None, display_name=None, user_principal_name=None, mail=None, mail_enabled=None, security_enabled=None, sign_in_name=None, service_principal_names=None, user_type=None):
        self.object_id = object_id
        self.object_type = object_type
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.mail = mail
        self.mail_enabled = mail_enabled
        self.mail_nickname = None
        self.security_enabled = security_enabled
        self.sign_in_name = sign_in_name
        self.service_principal_names = service_principal_names
        self.user_type = user_type
        self.usage_location = None
        self.app_id = None
        self.app_permissions = None
        self.available_to_other_tenants = None
        self.identifier_uris = None
        self.reply_urls = None
        self.homepage = None
