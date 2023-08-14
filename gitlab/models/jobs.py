from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict
    

class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description='Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description='Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description='Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description='Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description='Token value associated with the GitLab-provided CI_JOB_TOKEN variable.')
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None, description='An array containing the custom variables available to the job.')