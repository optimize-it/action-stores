import logging

from .. import action_store as action_store
from ..azure_devops_wrapper import *
from ..models.azure_repos_git_models import *
from typing import Union

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def azure_repos_create_git_repository(params: CreateRepoParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        repo_data = {
                        "name": params.repoName,
                        "project": {
                            "id": params.projectId
                                }
                     }
        
        endpoint = f"/{organization}/{project}/_apis/git/repositories"
        response = post_wrapper_azure_devops(endpoint , api_version , data=repo_data)
        return response
    except Exception as e:
        logger.error(f"Failed to get azure repos: {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def azure_repos_delete_repository(params: DeleteRepositoryParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}"
        response = delete_wrapper(endpoint, api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to delete azure repository: {e}")
        return {"error": str(e)} 

@action_store.kubiya_action()  
def azure_repos_update_repository(params: UpdateRepositoryParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        update_data = {
                        "isDisabled": params.isDisabled
                        }
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}"
        response = patch_wrapper(endpoint, api_version, data=update_data)
    except Exception as e:
        logger.error(f"Failed to delete azure repository: {e}")
        return {"error": str(e)} 


@action_store.kubiya_action()
def azure_repos_get_git_repository(params: GetGitReposParameters):
    try:
        api_version = "7.0"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryIdorName}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get azure repos: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()   
def azure_repos_get_git_repostiroty_with_parents(params: GetGitReposParameters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryIdorName}?includeParent=True"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to get azure repos: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()
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

@action_store.kubiya_action()   
def azure_repos_create_merge(params: CreateMergeParemeters):
    try:
        api_version = "7.1-preview.1"
        organization = params.organization
        merge_data = {
                "parents": [
                    params.branch1,
                    params.branch2
                ],
                "comment": params.comment
                }
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryNameOrId}/merges"
        response = post_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()     
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
    

@action_store.kubiya_action() 
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
    
    
@action_store.kubiya_action() 
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
    
@action_store.kubiya_action()     
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


@action_store.kubiya_action()     
def azure_repos_create_pushes(params: CreatePushesParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        push_data = {
                    "refUpdates": [
                        {
                        "name": "refs/heads/master",
                        "oldObjectId": params.branchId
                        }
                    ],
                    "commits": [
                        {
                        "comment": "Initial commit.",
                        # "changes": [
                        #     {
                        #     "changeType": "add",
                        #     "item": {
                        #         "path": params.filenamewithlocation
                        #     },
                        #     "newContent": {
                        #         "content": "My first file!",
                        #         "contentType": "rawtext"
                        #     }
                        #     }
                        # ]
                        }
                    ]
                    }
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/pushes"
        response = post_wrapper_azure_devops(endpoint , api_version, data=push_data)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()     
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
    
@action_store.kubiya_action()     
def azure_repos_list_pushes(params: ListPushesParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/pushes"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}

@action_store.kubiya_action() 
def azure_repos_get_details_commit(params: GetCommitDetailsParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/commits/{params.commitId}"
        response = get_wrapper_azure_devops(endpoint , api_version)
        return response
    except Exception as e:
        logger.error(f"Failed to list azure repos: {e}")
        return {"error": str(e)}

@action_store.kubiya_action()     
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
    
    
@action_store.kubiya_action() 
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
    
@action_store.kubiya_action()
def azure_repos_get_refs(params: GetCommitParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/refs"
        response = get_wrapper_azure_devops(endpoint , api_version)
        refs_list = response.get('value', [])
        # availabilityset_list = response_data.get('value', [])
        # return [availabilitysetListModel(**availabilityset) for availabilityset in availabilityset_list]
        return [refs for refs in refs_list]
    except Exception as e:
        logger.error(f"Failed to get commits: {e}")
        return {"error": str(e)}
    
@action_store.kubiya_action()
def azure_repos_update_ref(params: UpdateRefParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        ref_data = {
                "isLocked": params.isLocked
                }
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/refs?filter={params.filter}&api-version={api_version}"
        response = patch_wrapper(endpoint , api_version, data=ref_data)
        # refs_list = response.get('value', [])
        # availabilityset_list = response_data.get('value', [])
        # return [availabilitysetListModel(**availabilityset) for availabilityset in availabilityset_list]
        return response
    except Exception as e:
        logger.error(f"Failed to update ref: {e}")
        return {"error": str(e)}
    
def azure_repos_update_refs(params: UpdateRefsParameters):
    try:
        api_version = "7.2-preview.1"
        organization = params.organization
        project = params.project
        refs_data = [
                    {
                        "name": "refs/heads/vsts-api-sample/answer-woman-flame",
                        "oldObjectId": "0000000000000000000000000000000000000000",
                        "newObjectId": "ffe9cba521f00d7f60e322845072238635edb451"
                    }
                    ]
        endpoint = f"/{organization}/{project}/_apis/git/repositories/{params.repositoryId}/refs"
        response = post_wrapper_azure_devops(endpoint , api_version, data=refs_data)
        # refs_list = response.get('value', [])
        # availabilityset_list = response_data.get('value', [])
        # return [availabilitysetListModel(**availabilityset) for availabilityset in availabilityset_list]
        return response
    except Exception as e:
        logger.error(f"Failed to update refs: {e}")
        return {"error": str(e)}