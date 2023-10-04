import logging

from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.build_models import *
from typing import Union


def create_build_defination(params: CreateBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions"
        build_defination = {
                        "name": "MyNewBuildDefinition",
                        "path": "\\",
                        "type": "build",
                        "queue": {
                            "pool": {"name": "Default"}
                        },
                        "repository": {"type": "tfsgit", "id": "1"},
                        "process": {
                            "yamlFilename": "azure-pipelines.yml"
                        }
                    }
        response = post_wrapper_azure_devops(endpoint, api_version, data=build_defination)
        return response
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}

def delete_build_defination(params: DeleteBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions"
        response = delete_wrapper(endpoint, api_version)
        return response       
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()    
def get_build_defination(params: GetBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions/{params.definitionId}"
        response = get_wrapper_azure_devops(endpoint, api_version)        
        return response
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()    
def list_build_defination(params: ListBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
        
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
def delete_builds(params: DeleteBuildsParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}"
        response = delete_wrapper(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()    
def get_builds(params: GetBuildsParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}"
        response = get_wrapper_azure_devops(endpoint, api_version)
        # if 200 <= response.status_code < 300:
        return response
        # else:
        #     return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()    
def get_build_log(params: GetBuildsLogParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}/logs/{params.logId}"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
        # else:
        #     return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to get build log : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()    
def get_builds_changes(params: GetBuildsChangesParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}/changes"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get build changes : {e}")
        return {"error": str(e)}
    
    
@action_store.kubiya_action()    
def get_builds_logs(params: GetBuildsLogsParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}/logs"
        response = get_wrapper_azure_devops(endpoint, api_version)
        if response:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to get build logs : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()    
def list_builds(params: ListBuildsParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds"
        response = get_wrapper_azure_devops(endpoint, api_version)
        if response:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to get build logs : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()    
def queue_builds(params: QueueBuildParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds"
        build_queue_data = {
            "definition": {
                "id": params.buildId
            }
        }
        response = post_wrapper_azure_devops(endpoint, api_version, data=build_queue_data)
        return response
    except Exception as e:
        logger.error(f"Failed to queue build : {e}")
        return {"error": str(e)}
    
def update_builds(params: UpdateBuildParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds"
        build_queue_data = {
            "definition": {
                "id": params.buildId
            }
        }
        response = patch_wrapper(endpoint, api_version, data=build_queue_data)
        return response
    except Exception as e:
        logger.error(f"Failed to queue build : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()    
def builds_get_defination_metrics(params: DefinationMetricsParameters):
    try:
        api_version = "7.0-preview.1"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions/{params.definitionId}/metrics"
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
        
    except Exception as e:
        logger.error(f"Failed to get build logs : {e}")
        return {"error": str(e)}
    
    # {metricAggregationType}

@action_store.kubiya_action()    
def builds_get_Project_metrics(params: ProjectMetricsParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/metrics"  #/{params.metricAggregationType}
        response = get_wrapper_azure_devops(endpoint, api_version)
        return response
        
    except Exception as e:
        logger.error(f"Failed to get build logs : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def build_add_tag(params: AddTagParameters):
    try:
        api_version = "7.0"
        # /{organization}/{project}/_apis/build
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}/tags/{params.tag}"
        response = put_wrapper_azure_devops(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to add tag : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def build_delete_tag(params: DeleteTagParameters):
    try:
        api_version = "7.0"
        # /{organization}/{project}/_apis/build
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}/tags/{params.tag}"
        response = delete_wrapper(endpoint, api_version)
        
            # logger.info(f"Successfully request accepted wit status code {response.status_code}")
        return response
        
    except Exception as e:
        logger.error(f"Failed to delete tag : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def build_get_build_tag(params: GetBuildTagParameters):
    try:
        api_version = "7.0"
        # /{organization}/{project}/_apis/build
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}/tags"
        response = get_wrapper_azure_devops(endpoint, api_version)
        # if 200 <= response.status_code < 300:
            # logger.info(f"Successfully request accepted wit status code {response.status_code}")
        return response
        
    except Exception as e:
        logger.error(f"Failed to get build tag : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def build_get_tags(params: GetTagParameters):
    try:
        api_version = "7.0"
        # /{organization}/{project}/_apis/build
        endpoint = f"/{params.organization}/{params.project}/_apis/build/tags"
        response = get_wrapper_azure_devops(endpoint, api_version)
        # if 200 <= response.status_code < 300:
            # logger.info(f"Successfully request accepted wit status code {response.status_code}")
        return response
        # else:
        #     return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to get tag : {e}")
        return {"error": str(e)}
    

    
@action_store.kubiya_action()
def build_add_tags(params: AddTagsParameters):
    try:
        api_version = "7.0"
        # /{organization}/{project}/_apis/build
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}/tags"
        tags_list = params.tags
        load_data = {
                        "op": "add",
                        "path": "/fields/System.Tags",
                        "value": ",".join(tags_list)
                    }
        response = post_wrapper_azure_devops(endpoint, api_version, data=load_data)
        # if 200 <= response.status_code < 300:
        return response
        # else:
        #     return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to add build tags : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def build_defination_add_tag(params: DefinitionAddTagParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions/{params.definitionId}/tags/{params.tag}"
        response = put_wrapper_azure_devops(endpoint, api_version)
        # if 200 <= response.status_code < 300:
        return response
        # else:
        #     return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to add defination tag : {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def build_add_tags(params: DefinitionAddTagsParameters):
    try:
        api_version = "7.0"
        # /{organization}/{project}/_apis/build
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions/{params.buildId}/tags"
        tags_list = params.tags
        load_data = {
                        "op": "add",
                        "path": "/fields/System.Tags",
                        "value": ",".join(tags_list)
                    }
        response = post_wrapper_azure_devops(endpoint, api_version, data=load_data)
        # if 200 <= response.status_code < 300:
        return response
    except Exception as e:
        logger.error(f"Failed to add build tags : {e}")
        return {"error": str(e)}