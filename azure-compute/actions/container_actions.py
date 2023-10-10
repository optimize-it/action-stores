import logging

from .. import action_store as action_store
from ..azure_wrapper import *
from ..models.container_models import *
from typing import Union

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def list_blob_containers(params: ContainerListParameters) -> List[ContainerResponseModel]:
    try:
        # subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        storageAccountName = params.storageAccountName
        api_version = "2023-01-01"
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{storageAccountName}/blobServices/default/containers"
        response_data = get_wrapper(endpoint, api_version)
        container_list = response_data.get('value', [])
        return [ContainerResponseModel(**container) for container in container_list]
    except Exception as e:
        logger.error(f"Failed to list blob containers set: {e}")
        raise


@action_store.kubiya_action()
def create_blob_containers(params: ContainerCreateParameters) -> Union[ContainerCreateResponseModel, dict]:
    try:
        # subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        storageAccountName = params.storageAccountName
        api_version = "2023-01-01"
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{storageAccountName}/blobServices/default/containers/{params.containerName}"
        response_data = put_wrapper(endpoint, api_version , data = {})
        return ContainerResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to create blob containers: {e}")
        raise




@action_store.kubiya_action()
def get_blob_container_properties(params: GetContainerPropertiesParameters) -> Union[GetContainerPropertiesResponseModel , dict]:
    try:
        # subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        storageAccountName = params.storageAccountName
        api_version = "2023-01-01"
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{storageAccountName}/blobServices/default"
        response_data = get_wrapper(endpoint , api_version)
        return GetContainerPropertiesResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get blob properties: {e}")
        raise

@action_store.kubiya_action()
def set_blob_container_properties(params: SetContainerPropertiesParameters):
    try:
        # subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        storageAccountName = params.storageAccountName
        containerproperties = {
                            "properties": {
                                "cors": {
                                "corsRules": [
                                    {
                                    "allowedOrigins": [
                                        "",
                                        ""
                                    ],
                                    "allowedMethods": [
                                        "GET",
                                        "HEAD",
                                        "POST",
                                        "OPTIONS",
                                        "MERGE",
                                        "PUT"
                                    ],
                                    "maxAgeInSeconds": 100,
                                    "exposedHeaders": [
                                        "x-ms-meta-*"
                                    ],
                                    "allowedHeaders": [
                                        "x-ms-meta-abc",
                                        "x-ms-meta-data*",
                                        "x-ms-meta-target*"
                                    ]
                                    },
                                    {
                                    "allowedOrigins": [
                                        "*"
                                    ],
                                    "allowedMethods": [
                                        "GET"
                                    ],
                                    "maxAgeInSeconds": 2,
                                    "exposedHeaders": [
                                        "*"
                                    ],
                                    "allowedHeaders": [
                                        "*"
                                    ]
                                    },
                                    {
                                    "allowedOrigins": [
                                        "http://www.abc23.com",
                                        "https://www.fabrikam.com/*"
                                    ],
                                    "allowedMethods": [
                                        "GET",
                                        "PUT"
                                    ],
                                    "maxAgeInSeconds": 2000,
                                    "exposedHeaders": [
                                        "x-ms-meta-abc",
                                        "x-ms-meta-data*",
                                        "x -ms-meta-target*"
                                    ],
                                    "allowedHeaders": [
                                        "x-ms-meta-12345675754564*"
                                    ]
                                    }
                                ]
                                },
                                "defaultServiceVersion": "2017-07-29",
                                "deleteRetentionPolicy": {
                                "enabled": True,
                                "days": 300
                                },
                                "isVersioningEnabled": True,
                                "changeFeed": {
                                "enabled": True,
                                "retentionInDays": 7
                                }
                            }
                            }
        api_version = "2023-01-01"
        endpoint = f"/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{storageAccountName}/blobServices/default"
        response_data = get_wrapper(endpoint , api_version, data = containerproperties)
        return GetContainerPropertiesResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to set blob properties: {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def delete_container_from_storage_account(params: DeleteContainerParams):
    try:
        endpoint = f"/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{params.storageAccountName}/blobServices/default/containers/{params.containerName}"
        api_version = "2023-01-01"
        response_data = delete_wrapper(endpoint , api_version)
        return {"Successfully Deleted with status code ":response_data}
    except Exception as e:
        logger.error(f"Failed to delete container: {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()    
def get_blob_from_storage(params: GetBlobParameters):
    endpoint = f"/{params.containerName}/{params.blobName}"
    storageAccountName = params.storageAccountName
    response_data = blob_get_wrapper(endpoint, storageAccountName)
    return response_data


    
# @action_store.kubiya_action()
# def get_blob_properties_from_container(params: GetBlobParametersProperties):
#     endpoint = f"/{params.containerName}/{params.blobName}"
#     storageAccountName = params.storageAccountName
#     response_data = blob_head_wrapper(endpoint, storageAccountName)
#     return response_data

def get_acl_container(params: GetContainerAcl):
    try:
        endpoint = f"/mycontainer?restype=container&comp=acl"
        storageAccountName = params.storageAccountName
        response_data = blob_get_wrapper(endpoint, storageAccountName)
        return response_data
    except Exception as e:
        logger.error(f"Failed to delete container: {e}")
        return {"error": str(e)}
