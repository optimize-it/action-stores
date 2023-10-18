from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.wit_models import *
# from ..models.nic_models import *
from typing import Union
import json

logger = logging.getLogger(__name__)


@action_store.kubiya_action()
def create_query_work_item_tracking(params: CreateQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        # query = params.query
        create_data = {
                    "name": "All Bugs2",
                    "wiql": "Select [System.Id], [System.Title], [System.State] From WorkItems Where [System.WorkItemType] = 'Bug' order by [Microsoft.VSTS.Common.Priority] asc, [System.CreatedDate] desc"
                    }
        endpoint = f"/{organization}/{project}/_apis/wit/queries/Shared Queries"
        # response = post_wrapper_azure_devops(endpoint, api_version, post_data=create_data)
        def wit_session():
            wit_devops_session = Session()
            wit_devops_session.headers.update({"Content-Type": "application/json","Authorization": f"Bearer {get_token_for_azure_devops()}",})
            return wit_devops_session
        
        # application/json-patch+json
        test = wit_session()
        # session = get_devops_session.headers.update({"Content-Type": "application/json-patch+json",})
        # print(session.headers)
        url = f'https://dev.azure.com/{organization}/{project}/_apis/wit/queries/Shared Queries?api-version=7.0'
        response = test.post(url,json=create_data)
        if 200 <= response.status_code < 300:
            return response.json()
        else:
            response.raise_for_status()
        # return response
    except Exception as e:
        logger.error(f"Failed to create query for work item tracking : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()   
def get_query_work_item_tracking(params: GetQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        queryName = params.queryName
        endpoint = f"/{organization}/{project}/_apis/wit/queries/Shared Queries/All Bugs"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get query for work item tracking : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()   
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
@action_store.kubiya_action()   
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
    
@action_store.kubiya_action()
def search_query_work_item_tracking(params: ListQueryWITParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/wit/queries?$filter=" #{{$'All Bugs'}}#System.Title eq 'Bug'
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list query for work item tracking : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()   
def get_wiql_work_item_tracking(params: GetWIQLParameters):
    try:
        api_version = "7.1-preview.2"
        organization = params.organization
        project = params.project
        team = params.team
        wiqlId = params.wiqlId
        endpoint = f"/{organization}/{project}/{team}/_apis/wit/wiql/{wiqlId}"
        response = head_wrapper(endpoint, api_version)
        print(response)
        return response
    except Exception as e:
        logger.error(f"Failed to get wiql for work item tracking : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()    
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

@action_store.kubiya_action()    
def get_wiql_by_wiql_work_item_tracking(params: GetWIQLByWIQLParameters):
    try:
        api_version = "7.2-preview.2"
        organization = params.organization
        project = params.project
        team = params.team
        endpoint = f"/{organization}/_apis/wit/wiql"
        wiql_data = {
                    "query": params.query
                    }
        response = post_wrapper_azure_devops(endpoint, api_version, post_data=wiql_data)
        return response
    except Exception as e:
        logger.error(f"Failed to get wiql by wiql for work item tracking : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()   
def create_work_item(params: CreateWorkItemParameters):
    try:
        api_version = "7.2-preview.3"
        organization = params.organization
        project = params.project
        type = params.type
        # endpoint = f"/{organization}/{project}/_apis/wit/workitems/${type}"
        create_work_item_data =[{
                        "op": "add",
                        "path": "/fields/System.Title",
                        "value": "Sample task4"
                    }
        ]
        create_work_item_data_json = json.dumps(create_work_item_data)
        # response = post_wrapper_azure_devops(endpoint, api_version, post_data=create_work_item_data)
        def wit_session():
            wit_devops_session = Session()
            wit_devops_session.headers.update({"Content-Type": "application/json-patch+json","Authorization": f"Bearer {get_token_for_azure_devops()}",})
            return wit_devops_session
        
        test = wit_session()
        # session = get_devops_session.headers.update({"Content-Type": "application/json-patch+json",})
        # print(session.headers)
        url = f'https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/$Task?api-version=7.0'
        response = test.post(url,json=create_work_item_data)
        return response.status_code
    except Exception as e:
        logger.error(f"Failed to create work item : {e}")
        return {"error": str(e)}


@action_store.kubiya_action()
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
    
@action_store.kubiya_action()
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

@action_store.kubiya_action()    
def list_work_items(params: ListWorkItemParameters):
    try:
        api_version = "7.2-preview.3"
        organization = params.organization
        project = params.project
        workitemIds = params.workitemIds
        url = f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems?ids={workitemIds}&api-version={api_version}"
        list_session = get_devops_session()
        response = list_session.get(url)
        # response = get_wrapper_azure_devops(endpoint, api_version)
        return response.json()
    except Exception as e:
        logger.error(f"Failed to list work items : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()    
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