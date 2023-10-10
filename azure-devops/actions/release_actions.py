from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.release_models import *
# from ..models.nic_models import *
from typing import Union
# import json

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def create_release_azure_devops(params: CreateReleaseParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    release_data = {
                    "definitionId": 1,
                    "description": "Creating Sample release",
                    "artifacts": [
                        {
                        "alias": "Fabrikam.CI",
                        "instanceReference": {
                            "id": "2",
                            "name": None
                        }
                        }
                    ],
                    "isDraft": False,
                    "reason": "none",
                    "manualEnvironments": None
                    }
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases"
    response = post_wrapper_azure_devops(endpoint, api_version, data = release_data)
    return response

# def delete_release_azure_devops(params: DeleteReleaseParameters):
#     api_version = "7.0"
#     organization = params.organization
#     project = params.project
#     endpoint = ""
#     response = ""
#     return response

@action_store.kubiya_action()
def release_get_logs_azure_devops(params: GetLogsReleaseParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    releaseId = params.releaseId
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases/{releaseId}/logs"
    response = get_wrapper_azure_devops(endpoint, api_version)
    return response


@action_store.kubiya_action()
def get_release_azure_devops(params: GetReleaseParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    releaseId = params.releaseId
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases/{releaseId}"
    response = get_wrapper_azure_devops(endpoint, api_version)
    return response

@action_store.kubiya_action()
def list_release_azure_devops(params: ListReleaseParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases"
    response = get_wrapper_azure_devops(endpoint, api_version)
    return response

@action_store.kubiya_action()
def update_release_azure_devops(params: UpdateReleaseParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    releaseId = params.releaseId
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases/{releaseId}"
    update_data = {}
    response = put_wrapper_azure_devops(endpoint, api_version,data=update_data)
    return response

@action_store.kubiya_action()
def get_release_environment_azure_devops(params: GetReleaseEnvironmentParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    releaseId = params.releaseId
    environmentId = params.environmentId
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/Release/releases/{releaseId}/environments/{environmentId}"
    release_env_data = {
                        "status": "inProgress",
                        "scheduledDeploymentTime": None,
                        "comment": None,
                        "variables": {}
                        }
    response = patch_wrapper(endpoint, api_version,data=release_env_data)
    return response


@action_store.kubiya_action()
def create_release_definition(params: CreateReleaseDefinitionParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions"
    release_definition_data = {}
    response = post_wrapper_azure_devops(endpoint, api_version,data=release_definition_data)
    return response

@action_store.kubiya_action()
def delete_release_definition(params: DeleteReleaseDefinitionParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    definitionId = params.definitionId
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions/{definitionId}"
    response = delete_wrapper(endpoint, api_version)
    return response

@action_store.kubiya_action()
def get_release_definition(params: GetReleaseDefinitionParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    definitionId = params.definitionId
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions/{definitionId}"
    response = get_wrapper_azure_devops(endpoint, api_version)
    return response

@action_store.kubiya_action()   
def list_release_definition(params: ListReleaseDefinitionParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions"
    response = get_wrapper_azure_devops(endpoint, api_version)
    return response

@action_store.kubiya_action()
def update_release_definition(params: UpdateReleaseDefinitionParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    update_release_defination_date = {}
    endpoint = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions"
    response = put_wrapper_azure_devops(endpoint, api_version, data=update_release_defination_date)
    return response
