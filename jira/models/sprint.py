from pydantic import BaseModel, Field, constr
from typing import List


class SprintParams(BaseModel):
    name: str
    board_id: constr(regex=r'^(2)$') = '2'
    start_date: str
    end_date: str


class SprintResponse(BaseModel):
    id: int
    self: str
    state: str
    name: str
    startDate: str
    endDate: str
    originBoardId: int

class EndSprintParams(BaseModel):
    sprint_id: int

class EndSprintResponse(BaseModel):
    success: bool

class AddIssueToSprintParams(BaseModel):
    sprint_id: int
    issue_key: str

class AddIssueToSprintResponse(BaseModel):
    success: bool

class GetAllSprintsParams(BaseModel):
    board_id: constr(regex=r'^(2)$') = '2'

class SprintData(BaseModel):
    id: int
    name: str
    state: str = Field(..., alias='complete')

class GetAllSprintsResponse(BaseModel):
    sprints: List[SprintData]

class GetBoardIDRequest(BaseModel):
    board_name: str