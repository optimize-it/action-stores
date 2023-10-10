import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.storageaccount_models import *
from typing import Union

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_azure_storage_account(params: StorageAccountCreationParameters) -> Union[StorageAccountResponseModel, dict]:
    subscriptionId = get_subscription_id_secret()
    resourceGroupName = params.resourceGroupName
    storageAccountName = params.storageAccountName
    storage_data =  {
                        "sku": {
                            "name": params.sku
                        },
                        "kind": params.kind,
                        "location": params.location,
                        # "extendedLocation": {
                        #     "type": "EdgeZone",
                        #     "name": "losangeles001"
                        # },
                        "properties": {
                            "keyPolicy": {
                            "keyExpirationPeriodInDays": 20
                            },
                            "sasPolicy": {
                            "sasExpirationPeriod": "1.15:59:59",
                            "expirationAction": "Log"
                            },
                            # "isHnsEnabled": True,
                            # "isSftpEnabled": True,
                            "allowBlobPublicAccess": False,
                            "defaultToOAuthAuthentication": False,
                            "minimumTlsVersion": "TLS1_2",
                            "allowSharedKeyAccess": True,
                            # "routingPreference": {
                            # "routingChoice": "MicrosoftRouting",
                            # "publishMicrosoftEndpoints": True,
                            # "publishInternetEndpoints": True
                            # },
                            "encryption": {
                            "services": {
                                "file": {
                                "keyType": "Account",
                                "enabled": True
                                },
                                "blob": {
                                "keyType": "Account",
                                "enabled": True
                                }
                            },
                            "requireInfrastructureEncryption": False,
                            "keySource": "Microsoft.Storage"
                            }
                        }
                        }
    endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{storageAccountName}"
    api_version = "2023-01-01"

    response_data = put_wrapper(endpoint, api_version, data=storage_data)

    return response_data

@action_store.kubiya_action()
def list_storage_skus(params: StorageSkuParametes):
    # subscriptionId = params.subscriptionId
    endpoint = f"/providers/Microsoft.Storage/skus"
    api_version = "2023-01-01"

    response_data = get_wrapper(endpoint, api_version)

    return response_data

@action_store.kubiya_action()
def list_all_storage_accounts(params: ListStorageParametes) -> List[ListStorageResponseModel]:
    endpoint = "/providers/Microsoft.Storage/storageAccounts"
    api_version = "2023-01-01"
    response_data = get_wrapper(endpoint, api_version)
    storage_list = response_data.get('value', [])
    return [ListStorageResponseModel(**storageaccount) for storageaccount in storage_list]



@action_store.kubiya_action()
def delete_storage_account(params: DeleteStorageAccount):
    endpoint = f"/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{params.storageaccountName}"
    api_version = "2023-01-01"
    response_data = delete_wrapper(endpoint, api_version)
    return response_data

@action_store.kubiya_action()
def get_storage_account(params: GetStorageAccount):
    endpoint = f"/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{params.storageaccountName}"
    api_version = "2023-01-01"
    response_data = get_wrapper(endpoint, api_version)
    return response_data