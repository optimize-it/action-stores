from pydantic import BaseModel
from typing import Optional, List, Literal

Regions = Literal["eastus", "eastus2", "westus", "northeurope", "westindia", "southindia"]


class SnapshotCreationParameters(BaseModel):
    snapshotName: str
    
    resourceGroupName: str
    diskName: str
    location: Regions
    
class SnapshotResponseModel(BaseModel):
    name: Optional[str]
    location: Optional[str]
    properties: Optional[dict]

class SnapshotGetParameters(BaseModel):
    snapshotName: str
    
    resourceGroupName: str

class SnapshotGetResponseModel(BaseModel):
    snapshotName: Optional[str]
    subscriptionId: Optional[str]
    resourceGroupName: Optional[str]
    id: Optional[str]
    properties: dict

class SnapshotListParameters(BaseModel):
    None

class SnapshotListByRGParameters(BaseModel):
    
    resourceGroupName: str
    
class SnapshotListModel(BaseModel):
    name: Optional[str]
    location: Optional[str]
    id: Optional[str]
    type: Optional[str]
    properties: dict
    tags: Optional[dict] = {}

class SnapshotDeleteParameters(BaseModel):
    snapshotName: str
    
    resourceGroupName: str
    