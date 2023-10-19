from pydantic import BaseModel
from typing import Optional, List, Literal

org = Literal['kubiyaai']
pro = Literal['kubiya']

MetricAggregationType = Literal['hourly','daily']
class CreateBuildDefinationParameters(BaseModel):
    organization: org
    project: pro

class DeleteBuildDefinationParameters(BaseModel):
    organization: str
    project: str

class GetBuildDefinationParameters(BaseModel):
    organization: str
    project: str
    definitionId: int

class ListBuildDefinationParameters(BaseModel):
    organization: str
    project: str

class DeleteBuildsParameters(BaseModel):
    organization: str
    project: str
    buildId: int

class GetBuildsParameters(BaseModel):
    organization: str
    project: str
    buildId: int 

class GetBuildsLogParameters(BaseModel):
    organization: str
    project: str
    buildId: int
    logId: int

class GetBuildsChangesParameters(BaseModel):
    organization: str
    project: str
    buildId: int 

class GetBuildsLogsParameters(BaseModel):
    organization: str
    project: str
    buildId: int

class ListBuildsParameters(BaseModel):
    organization: str
    project: str

class QueueBuildParameters(BaseModel):
    organization: str
    project: str
    buildId: int

class UpdateBuildParameters(BaseModel):
    organization: str
    project: str
    buildId: int

class DefinationMetricsParameters(BaseModel):
    organization: str
    project: str
    definitionId: int

class ProjectMetricsParameters(BaseModel):
    organization: str
    project: str
    metricAggregationType: MetricAggregationType

class AddTagParameters(BaseModel):
    organization: str
    project: str
    buildId: int
    tag: str

class DeleteTagParameters(BaseModel):
    organization: str
    project: str
    buildId: int
    tag: str

class GetBuildTagParameters(BaseModel):
    organization: str
    project: str
    buildId: int

class GetTagParameters(BaseModel):
    organization: str
    project: str
class AddTagsParameters(BaseModel):
    organization: str
    project: str
    buildId: int
    tags: list = ["tag1","tag2"]

    
class DefinitionAddTagParameters(BaseModel):
    organization: str
    project: str
    definitionId: int
    tag: str  
class DefinitionAddTagsParameters(BaseModel):
    organization: str
    project: str
    buildId: int
    tags: str
    