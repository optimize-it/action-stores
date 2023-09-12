import logging

from .. import action_store as action_store
from ..azure_wrapper import *
# from ..models.vmss_models import *
from ..models.vmss_models import *
from typing import Union

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_or_update_virtual_machine_scale_set(params: VMSSCreationParameters) -> Union[VirtualMachineSSResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        networkInterfaceName = params.networkInterfaceName
        vmss_data = {
                        "sku": {
                            "tier": "Standard",
                            "capacity": 3,
                            "name": params.size
                        },
                        "location": "westus",
                        "properties": {
                            "overprovision": True,
                            "virtualMachineProfile": {
                            "storageProfile": {
                                "imageReference": {
                                "sku": params.sku,
                                "publisher": params.publisher,
                                "version": params.version,
                                "offer": params.offer
                                },
                                "osDisk": {
                                "caching": "ReadWrite",
                                "managedDisk": {
                                    "storageAccountType": "Standard_LRS"
                                },
                                "createOption": "FromImage"
                                }
                            },
                            "osProfile": {
                                "computerNamePrefix": "{vmss-name}",
                                "adminUsername": "{your-username}",
                                "adminPassword": "{your-password}"
                            },
                            "networkProfile": {
                                "networkInterfaceConfigurations": [
                                {
                                    "name": "{vmss-name}",
                                    "properties": {
                                    "primary": True,
                                    "enableIPForwarding": True,
                                    "ipConfigurations": [
                                        {
                                        "name": "{vmss-name}",
                                        "properties": {
                                            "subnet": {
                                            "id": f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{params.vnet_name}/subnets/{params.subnet_name}"
                                            }
                                        }
                                        }
                                    ]
                                    }
                                }
                                ]
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

        return VirtualMachineSSResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to create vmss: {e}")
        raise


@action_store.kubiya_action()
def get_virtual_machine_scale_set(params: VMSSQueryParameters) -> Union[VirtualMachineSSResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName

        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}"
        api_version = "2023-07-01"

        response_data = get_wrapper(endpoint, subscriptionId, api_version)

        return VirtualMachineSSResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get vmss: {e}")
        raise



@action_store.kubiya_action()
def list_all_virtual_machines_scale_set(params: VMSSListParameters) -> List[VirtualMachineSSListModel]:
    try:
        endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/virtualMachineScaleSets"
        api_version = "2023-07-01"

        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

        vmss_list = response_data.get('value', [])
        return [VirtualMachineSSListModel(**vmss) for vmss in vmss_list]
    except Exception as e:
        logger.error(f"Failed to list all vmss: {e}")
        raise



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
def list_all_instances_virtual_machines_scale_set(params: ListInstancesParameters) -> List[ListInstancesResponseModel]:
    try:
        endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{params.vmssName}/virtualMachines"
        api_version = "2023-07-01"

        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

        vmss_list = response_data.get('value', [])
        return [ListInstancesResponseModel(**vmss) for vmss in vmss_list]
    except Exception as e:
        logger.error(f"Failed to get all instances in vmss: {e}")
        raise
  
@action_store.kubiya_action()
def deallocate_virtual_machine_scaleset(params: VMSSQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/Deallocate"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to deallocate : {e}")
        raise

@action_store.kubiya_action()
def restart_virtual_machine_scaleset(params: VMSSQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/Restart"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to restart : {e}")
        raise

@action_store.kubiya_action()
def start_virtual_machine_sccaleset(params: VMSSQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/Start"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to start : {e}")
        raise

@action_store.kubiya_action()
def redeploy_virtual_machine_scaleset(params: VMSSQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/redeploy"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to redeploy : {e}")
        raise

@action_store.kubiya_action()
def list_by_location_virtual_machines_scaleset(params: VMSSGetParametersByLocation) -> List[VirtualMachineSSListModel]:
    try:
        endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/virtualMachineScaleSets"
        api_version = "2023-03-01"

        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

        vm_list = response_data.get('value', [])
        return [VirtualMachineSSListModel(**vmss) for vmss in vm_list]
    except Exception as e:
        logger.error(f"Failed to list by location : {e}")
        raise

@action_store.kubiya_action()
def delete_virtual_machine_scaleset(params: VMSSQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/redeploy"
        api_version = "2023-07-01"
        response_data = delete_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to delete vmss : {e}")
        raise

@action_store.kubiya_action()
def instance_view_virtual_machine_scaleset(params: VMSSQueryParameters) -> Union[VirtualMachineScaleSetInstanceViewResponseModel, dict] :
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/instanceView"
        api_version = "2023-07-01"
        response_data = get_wrapper(endpoint, subscriptionId, api_version)
        return VirtualMachineScaleSetInstanceViewResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to view instance : {e}")
        raise


@action_store.kubiya_action()
def delete_instance_of_virtual_machine_scaleset(params: VMSSInstanceDeleteParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/virtualMachines/{params.instanceId}"
        api_version = "2023-07-01"
        response_data = delete_wrapper(endpoint, subscriptionId, api_version)
        return VirtualMachineSSResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to delete a instance in vmss : {e}")
        raise

@action_store.kubiya_action()
def power_off_virtual_machine_scale_set(params: VMSSInstanceQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        # /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}/poweroff"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to poweroff vmss : {e}")
        raise

@action_store.kubiya_action()
def list_sku_virtual_machine_scale_set(params: VMSSQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmssName = params.vmssName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachinesScaleSets/{vmssName}/skus"
        api_version = "2023-07-01"
        response_data = get_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to list  sku : {e}")
        raise