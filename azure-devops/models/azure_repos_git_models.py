from pydantic import BaseModel
from typing import Optional, List, Literal

class GetGitReposParameters(BaseModel):
    organization: str
    project: str
    repositoryId: str

class ListRepositoriesParameters(BaseModel):
    None