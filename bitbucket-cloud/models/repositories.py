from pydantic import BaseModel
from typing import List
from . import DEFAULT_BB_WORKSPACE

class GetRepositoryParams(BaseModel):
    workspace: str= DEFAULT_BB_WORKSPACE
    repo_slug: str

class GetRepositoryResponse(BaseModel):
    repo: dict


class CreateRepositoryParams(BaseModel):
    workspace: str = DEFAULT_BB_WORKSPACE
    repo_slug: str
    is_private: bool

class CreateRepositoryResponse(BaseModel):
    response: dict

class GetRepositoriesParams(BaseModel):
    workspace: str = DEFAULT_BB_WORKSPACE


class Repository(BaseModel):
    name: str
    full_name: str
    description: str
    slug: str
    is_private: bool
    uuid: str
    created_on: str
    updated_on: str
    size: int
    language: str
    has_issues: bool
    has_wiki: bool
    override_settings: dict
    mainbranch: dict

class GetRepositoriesResponse(BaseModel):
    repos: List[Repository]
