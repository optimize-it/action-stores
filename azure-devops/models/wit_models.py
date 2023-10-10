from pydantic import BaseModel
from typing import Optional, List, Literal

class CreateQueryWITParameters(BaseModel):
    organization : str
    project : str

class GetQueryWITParameters(BaseModel):
    organization : str
    project : str
    queryName: str

class DeleteQueryWITParameters(BaseModel):
    organization : str
    project : str
    queryName: str

class ListQueryWITParameters(BaseModel):
    organization : str
    project : str

class GetWIQLParameters(BaseModel):
    organization : str
    project : str
    team: str
    wiqlId: int

class GetWIQLByIdParameters(BaseModel):
    organization : str
    project : str
    team: str
    wiqlId: int

class GetWIQLByWIQLParameters(BaseModel):
    organization : str
    project : str
    team: str

class CreateWorkItemParameters(BaseModel):
    organization : str
    project : str
    type: str

class DeleteWorkItemParameters(BaseModel):
    organization : str
    project : str
    workitemId: str

class GetWorkItemParameters(BaseModel):
    organization : str
    project : str
    workitemId: str

class ListWorkItemParameters(BaseModel):
    organization : str
    project : str
    workitemIds: list

class UpdateWorkItemParameters(BaseModel):
    organization : str
    project : str
    workitemId: str