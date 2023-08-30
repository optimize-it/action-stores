import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.vmss_models import *
from ..models.vm_models import *
from typing import Union

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_or_update_virtual_machine(params: VMCreationParameters) -> Union[VirtualMachineResponseModel, dict]:
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmssName = params.vmssName
    networkInterfaceName = params.networkInterfaceName
    vmss_data = {
                "sku": {
                  "tier": params.sku_tier,
                  "capacity": params.sku_capacity,
                  "name": params.sku_name
                },
                "location": params.location,
                "properties": {
                  "overprovision": true,
                  "virtualMachineProfile": {
                    "osProfile": {
                      "computerNamePrefix": params.computer_name,
                      "adminUsername": params.admin_username,
                      "adminPassword": params.admin_password
                    },
                    "imageReference": {
                      "sku": params.sku,
                      "publisher": params.publisher,
                      "version": params.version,
                      "offer": params.offer
                    },
                    "networkProfile": {
                    }
                  },
                  "upgradePolicy": {
                    "mode": "Manual"
                  }
                }
              }

    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachinesScaleSets/{vmssName}"
    api_version = "2023-03-01"

    response_data = put_wrapper(endpoint, subscriptionId, api_version, data=vmss_data)

    return VirtualMachineResponseModel(**response_data)



@action_store.kubiya_action()
def get_virtual_machine_scale_set(params: VMSSQueryParameters) -> Union[VirtualMachineSSResponseModel, dict]:
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmssName = params.vmssName

    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}"
    api_version = "2023-07-01"

    response_data = get_wrapper(endpoint, subscriptionId, api_version)

    return VirtualMachineSSResponseModel(**response_data)



@action_store.kubiya_action()
def list_all_virtual_machines_scale_set(params: VMSSListParameters) -> List[VirtualMachineSSListModel]:
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/virtualMachinesScaleSets"
    api_version = "2023-07-01"

    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

    vmss_list = response_data.get('value', [])
    return [VirtualMachineSSListModel(**vmss) for vmss in vmss_list]



# @action_store.kubiya_action()
# def get_subscriptions(params: SubscriptionQueryParameters) -> Union[SubscriptionListResult, dict]:
#     endpoint = "/subscriptions"
#     api_version = "2020-01-01"

#     response_data = get_wrapper(endpoint, '', api_version)

#     return SubscriptionListResult(**response_data)



# @action_store.kubiya_action()
# def get_resource_groups(params: RGQueryParameters) -> Union[ResourceGroupListResult, dict]:
#     subscriptionId = params.subscriptionId
#     endpoint = f"/subscriptions/{subscriptionId}/resourcegroups"
#     api_version = "2021-04-01"

#     response_data = get_wrapper(endpoint, subscriptionId, api_version)

#     if response_data:
#         return ResourceGroupListResult(**response_data)
#     else:
#         return None
    


# @action_store.kubiya_action()
# def get_network_interfaces(params: NetworkInterfaceParams) -> Union[NetworkInterfaceListResult, dict]:
#     endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/networkInterfaces"
#     api_version = "2022-11-01"

#     response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

#     return NetworkInterfaceListResult(**response_data)



# @action_store.kubiya_action()
# def get_publishers(params: PublisherParams):
#     endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/publishers"
#     api_version = "2023-03-01"

#     response_data = get_wrapper(endpoint, "", api_version)

#     return response_data



# @action_store.kubiya_action()
# def get_locations(params: LocationParams): 
#     endpoint = f"/subscriptions/{params.subscriptionId}/locations"
#     api_version = "2020-01-01"

#     response_data = get_wrapper(endpoint, "", api_version)

#     return response_data



# @action_store.kubiya_action()
# def get_versions(params: VersionsParams):
#     endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/publishers/{params.publisherName}/artifacttypes/vmimage/offers/{params.offer}/skus/{params.skus}/versions"
#     api_version = "2023-03-01"

#     response_data = get_wrapper(endpoint, "", api_version)

#     return response_data



# @action_store.kubiya_action()
# def get_skus(params: SkusParams):
#     endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/publishers/{params.publisherName}/artifacttypes/vmimage/offers/{params.offer}/skus"
#     api_version = "2023-03-01"

#     response_data = get_wrapper(endpoint, "", api_version)

#     return response_data



# @action_store.kubiya_action()
# def get_machine_sizes(params: MachineSizesParams):
#     endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/vmSizes"
#     api_version = "2023-03-01"

#     response_data = get_wrapper(endpoint, "", api_version)

#     return response_data

@action_store.kubiya_action()
def list_virtual_machines_scale_set(params: VMSSListParameters) -> List[VirtualMachineSSListModel]:
    endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}providers/Microsoft.Compute/virtualMachinesScaleSets"
    api_version = "2023-07-01"

    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

    vmss_list = response_data.get('value', [])
    return [VirtualMachineSSListModel(**vmss) for vmss in vmss_list]
  
@action_store.kubiya_action()
def deallocate_virtual_machine_scaleset(params: VMSSQueryParameters):
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmssName = params.vmssName
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachinesScaleSets/{vmssName}/Deallocate"
    api_version = "2023-07-01"
    response_data = post_wrapper(endpoint, subscriptionId, api_version)
    return response_data

def restart_virtual_machine_scaleset(params: VMSSQueryParameters):
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmssName = params.vmssName
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachinesScaleSets/{vmssName}/Restart"
    api_version = "2023-07-01"
    response_data = post_wrapper(endpoint, subscriptionId, api_version)
    return response_data

def start_virtual_machine_sccaleset(params: VMSSQueryParameters):
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmssName = params.vmssName
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachinesScaleSets/{vmssName}/Start"
    api_version = "2023-07-01"
    response_data = post_wrapper(endpoint, subscriptionId, api_version)
    return response_data

def instance_view_virtual_machine_scaleset(params: VMSSQueryParameters) -> Union[VirtualMachineSSResponseModel, dict] :
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmssName = params.vmssName
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachinesScaleSets/{vmssName}/instancView"
    api_version = "2023-07-01"
    response_data = post_wrapper(endpoint, subscriptionId, api_version)
    return VirtualMachineSSResponseModel(**response_data)

def redeploy_virtual_machine_scaleset(params: VMSSQueryParameters):
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    vmssName = params.vmssName
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachinesScaleSets/{vmssName}/redeploy"
    api_version = "2023-07-01"
    response_data = post_wrapper(endpoint, subscriptionId, api_version)
    return response_data

@action_store.kubiya_action()
def list_by_location_virtual_machines_scaleset(params: VMSSGetParametersByLocation) -> List[VirtualMachineSSListModel]:
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/virtualMachinesScaleSets"
    api_version = "2023-03-01"

    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

    vm_list = response_data.get('value', [])
    return [VirtualMachineSSListModel(**vmss) for vmss in vm_list]


