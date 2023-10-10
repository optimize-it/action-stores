from pydantic import BaseModel
from typing import Optional, List, Literal

Organization = Literal["kubiyaai"]
class ListProjectParameters(BaseModel):
    organization: Organization

class CreateProjectParameters(BaseModel):
    projectName: str
    projectDescription: str