import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.availabilityset_models import *
from typing import Union

logger = logging.getLogger(__name__)

subscriptionId = get_subscription_id_secret
@action_store.kubiya_action()
def create_or_update_availabilitysets(params: availabilitysetCreationParameters) -> Union[availabilitysetResponseModel, dict]:
    try:
        # subscriptionId = subscriptionId
        resourceGroupName = params.resourceGroupName
        availabilitySetName = params.availabilitySetName
        availabilityset_data ={
                                "location": params.location,
                                "properties": {
                                    "platformFaultDomainCount": params.fault_domain,
                                    "platformUpdateDomainCount": params.update_domain
                                }
                                }
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
        api_version = "2023-07-01"

        response_data = put_wrapper(endpoint, api_version, data=availabilityset_data)

        return availabilitysetResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to create availability set : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def get_availabilitysets(params: availabilitysetGetParameters) -> Union[availabilitysetResponseModel, dict]:
    try:
        # subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        availabilitySetName = params.availabilitySetName
        api_version = "2023-07-01"
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
        response_data = get_wrapper(endpoint, api_version)
        return availabilitysetResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get availability set: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def list_azure_availabilitysets(params: availabilitysetListParameters) -> Union[availabilitysetListModel, dict]:
    try:
        # subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets"
        api_version = "2023-07-01"
        response_data = get_wrapper(endpoint, api_version)
        availabilityset_list = response_data.get('value', [])
        return [availabilitysetListModel(**availabilityset) for availabilityset in availabilityset_list]
    except Exception as e:
        logger.error(f"Failed to list availability sets: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def list_availablesizes_availabilitysets(params: availabilitysetListAvailableSizesParameters) -> List[availabilitysetListAvailableSizesResponse]:
    try:
        #subscriptionId = params.subscriptionId
        endpoint = f"/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{params.availabilitySetName}/vmSizes"
        api_version = "2023-07-01"
        response_data = get_wrapper(endpoint, api_version)
        sizes_availabilityset_list = response_data.get('value', [])
        return [availabilitysetListAvailableSizesResponse(**sizes_availabilityset) for sizes_availabilityset in sizes_availabilityset_list]
    except Exception as e:
        logger.error(f"Failed to list available sizes for availability set: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def list_all_availabilitysets(params: availabilitysetListAllParameters) -> Union[availabilitysetListModel, dict]:
    try:
        # subscriptionId = params.subscriptionId
        endpoint = f"/providers/Microsoft.Compute/availabilitySets"
        api_version = "2023-07-01"
        response_data = get_wrapper(endpoint, api_version)
        availabilityset_listall = response_data.get('value', [])
        return [availabilitysetListModel(**availabilitysetlistall) for availabilitysetlistall in availabilityset_listall]
    except Exception as e:
        logger.error(f"Failed to list all availability sets: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def delete_availabilitysets(params: availabilitysetDeletetionParameters):
    try:
        # subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        availabilitySetName = params.availabilitySetName
        api_version = "2023-07-01"
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
        response_data = delete_wrapper(endpoint, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to delete availability set: {e}")
        return {"error": str(e)}

# @action_store.kubiya_action()
# def update_availabilitysets(params: availabilitysetDeletetionParameters):
#     try:
#         subscriptionId = params.subscriptionId
#         resourceGroupName = params.resourceGroupName
#         availabilitySetName = params.availabilitySetName
#         api_version = "2023-07-01"
#         endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}"
#         response_data = delete_wrapper(endpoint, subscriptionId, api_version)
#         return response_data
#     except Exception as e:
#         logger.error(f"Failed to delete availability set: {e}")
#         raise