import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.virtualnetwork_models import *
from typing import Union

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_or_update_virtual_network(params: VNETCreationParameters) -> Union[VirtualNetworkResponseModel, dict]:
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vnetName = params.vnetName
    vnet_data = {
                "properties": {
                    "addressSpace": {
                    "addressPrefixes": params.cidr
                    },
                "subnets": [
                {
                    "name": params.subnet_name,
                    "properties": {
                    "addressPrefix": params.subnet_cidr
                    }
                }
                ]
                },
                "location": params.location
}
    endpoint = f"subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}"
    api_version = "2023-03-01"

    response_data = put_wrapper(endpoint, subscriptionId, api_version, data=vnet_data)

    return VirtualNetworkResponseModel(**response_data)

@action_store.kubiya_action()
def get_virtual_network(params: VNETCreationParameters) -> Union[VirtualNetworkResponseModel, dict]:
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vnetName = params.vnetName
    api_version = "2022-02-01"
    endpoint = f"subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}"
    response_data = get_wrapper(endpoint, subscriptionId, api_version)
    return VirtualNetworkResponseModel(**response_data)

@action_store.kubiya_action()
def listall_azure_Vnets(params: VnetListParameters) -> List[VnetListModel]:
    #subscriptionId = params.subscriptionId
    endpoint = f"subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/virtualNetworks"
    api_version = "2022-02-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    Vnet_list = response_data.get('value', [])
    return [VnetListModel(**Vnet) for Vnet in Vnet_list]

@action_store.kubiya_action()
def list_by_rg_azure_Vnets(params: VnetListParameters) -> List[VnetListModel]:
    #subscriptionId = params.subscriptionId
    endpoint = f"subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/virtualNetworks"
    api_version = "2022-02-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    Vnet_list = response_data.get('value', [])
    return [VnetListModel(**Vnet) for Vnet in Vnet_list]

@action_store.kubiya_action()
def delete_azure_virtual_network(params: VnetDeleteParameters):
    #subscriptionId = params.subscriptionId
    endpoint = f"subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/virtualNetworks/{params.vnetName}"
    api_version = "2022-02-01"
    response_data = delete_wrapper(endpoint, params.subscriptionId, api_version)
    if response_data:
        return response_data
    else:
        None

@action_store.kubiya_action()
def update_tags_azure_virtual_network(params: VnetTagsUpdateParameters) -> List[VnetTagsUpdateResponse]:
    #subscriptionId = params.subscriptionId
    endpoint = f"subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/virtualNetworks/{params.vnetName}"
    api_version = "2022-02-01"
    response_data = patch_wrapper(endpoint, params.subscriptionId, api_version)
    if response_data:
        return VnetTagsUpdateResponse(**response_data)
    else:
        None

