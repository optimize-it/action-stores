import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.vm_extensions_models import *
from typing import Union

logger = logging.getLogger(__name__)



@action_store.kubiya_action()
def get_virtual_machine_extensions(params: ExtensionsGetParameters) -> Union[ExtensionGetResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        extensionName = params.availabilitySetName
        vmName = params.vmName
        api_version = "2023-07-01"
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{extensionName}"
        response_data = get_wrapper(endpoint, subscriptionId, api_version)
        return ExtensionGetResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get extension : {e}")
        raise

@action_store.kubiya_action()
def list_virtual_machine_extensions(params: ExtensionsListParameters) -> Union[ExtensionsListResponse, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        vmName = params.vmName
        api_version = "2023-07-01"
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions"
        response_data = get_wrapper(endpoint, subscriptionId, api_version)
        return ExtensionsListResponse(**response_data)
    except Exception as e:
        logger.error(f"Failed to get extension : {e}")
        raise