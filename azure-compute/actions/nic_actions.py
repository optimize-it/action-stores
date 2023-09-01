import logging

from .. import action_store as action_store
from ..azure_wrapper import *
# from ..models.vmss_models import *
from ..models.nic_models import *
from typing import Union

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def create_or_update_azure_networkInterface(params: networkInterfaceCreationParameters) -> Union[networkInterfaceModel, dict]:
    networkInterfaceName = params.networkInterfaceName
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmName = params.vmName
    networkInterface_data = {
                            "properties": {
                                "enableAcceleratedNetworking": True,
                                "disableTcpStateTracking": True,
                                "ipConfigurations": [
                                {
                                    "name": "ipconfig1",
                                    "properties": {
                                    "subnet": {
                                        "id": "/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{params.vnetname}/subnets/{params.subnet_name}"
                                    }
                                    }
                                }
                                ]
                            },
                            "location": params.location
                            }
    endpoint = f"subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/networkInterfaces/{networkInterfaceName}"
    api_version = "2023-02-01"
    response_data = put_wrapper(endpoint, subscriptionId, api_version, data=networkInterface_data)
    return networkInterfaceModel(**response_data)

@action_store.kubiya_action()
def get_azure_networkInterfaces(params: networkInterfaceCreationParameters) -> Union[networkInterfaceModel, dict]:
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    networkInterfaceName = params.networkInterfaceName
    endpoint = f"subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/networkInterfaces/{networkInterfaceName}"
    api_version = "2022-11-01"

    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

    return networkInterfaceModel(**response_data)

@action_store.kubiya_action()
def listall_azure_networkInterfaces(params: networkInterfaceListParameters) -> Union[networkInterfaceListModel, dict]:
    #subscriptionId = params.subscriptionId
    endpoint = f"subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/networkInterfaces"
    api_version = "2022-11-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    networkInterface_list = response_data.get('value', [])
    return [networkInterfaceListModel(**networkInterface) for networkInterface in networkInterface_list]

def list_by_rg_azure_networkInterfaces(params: networkInterfaceListParameters) -> Union[networkInterfaceListModel, dict]:
    #subscriptionId = params.subscriptionId
    endpoint = f"subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/networkInterfaces"
    api_version = "2022-11-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    networkInterface_list = response_data.get('value', [])
    return [networkInterfaceListModel(**networkInterface) for networkInterface in networkInterface_list]
    