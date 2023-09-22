from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.project_models import *
# from ..models.nic_models import *
from typing import Union
# import json

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def list_projects(params: ListProjectParameters):
    api_version = "7.0"
    organization = "kubiyaai"
    endpoint = f"/{organization}/_apis/projects"
    response = get_wrapper_azure_devops(endpoint, api_version)
    return response
