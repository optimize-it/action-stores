import logging

from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.azure_repos_git_models import *
from typing import Union

logger = logging.getLogger(__name__)

def azure_repos_get_git_repository(params: GetGitReposParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryName}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get azure repos: {e}")
        return {"error": str(e)}
    
def azure_repos_get_git_repostiroty_with_parents(params: GetGitReposParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}?includeParent=True"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get azure repos: {e}")
        return {"error": str(e)}

def azure_repos_list_all_repositories(params: ListRepositoriesParameters):  
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
def azure_repos_create_merge(params: CreateMergeParemeters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryNameOrId}/merges"
        response = post_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
def azure_repos_get_merge(params: GetMergeParemeters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryNameOrId}/merges/{params.mergeOperationId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}

def azure_repos_get_pull_requests(params: GetPullRequestsParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/pullrequests/{params.pullRequestId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
    

def azure_repos_get_pull_requests_by_id(params: GetPullRequestsByIdParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/pullrequests/{params.pullRequestId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
def azure_repos_get_pull_requests_by_project(params: GetPullRequestsByProjectParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/pullrequests"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
def azure_repos_get_pushes(params: GetPushesParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/pushes/{params.pushId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
    
def azure_repos_list_pushes(params: ListPushesParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{repositoryId}/pushes"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}

def azure_repos_get_details_commit(params: GetCommitDetailsParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"{organization}/{project}/_apis/git/repositories/{params.repositoryId}/commits/{params.commitId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
def azure_repos_get_changes_commit(params: ChangesCommitParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/commits/{params.commitId}/changes"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}
    
    

def azure_repos_get_commits(params: GetCommitParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/commits"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get commits: {e}")
        return {"error": str(e)}