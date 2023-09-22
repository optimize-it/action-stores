import logging

from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.build_models import *
from typing import Union


def create_build_defination(params: CreateBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions"
        response = post_wrapper_azure_devops(endpoint, api_version)
        if 200 <= response.status_code < 300:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}

def delete_build_defination(params: DeleteBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions"
        response = delete_wrapper(endpoint, api_version)
        if 200 <= response.status_code < 300:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
def get_build_defination(params: GetBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions/{params.definitionId}"
        response = get_wrapper_azure_devops(endpoint, api_version)
        if 200 <= response.status_code < 300:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
def list_build_defination(params: ListBuildDefinationParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/definitions"
        response = get_wrapper_azure_devops(endpoint, api_version)
        if 200 <= response.status_code < 300:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
def delete_builds(params: DeleteBuildsParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}"
        response = delete_wrapper(endpoint, api_version)
        if 200 <= response.status_code < 300:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
def get_builds(params: GetBuildsParameters):
    try:
        api_version = "7.0"
        endpoint = f"/{params.organization}/{params.project}/_apis/build/builds/{params.buildId}"
        response = delete_wrapper(endpoint, api_version)
        if 200 <= response.status_code < 300:
            return response
        else:
            return {"Failed": response}
    except Exception as e:
        logger.error(f"Failed to create build defination : {e}")
        return {"error": str(e)}
    
    
    