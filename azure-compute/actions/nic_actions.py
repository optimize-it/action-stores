
from .. import action_store as action_store
from ..azure_wrapper import *
# from ..models.vmss_models import *
from ..models.nic_models import *
from typing import Union
import json

logger = logging.getLogger(__name__)



def create_or_update_network_interface(params: NetworkInterfaceCreationParameters) -> NetworkInterfaceResponseModel:
    try:
        api_version = "2023-02-01"
        nic_data = {
                    "properties": {
                        "enableAcceleratedNetworking": True,
                        "disableTcpStateTracking": True,
                        "ipConfigurations": [
                        {
                            "name": f"{params.nicName}-ipconfig1",
                            "properties": {
                            "publicIPAddress": {
                                "id": f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{params.ipName}"
                            },
                            "subnet": {
                                "id": f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{params.vnetName}/subnets/{params.subnetName}"
                            }
                            }
                        }
                        ]
                    },
                    "location": params.location
                    }
        
        endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{params.networkInterfaceName}"
    except Exception as e:
        logger.error(f"Failed to get image: {e}")
        raise


def list_all_network_interfaces(params: NetworkInterfaceListAllParameters) -> NetworkInterfaceResponseModel:
    api_version = "2023-02-01"
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Network/networkInterfaces"
    response_data = get_wrapper(endpoint, params.subscriptionId ,  api_version )
    nic_list = response_data.get('value', [])
    return [NetworkInterfaceResponseModel(**nic) for nic in nic_list]

def list_by_rg_network_interfaces(params: NetworkInterfaceListParameters) -> NetworkInterfaceResponseModel:
    api_version = "2023-02-01"
    endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/networkInterfaces"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    nic_list = response_data.get('value', [])
    return [NetworkInterfaceResponseModel(**nic) for nic in nic_list]

# def get_network_interface(params: NetworkInterfaceGetParameters) -> NetworkInterfaceResponseModel:
#         api_version = "2023-02-01"
#         endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{params.nicName}"
#         response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
#         return NetworkInterfaceResponseModel(**response_data)


