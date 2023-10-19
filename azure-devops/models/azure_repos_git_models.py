from pydantic import BaseModel
from typing import Optional, List, Literal

org = Literal['kubiyaai']
pro = Literal['kubiya']
class CreateRepoParameters(BaseModel):
    organization: org
    project: pro
    repoName: str
    projectId: str

class DeleteRepositoryParameters(BaseModel):
    organization: org
    project: pro
    repositoryId: str

class UpdateRepositoryParameters(BaseModel):
    isDisabled: bool
    organization: org
    project: pro
    repositoryId: str
class GetGitReposParameters(BaseModel):
    organization: org
    project: pro
    repositoryIdorName: str

class ListRepositoriesParameters(BaseModel):
    organization: org
    project: pro

class CreateMergeParemeters(BaseModel):
    repositoryNameOrId: str
    organization: org
    project: pro
    branch1: str
    branch2: str
    comment: str

class GetMergeParemeters(BaseModel):
    mergeOperationId: str
    repositoryNameOrId: str
    organization: org
    project: pro

class GetPullRequestParameters(BaseModel):
    pullRequestId: str
    repositoryId: str
    organization: org
    project: pro

class GetPullRequestsParameters(BaseModel):
    repositoryId: str
    organization: org
    project: pro

class GetPullRequestsByIdParameters(BaseModel):
    pullRequestId: str
    organization: org
    project: pro

class GetPullRequestsByProjectParameters(BaseModel):
    organization: org
    project: pro
class CreatePushesParameters(BaseModel):
    branchId: str
    repositoryId: str
    organization: org
    project: pro
class GetPushesParameters(BaseModel):
    pushId: str
    repositoryId: str
    organization: org
    project: pro
class ListPushesParameters(BaseModel):
    repositoryId: str
    organization: org
    project: pro

class GetCommitDetailsParameters(BaseModel):
    commitId: str
    repositoryId: str
    organization: org
    project: pro

class ChangesCommitParameters(BaseModel):
    commitId: str
    repositoryId: str
    organization: org
    project: pro
class GetCommitParameters(BaseModel):
    repositoryId: str
    organization: org
    project: pro

class UpdateRefParameters(BaseModel):
    repositoryId: str
    organization: org
    project: pro
    filer: str = "heads/master"
    isLocked: bool = False

class UpdateRefsParameters(BaseModel):
    repositoryId: str
    organization: org
    project: pro