from pydantic import BaseModel
from typing import Optional, List, Literal

Regions = Literal["eastus", "eastus2", "westus", "northeurope", "westindia", "southindia"]

class DiskCreationParameters(BaseModel):
    diskName: str
    
    resourceGroupName: str
    location: Regions
    diskSizeGB: int
    
class DiskResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    location: Optional[str]
    type: Optional[str]
    properties: dict

class DiskGetParameters(BaseModel):
    diskName: str
    
    resourceGroupName: str
    
class DiskListParameters(BaseModel):
    None

class DiskListByRGParameters(BaseModel):
    
    resourceGroupName: str
    
class DiskListModel(BaseModel):
    name: str
    location: str
    type: str
    id: str
    properties: dict
    tags: Optional[dict] = {}

    
class DiskDeleteParameters(BaseModel):
    diskName: str
    
    resourceGroupName: str