from pydantic import BaseModel
from typing import Optional, List, Literal

class CreateRepoParameters(BaseModel):
    organization: str
    project: str
    repoName: str
    projectId: str

class DeleteRepositoryParameters(BaseModel):
    organization: str
    project: str
    repositoryId: str

class UpdateRepositoryParameters(BaseModel):
    isDisabled: bool
    organization: str
    project: str
    repositoryId: str
class GetGitReposParameters(BaseModel):
    organization: str
    project: str
    repositoryIdorName: str

class ListRepositoriesParameters(BaseModel):
    organization: str
    project: str

class CreateMergeParemeters(BaseModel):
    repositoryNameOrId: str
    organization: str
    project: str
    branch1: str
    branch2: str
    comment: str

class GetMergeParemeters(BaseModel):
    mergeOperationId: str
    repositoryNameOrId: str
    organization: str
    project: str

class GetPullRequestParameters(BaseModel):
    pullRequestId: str
    repositoryId: str
    organization: str
    project: str

class GetPullRequestsParameters(BaseModel):
    repositoryId: str
    organization: str
    project: str

class GetPullRequestsByIdParameters(BaseModel):
    pullRequestId: str
    organization: str
    project: str

class GetPullRequestsByProjectParameters(BaseModel):
    organization: str
    project: str
class CreatePushesParameters(BaseModel):
    branchId: str
    repositoryId: str
    organization: str
    project: str
class GetPushesParameters(BaseModel):
    pushId: str
    repositoryId: str
    organization: str
    project: str
class ListPushesParameters(BaseModel):
    repositoryId: str
    organization: str
    project: str

class GetCommitDetailsParameters(BaseModel):
    commitId: str
    repositoryId: str
    organization: str
    project: str

class ChangesCommitParameters(BaseModel):
    commitId: str
    repositoryId: str
    organization: str
    project: str
class GetCommitParameters(BaseModel):
    repositoryId: str
    organization: str
    project: str

class UpdateRefParameters(BaseModel):
    repositoryId: str
    organization: str
    project: str
    filer: str = "heads/master"
    isLocked: bool = False

class UpdateRefsParameters(BaseModel):
    repositoryId: str
    organization: str
    project: str