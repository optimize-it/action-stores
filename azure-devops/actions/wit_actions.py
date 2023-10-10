from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.wit_models import *
# from ..models.nic_models import *
from typing import Union
# import json

logger = logging.getLogger(__name__)



def create_query_work_item_tracking(params: CreateQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        # query = params.query
        create_data = {
                    "name": "All Bugs",
                    "wiql": "Select [System.Id], [System.Title], [System.State] From WorkItems Where [System.WorkItemType] = 'Bug' order by [Microsoft.VSTS.Common.Priority] asc, [System.CreatedDate] desc"
                    }
        endpoint = f"/{organization}/{project}/_apis/wit/queries/Shared Queries"
        response = post_wrapper_azure_devops(endpoint, api_version, data=create_data)
        return response
    except Exception as e:
        logger.error(f"Failed to create query for work item tracking : {e}")
        return {"error": str(e)}
    
def get_query_work_item_tracking(params: GetQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        queryName = params.queryName
        endpoint = f"/{organization}/{project}/_apis/wit/queries/{queryName}"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get query for work item tracking : {e}")
        return {"error": str(e)}
    
def delete_query_work_item_tracking(params: DeleteQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        queryName = params.queryName
        endpoint = f"/{organization}/{project}/_apis/wit/queries/{queryName}"
        response = delete_wrapper(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to delete query for work item tracking : {e}")
        return {"error": str(e)}
    
def list_query_work_item_tracking(params: ListQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/wit/queries"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list query for work item tracking : {e}")
        return {"error": str(e)}
    

def search_query_work_item_tracking(params: ListQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/wit/queries?$filter=${params.filterby}"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list query for work item tracking : {e}")
        return {"error": str(e)}
    
def get_wiql_work_item_tracking(params: GetWIQLParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        team = params.team
        wiqlId = params.wiqlId
        endpoint = f"/{organization}/{project}/{team}/_apis/wit/wiql/{wiqlId}"
        response = head_wrapper(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get wiql for work item tracking : {e}")
        return {"error": str(e)}
    
def get_wiql_by_id_work_item_tracking(params: GetWIQLByIdParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        team = params.team
        wiqlId = params.wiqlId
        endpoint = f"/{organization}/{project}/{team}/_apis/wit/wiql/{wiqlId}"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get wiql by id for work item tracking : {e}")
        return {"error": str(e)}
    
def get_wiql_by_wiql_work_item_tracking(params: GetWIQLByWIQLParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        team = params.team
        endpoint = f"/{organization}/{project}/{team}/_apis/wit/wiql"
        wiql_data = {
                    "query": "Select [System.Id], [System.Title], [System.State] From WorkItems Where [System.WorkItemType] = 'Task' AND [State] <> 'Closed' AND [State] <> 'Removed' order by [Microsoft.VSTS.Common.Priority] asc, [System.CreatedDate] desc"
                    }
        response = post_wrapper_azure_devops(endpoint, api_version, data=wiql_data)
        return response
    except Exception as e:
        logger.error(f"Failed to get wiql by wiql for work item tracking : {e}")
        return {"error": str(e)}
    
def create_work_item(params: CreateWorkItemParameters):
    try:
        api_version = "7.2-preview.3"
        organization = params.organization
        project = params.project
        type = params.type
        endpoint = f"/{organization}/{project}/_apis/wit/workitems/${type}"
        create_work_item_data = [
                    {
                        "op": "add",
                        "path": "/fields/System.Title",
                        "from": None,
                        "value": "Sample task"
                    }
                    ]
        response = post_wrapper_azure_devops(endpoint, api_version, data=create_work_item_data)
        return response
    except Exception as e:
        logger.error(f"Failed to create work item : {e}")
        return {"error": str(e)}



def delete_work_item(params: DeleteWorkItemParameters):
    try:
        api_version = "7.2-preview.3"
        organization = params.organization
        project = params.project
        workitemId = params.workitemId
        endpoint = f"/{organization}/{project}/_apis/wit/workitems/{workitemId}"
        response = delete_wrapper(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to delete work item : {e}")
        return {"error": str(e)}
    

def get_work_item(params: GetWorkItemParameters):
    try:
        api_version = "7.2-preview.3"
        organization = params.organization
        project = params.project
        workitemId = params.workitemId
        endpoint = f"/{organization}/{project}/_apis/wit/workitems/{workitemId}"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get work item : {e}")
        return {"error": str(e)}
    
def list_work_items(params: ListWorkItemParameters):
    try:
        api_version = "7.2-preview.3"
        organization = params.organization
        project = params.project
        workitemIds = params.workitemIds
        endpoint = f"/{organization}/{project}/_apis/wit/workitems/?ids={workitemIds}&"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list work items : {e}")
        return {"error": str(e)}
    
def update_work_item(params: UpdateWorkItemParameters):
    try:
        api_version = "7.2-preview.3"
        organization = params.organization
        project = params.project
        workitemId = params.workitemId
        update_data = {}
        endpoint = f"/{organization}/{project}/_apis/wit/workitems/{workitemId}"
        response = patch_wrapper(endpoint, api_version, data=update_data)
        return response
    except Exception as e:
        logger.error(f"Failed to update work items : {e}")
        return {"error": str(e)}