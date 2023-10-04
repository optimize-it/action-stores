from pydantic import BaseModel
from typing import Optional, List, Literal

Organization = Literal["kubiyaai"]

class CreateTestPlanParameters(BaseModel):
    organization : str
    project : str
    testplanName : str
    testplanDescription : str

class DeleteTestPlanParameters(BaseModel):
    organization : str
    project : str
    planId : str

class GetTestPlanParameters(BaseModel):
    organization : str
    project : str
    planId : str

class ListTestPlanParameters(BaseModel):
    organization : str
    project : str

class CreateTestRunsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    runName: str
    planId: int

class DeleteTestRunsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    runId: str

class GetTestRunsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    runId: str

class ListTestRunsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"

class GetTestRunsStatisticsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    runID: int

class GetTestRunsResultsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    runID: int
    testCaseResultId: int

class ListTestRunsResultsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    runID: int