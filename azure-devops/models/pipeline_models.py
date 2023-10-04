from pydantic import BaseModel
from typing import Optional, List, Literal

class CreatePipelineParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineName: str
class GetPipelineParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: int

class ListPipelineParameters(BaseModel):
    organization: str
    project: str

class GetRunsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: int
    runId: int

class ListRunsParametes(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: int

class RunPipelineParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: int

class GetLogsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: int
    logId: int
    runId: int

class ListLogsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: int
    runId: int

class PreviewParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: int



