import logging

from .. import action_store as action_store
from ..azure_wrapper import *
# from ..models.vmss_models import *
from ..models.image_models import *
from typing import Union
import json

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def create_or_update_azure_image(params: ImageCreationParameters) -> Union[ImageModel, dict]:
    try:
        imageName = params.imageName
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        imageName = params.vmName
        image_data = {
                    "location": params.location,
                    "properties": {
                    "sourceVirtualMachine": {
                        "id": f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{params.vmName}"
                                            },
                    "storageProfile": {
                        "osDisk": {
                            "osState": "Specialized"
                                                        }
                    }
                    }}
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}"
        api_version = "2023-07-01"
        response_data = put_wrapper(endpoint, subscriptionId, api_version, data=image_data)
        if response_data.get('id') != None:
            return ImageModel(**response_data)
        else:
            logger.error(f"returned values: {response_data}")
    except Exception as e:
        logger.error(f"Failed to get image: {e}")
        raise

@action_store.kubiya_action()
def get_azure_images(params: ImageGetParameters) -> Union[ImageModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        imageName = params.imageName
        endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}"
        api_version = "2023-07-01"

        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

        return ImageModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get image: {e}")
        raise

@action_store.kubiya_action()
def listall_azure_images(params: ImageListParameters) -> Union[ImageListModel, dict]:
    #subscriptionId = params.subscriptionId
    endpoint = f"/subscriptions/{params.subscriptionId}/providers/Microsoft.Compute/images"
    api_version = "2023-07-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    image_list = response_data.get('value', [])
    return [ImageListModel(**image) for image in image_list]

@action_store.kubiya_action()
def list_by_rg_azure_images(params: ImageListParameters) -> Union[ImageListModel, dict]:
    #subscriptionId = params.subscriptionId
    endpoint = f"/subscriptions/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/images"
    api_version = "2023-07-01"
    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
    image_list = response_data.get('value', [])
    return [ImageListModel(**image) for image in image_list]


@action_store.kubiya_action()
def delete_azure_images(params: ImageDeletetionParameters):
    subscriptionId = params.subscriptionId
    resourceGroupName = params.resourceGroupName
    imageName = params.imageName
    endpoint = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}"
    api_version = "2023-07-01"

    response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

    return response_data
    