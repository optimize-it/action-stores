from pydantic import BaseModel
from typing import Optional, List, Literal

class GetPipelineParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: str

class ListPipelineParameters(BaseModel):
    organisation: str
    project: str

class GetRunsParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: str
    runId: str

class ListRunsParametes(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: str

class RunPipelineParameters(BaseModel):
    organization: str = "kubiyaai"
    project: str = "kubiya"
    pipelineId: str

class GetLogsParameters(BaseModel):
    organization: str
    project: str
    pipelineId: str
    logId: str
    runId: str

class ListLogsParameters(BaseModel):
    organization: str
    project: str
    pipelineId: str
    runId: str

class PreviewParameters(BaseModel):
    organization: str
    project: str
    pipelineId: str



