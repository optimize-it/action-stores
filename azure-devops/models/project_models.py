from pydantic import BaseModel
from typing import Optional, List, Literal

class ListProjectParameters(BaseModel):
    organization: str