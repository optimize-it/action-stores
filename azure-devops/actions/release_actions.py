from .. import action_store as action_store
from ..azure_devops_wrapper import *
# from ..models.project_models import *
from ..models.nic_models import *
from typing import Union
# import json

logger = logging.getLogger(__name__)

class CreateReleaseParameters(BaseModel):
    organization: str
    project: str
    definationId: int
    

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
                            "name": null
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

def delete_release_azure_devops(params: DeleteReleaseParameters):
    api_version = "7.0"
    organization = params.organization
    project = params.project
    endpoint = ""
    response = ""
    return response