from pydantic import BaseModel, Field
from typing import Optional, List, Any

# List Applications

class ListApplicationSetInput(BaseModel):
    projects: Optional[List[str]] = []
    selector: Optional[str] = ""
    appsetNamespace: Optional[str] = ""

class ListApplicationSetByNameInput(BaseModel):
    name: Optional[str] = ""
