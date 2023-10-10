
from pydantic import BaseModel
from typing import Optional, List, Literal


class CreateReleaseParameters(BaseModel):
    organization: str
    project: str
    definationId: int

class GetLogsReleaseParameters(BaseModel):
    organization: str
    project: str
    releaseId: int

class GetLogsReleaseParameters(BaseModel):
    organization: str
    project: str
    releaseId: int

class GetReleaseParameters(BaseModel):
    organization: str
    project: str
    releaseId: int

class ListReleaseParameters(BaseModel):
    organization: str
    project: str

class GetReleaseEnvironmentParameters(BaseModel):
    organization: str
    project: str
    releaseId: int
    environmentId: int

class UpdateReleaseParameters(BaseModel):
    organization: str
    project: str
    releaseId: int

class CreateReleaseDefinitionParameters(BaseModel):
    organization: str
    project: str

class DeleteReleaseDefinitionParameters(BaseModel):
    organization: str
    project: str
    definitionId: int

class GetReleaseDefinitionParameters(BaseModel):
    organization: str
    project: str
    definitionId: int

class ListReleaseDefinitionParameters(BaseModel):
    organization: str
    project: str

class UpdateReleaseDefinitionParameters(BaseModel):
    organization: str
    project: str