
from .. import action_store as action_store
from ..azure_wrapper import *
from ..actions.virtualnetwork_actions import *
from ..models.nic_models import *
from typing import Union
import json

logger = logging.getLogger(__name__)

# class VNETCreationParameters(BaseModel):
#     vnetName: str
#     subscriptionId: str
#     resourceGroupName: str
#     location: str
#     cidr: str = "10.10.0.0/16"
#     subnet_cidr: str = "10.10.0.0/24"
@action_store.kubiya_action()
def create_or_update_network_interface(params: NetworkInterfaceCreationParameters) -> Union[NetworkInterfaceResponseModel,dict ]:
    try:
        api_version = "2023-02-01"
        # VNETCreationParameters(
        #     vnetName = "test-vnet-name",
        #     subscriptionId= params.subscriptionId,
        #     resourceGroupName= params.resourceGroupName,
        #     cidr = "10.16.0.0/16",
        #     location = params.location,
        #     subnet_cidr= "10.16.0.0/24"


        # )
        vnet_response = get_virtual_network(params= VNETGetParameters(
            vnetName = params.vnetName,
            subscriptionId = params.subscriptionId,
            resourceGroupName = params.resourceGroupName
        ))
        if 200 <= vnet_response.status_code < 300:
            vnetName = vnet_response['name']
            subnetName = vnet_response['properties']['subnets'][0]['name']           
        else:
            None

            
            # vnet = create_or_update_virtual_network(params= VNETCreationParameters(
            #     vnetName = "test-vnet-name",
            #     subscriptionId= params.subscriptionId,
            #     resourceGroupName= params.resourceGroupName,
            #     cidr = "10.16.0.0/16",
            #     location = params.location,
            #     subnet_cidr= "10.16.0.0/24"


            # ))
            # vnetName = vnet['name']
            # subnetName = vnet['properties']['subnets'][0]['name']
        public_ip = create_azure_public_ip(PublicIpCreationParameters(
                                            subscriptionId =  params.subscriptionId,
                                            resourceGroupName = params.resourceGroupName,
                                            ipName = f"{params.nicName}-ip",
                                            location=  params.location))
        nic_data = {
                    "properties": {
                        "enableAcceleratedNetworking": True,
                        "ipConfigurations": [
                        {
                            "name": f"{params.nicName}-ipconfig1",
                            "properties": {
                            "publicIPAddress": {
                                "id": f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{public_ip}"
                            },
                            "subnet": {
                                "id": f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}"
                            }
                            }
                        }
                        ]
                    },
                    "location": params.location
                    }
        
        endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{params.nicName}"
        response_data = put_wrapper(endpoint , params.subscriptionId , api_version , data = nic_data)
        return NetworkInterfaceResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get image: {e}")
        raise

def create_azure_public_ip(params: PublicIpCreationParameters) -> [PublicIpResponseModel, dict]:
    resourceGroupName = params.resourceGroupName
    subscriptionId = params.subscriptionId
    api_version = "2023-02-01"
    ipName = params.ipName
    ip_data = {
                # "properties": {
                #     "publicIPAllocationMethod": "Static",
                #     "idleTimeoutInMinutes": 10,
                #     "publicIPAddressVersion": "IPv4"
                # },
                # "sku": {
                #     "name": "Standard",
                #     "tier": "Global"
                # },
                "location": params.location
                }
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{ipName}"
    response_data = put_wrapper(endpoint, subscriptionId, api_version , data = ip_data)
    if response_data.get('name') != None:
        return ipName
    else:
        logger.error("failed to create Ip")

    


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


