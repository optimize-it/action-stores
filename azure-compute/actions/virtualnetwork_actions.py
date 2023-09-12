import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.virtualnetwork_models import *
from typing import Union
import json


logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_or_update_virtual_network(params: VNETCreationParameters) -> Union[VirtualNetworkResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vnetName = params.vnetName
        vnet_data = {
                    "properties": {
                        "addressSpace": {
                        "addressPrefixes": [ params.cidr ]
                        },
                    "subnets": [
                    {
                        "name": f"{params.vnetName}-default-subnet",
                        "properties": {
                        "addressPrefix": params.subnet_cidr
                        }
                    }
                    ]
                    },
                    "location": params.location
                }
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}"
        api_version = "2023-02-01"

        response_data = put_wrapper(endpoint, subscriptionId, api_version, data=vnet_data)
        if response_data['id'] != "null":
            logger.info("got the response")
            return VirtualNetworkResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to create virtual network : {e}")
        raise

        

@action_store.kubiya_action()
def get_virtual_network(params: VNETGetParameters) -> Union[VirtualNetworkResponseModel, dict]:
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vnetName = params.vnetName
    api_version = "2023-02-01"
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}"
    response_data = get_wrapper(endpoint, subscriptionId, api_version)
    return VirtualNetworkResponseModel(**response_data)

@action_store.kubiya_action()
def listall_azure_Vnets(params: VnetListParameters) -> List[VnetListModel]:
    #subscriptionId = params.subscriptionId
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Network/virtualNetworks"
    api_version = "2023-02-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    Vnet_list = response_data.get('value', [])
    return [VnetListModel(**Vnet) for Vnet in Vnet_list]

@action_store.kubiya_action()
def list_by_rg_azure_Vnets(params: VnetListByRGParameters) -> List[VnetListModel]:
    #subscriptionId = params.subscriptionId
    endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks"
    api_version = "2023-02-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    Vnet_list = response_data.get('value', [])
    return [VnetListModel(**Vnet) for Vnet in Vnet_list]

@action_store.kubiya_action()
def delete_azure_virtual_network(params: VnetDeleteParameters):
    #subscriptionId = params.subscriptionId
    endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{params.vnetName}"
    api_version = "2023-02-01"
    response_data = delete_wrapper(endpoint, params.subscriptionId, api_version)
    if response_data:
        return response_data
    else:
        None

@action_store.kubiya_action()
def update_tags_azure_virtual_network(params: VnetTagsUpdateParameters) -> List[VnetTagsUpdateResponse]:
    #subscriptionId = params.subscriptionId
    endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{params.vnetName}"
    api_version = "2023-02-01"
    tags_data = {
  "tags": params.tags
}
    response_data = patch_wrapper(endpoint, params.subscriptionId, api_version, data=tags_data)
    if response_data:
        return VnetTagsUpdateResponse(**response_data)
    else:
        None

