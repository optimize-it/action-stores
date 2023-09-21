from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.pipeline_models import *
# from ..models.nic_models import *
from typing import Union
# import json

logger = logging.getLogger(__name__)




def get_pipeline(params: GetPipelineParameters):
    try:
        api_version = "6.0-preview.1"
        organization = params.organisationName
        project = params.projectName
        endpoint = f"/{organization}/{project}/_apis/pipelines"
        response = get_wrapper_azure_devops(endpoint , api_version )
        return response
    except Exception as e:
        logger.error(f"Failed to get pipeline : {e}")
        return {"error": str(e)}

def list_pipeline(params: ListPipelineParameters):
    try:
        api_version = "7.1-preview.1 "    
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response.json()
    except Exception as e:
        logger.error(f"Failed to list pipelines : {e}")
        return {"error": str(e)}



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



def list_runs(params: ListRunsParametes):
    try:
        api_version = "7.1-preview.1"   
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs"
        response = get_wrapper_azure_devops(endpoint , api_version )
        return response.json()
    except Exception as e:
        logger.error(f"Failed to list runs : {e}")
        return {"error": str(e)}


def run_pipeline_azure_devops(params: RunPipelineParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organisationName
        project = params.projectName
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs"
        response = post_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to run pipeline : {e}")
        return {"error": str(e)}

def get_pipeline_logs_azure_devops(params: GetLogsParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organisationName
        project = params.projectName
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs/{params.runId}/logs/{params.logId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get pipeline log : {e}")
        return {"error": str(e)}

def list_pipeline_logs_azure_devops(params: ListLogsParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organisationName
        project = params.projectName
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/runs/{params.runId}/logs"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response.json()
    except Exception as e:
        logger.error(f"Failed to list pipeline logs : {e}")
        return {"error": str(e)}

def preview_pipeline_azure_devops(params: PreviewParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organisationName
        project = params.projectName
        endpoint = f"/{organization}/{project}/_apis/pipelines/{params.pipelineId}/preview"
        response = post_wrapper_azure_devops(endpoint , api_version)
        return response.json()
    except Exception as e:
        logger.error(f"Failed to preview pipeline : {e}")
        return {"error": str(e)}
