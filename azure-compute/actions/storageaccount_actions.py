import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.storageaccount_models import *
from typing import Union

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_azure_storage_account(params: StorageAccountCreationParameters) -> Union[StorageAccountResponseModel, dict]:
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    storageAccountName = params.vnetName
    storage_data = {
                "kind": params.kind,
                "location": params.location,
                "sku": params.sku
}
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{storageAccountName}"
    api_version = "2023-03-01"

    response_data = put_wrapper(endpoint, subscriptionId, api_version, data=storage_data)

    return StorageAccountResponseModel(**response_data)

@action_store.kubiya_action()
def list_storage_skus(params: StorageSkuParametes):
    subscriptionId = params.subscriptionId
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{params.storageAccountName}"
    api_version = "2023-03-01"

    response_data = get_wrapper(endpoint, subscriptionId, api_version)

    return response_data