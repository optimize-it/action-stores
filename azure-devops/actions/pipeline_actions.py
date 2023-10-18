from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.pipeline_models import *
# from ..models.nic_models import *
from typing import Union
import json

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def create_pipeline_azure_devops(params: CreatePipelineParameters):
    try:
        api_version = "6.0"
        # pipeline_json_config = {
        #                     "phases": [
        #                         {
        #                             "name": "Build",
        #                             "steps": [
        #                                 {
        #                                     "script": "echo Hello, World!",
        #                                     "displayName": "Run a one-line script",
        #                                     "failOnStderr": "true"
        #                                 }
        #                             ]
        #                         }
        #                     ]
        #                 }
        pipeline_data = {
                        'name': params.pipelineName,
                        'configuration': {
                            'repository': {
                                'id': '2a36bd47-4c9e-4dd7-aae4-5d7333756092',
                                'type': 'azureReposGit'
                            },
                            'path': 'azure-pipelines.yml',
                            'type': 'yaml',
                            #'content': pipeline_yaml_base64,
                        }
                    }
        pipeline_data_json = json.dumps(pipeline_data)


        
        endpoint = f"/{params.organization}/{params.project}/_apis/pipelines"
        

        response = post_wrapper_azure_devops(endpoint, api_version, post_data=pipeline_data_json)
        print(response)
        return response
    except Exception as e:
        logger.error(f"Failed to create pipeline : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def get_pipeline(params: GetPipelineParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}"
        response = get_wrapper_azure_devops(endpoint , api_version )
        return response
    except Exception as e:
        logger.error(f"Failed to get pipeline : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def list_pipeline(params: ListPipelineParameters):
    try:
        api_version = "7.1-preview.1 "    
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list pipelines : {e}")
        return {"error": str(e)}


@action_store.kubiya_action()
def get_runs(params: GetRunsParameters):
    try:
        api_version = "7.1-preview.1"   
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs/{params.runId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get runs : {e}")
        return {"error": str(e)}


@action_store.kubiya_action()
def list_runs(params: ListRunsParametes):
    try:
        api_version = "7.0"   
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs"
        response = get_wrapper_azure_devops(endpoint , api_version )
        return response
    except Exception as e:
        logger.error(f"Failed to list runs : {e}")
        return {"error": str(e)}


@action_store.kubiya_action()
def run_pipeline_azure_devops(params: RunPipelineParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs"
        response = post_wrapper_azure_devops(endpoint , api_version, data={})
        return response
    except Exception as e:
        logger.error(f"Failed to run pipeline : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def get_pipeline_logs_azure_devops(params: GetLogsParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs/{params.runId}/logs/{params.logId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get pipeline log : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def list_pipeline_logs_azure_devops(params: ListLogsParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs/{params.runId}/logs"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list pipeline logs : {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
def preview_pipeline_azure_devops(params: PreviewParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        preview_data = {}
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/preview"
        response = post_wrapper_azure_devops(endpoint , api_version, data=preview_data)
        print(response)
        return response
    except Exception as e:
        logger.error(f"Failed to preview pipeline : {e}")
        return {"error": str(e)}    
