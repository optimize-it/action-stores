from pydantic import BaseModel
from typing import Optional, List, Literal

class CreateBuildDefinationParameters(BaseModel):
    organization: str
    project: str

class DeleteBuildDefinationParameters(BaseModel):
    organization: str
    project: str

class GetBuildDefinationParameters(BaseModel):
    organization: str
    project: str
    definitionId: str

class ListBuildDefinationParameters(BaseModel):
    organization: str
    project: str

class DeleteBuildsParameters(BaseModel):
    organization: str
    project: str
    buildId: str

class GetBuildsParameters(BaseModel):
    organization: str
    project: str
    buildId: str 
