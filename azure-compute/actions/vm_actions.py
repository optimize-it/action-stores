import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.vm_models import *
from typing import Union

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_or_update_virtual_machine(params: VMCreationParameters) -> Union[VirtualMachineResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName
        networkInterfaceName = params.networkInterfaceName
        vm_data = {
            "location": params.location,
            "properties": {
                "hardwareProfile": {"vmSize": params.vmSize},
                "osProfile": {
                    "computerName": params.computer_name,
                    "adminUsername": params.admin_username,
                    "adminPassword": params.admin_password,
                },
                "storageProfile": {
                    "imageReference": {
                        "publisher": params.publisher,
                        "offer": params.offer,
                        "sku": params.sku,
                        "version": params.version,
                    },
                },
                "networkProfile": {
                    "networkInterfaces": [
                        {
                            "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkInterfaces/{networkInterfaceName}",
                            "properties": {
                                "primary": True
                            }
                        }
                    ]
                }
            }
        }

        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}"
        api_version = "2023-03-01"

        response_data = put_wrapper(endpoint, subscriptionId, api_version, data=vm_data)

        return VirtualMachineResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to create virtual machine : {e}")
        raise



@action_store.kubiya_action()
def get_virtual_machine(params: VMQueryParameters) -> Union[VirtualMachineResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName

        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}"
        api_version = "2023-03-01"

        response_data = get_wrapper(endpoint, subscriptionId, api_version)

        return VirtualMachineResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get the VM : {e}")
        raise



@action_store.kubiya_action()
def list_all_virtual_machines(params: VMListParameters) -> List[VirtualMachineListModel]:
    try:
        endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/virtualMachines"
        api_version = "2023-03-01"

        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

        vm_list = response_data.get('value', [])
        return [VirtualMachineListModel(**vm) for vm in vm_list]
    except Exception as e:
        logger.error(f"Failed to list all VMs : {e}")
        raise



@action_store.kubiya_action()
def get_subscriptions(params: SubscriptionQueryParameters) -> Union[SubscriptionListResult, dict]:
    try:
        endpoint = "/subscriptions"
        api_version = "2020-01-01"

        response_data = get_wrapper(endpoint, '', api_version)

        return SubscriptionListResult(**response_data)
    except Exception as e:
        logger.error(f"Failed to get subscription : {e}")
        raise



@action_store.kubiya_action()
def get_resource_groups(params: RGQueryParameters) -> Union[ResourceGroupListResult, dict]:
    try:
        subscriptionId = params.subscriptionId
        endpoint = f"/subscriptions/{subscriptionId}/resourcegroups"
        api_version = "2021-04-01"

        response_data = get_wrapper(endpoint, subscriptionId, api_version)

        if response_data:
            return ResourceGroupListResult(**response_data)
        else:
            return None
    except Exception as e:
        logger.error(f"Failed to get resource group : {e}")
        raise


@action_store.kubiya_action()
def get_network_interfaces(params: NetworkInterfaceParams) -> Union[NetworkInterfaceListResult, dict]:
    try:
        endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Network/networkInterfaces"
        api_version = "2022-11-01"

        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

        return NetworkInterfaceListResult(**response_data)
    except Exception as e:
        logger.error(f"Failed to get_network_interfaces : {e}")
        raise



@action_store.kubiya_action()
def get_publishers(params: PublisherParams):

    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/publishers"
    api_version = "2023-03-01"

    response_data = get_wrapper(endpoint, "", api_version)

    return response_data



@action_store.kubiya_action()
def get_locations(params: LocationParams): 
    endpoint = f"/subscriptions/{params.subscriptionId}/locations"
    api_version = "2020-01-01"

    response_data = get_wrapper(endpoint, "", api_version)

    return response_data



@action_store.kubiya_action()
def get_versions(params: VersionsParams):
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/publishers/{params.publisherName}/artifacttypes/vmimage/offers/{params.offer}/skus/{params.skus}/versions"
    api_version = "2023-03-01"

    response_data = get_wrapper(endpoint, "", api_version)

    return response_data



@action_store.kubiya_action()
def get_skus(params: SkusParams):
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/publishers/{params.publisherName}/artifacttypes/vmimage/offers/{params.offer}/skus"
    api_version = "2023-03-01"

    response_data = get_wrapper(endpoint, "", api_version)

    return response_data



@action_store.kubiya_action()
def get_machine_sizes(params: MachineSizesParams):
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/vmSizes"
    api_version = "2023-03-01"

    response_data = get_wrapper(endpoint, "", api_version)

    return response_data

@action_store.kubiya_action()
def delete_virtual_machine(params: VMQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName

        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}"
        api_version = "2023-07-01"

        response_data = delete_wrapper(endpoint, subscriptionId, api_version)

        return response_data
    except Exception as e:
        logger.error(f"Failed to delete VM : {e}")
        raise

@action_store.kubiya_action()
def poweroff_virtual_machine(params: VMQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName

        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/powerOff"
        api_version = "2023-07-01"

        response_data = post_wrapper(endpoint, subscriptionId, api_version)

        return response_data
    except Exception as e:
        logger.error(f"Failed to poweroff VM : {e}")
        raise

@action_store.kubiya_action()
def deallocate_virtual_machine(params: VMQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName

        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/deallocate"
        api_version = "2023-07-01"

        response_data = post_wrapper(endpoint, subscriptionId, api_version)

        return response_data
    except Exception as e:
        logger.error(f"Failed to deallocate VM : {e}")
        raise

@action_store.kubiya_action()
def restart_virtual_machine(params: VMQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName

        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/restart"
        api_version = "2023-07-01"

        response_data = post_wrapper(endpoint, subscriptionId, api_version)

        return response_data
    except Exception as e:
        logger.error(f"Failed to restart VM : {e}")
        raise

@action_store.kubiya_action()
def redeploy_virtual_machine(params: VMQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/redeploy"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to redeploy VM : {e}")
        raise

@action_store.kubiya_action()
def instance_view_virtual_machine(params: VMQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/instanceView"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to view instance: {e}")
        raise

@action_store.kubiya_action()
def start_virtual_machine(params: VMQueryParameters):
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/start"
        api_version = "2023-07-01"
        response_data = post_wrapper(endpoint, subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to start VM : {e}")
        raise

@action_store.kubiya_action()
def list_virtual_machine(params: VMQueryParameters) -> List[VirtualMachineResponseModel]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines"
        api_version = "2023-07-01"
        response_data = get_wrapper(endpoint, subscriptionId, api_version)
        vm_list = response_data.get('value', [])
        return [VirtualMachineListModel(**vm) for vm in vm_list]
    except Exception as e:
        logger.error(f"Failed to list VM : {e}")
        raise

@action_store.kubiya_action()
def list_by_location_virtual_machine(params: VMByLocationListParameters) -> List[VirtualMachineListModel]:
    try:
        subscriptionId = params.subscriptionId
        # resourceGroupName = params.resourceGroupName
        endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/locations/{params.location}/virtualMachines"
        api_version = "2023-07-01"
        response_data = get_wrapper(endpoint, subscriptionId, api_version)
        vm_list = response_data.get('value', [])
        return [VirtualMachineListModel(**vm) for vm in vm_list]
    except Exception as e:
        logger.error(f"Failed to list VMs : {e}")
        raise