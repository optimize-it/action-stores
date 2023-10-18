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
    wiqlId: str

class GetWIQLByIdParameters(BaseModel):
    organization : str
    project : str
    team: str
    wiqlId: str

class GetWIQLByWIQLParameters(BaseModel):
    organization : str
    project : str
    team: str
    query: str = "Select [System.Id], [System.Title], [System.State] From WorkItems Where [System.WorkItemType] = 'Task' AND [State] <> 'Closed' AND [State] <> 'Removed' order by [Microsoft.VSTS.Common.Priority] asc, [System.CreatedDate] desc"

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
    workitemIds: str

class UpdateWorkItemParameters(BaseModel):
    organization : str
    project : str
    workitemId: str