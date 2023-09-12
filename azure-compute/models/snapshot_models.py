from pydantic import BaseModel
from typing import Optional, List

class SnapshotCreationParameters(BaseModel):
    snapshotName: str
    subscriptionId: str
    resourceGroupName: str
    diskName: str
    location: str
    
class SnapshotResponseModel(BaseModel):
    name: Optional[str]
    location: Optional[str]
    properties: Optional[dict]

class SnapshotGetParameters(BaseModel):
    snapshotName: str
    subscriptionId: str
    resourceGroupName: str

class SnapshotGetResponseModel(BaseModel):
    snapshotName: Optional[str]
    subscriptionId: Optional[str]
    resourceGroupName: Optional[str]
    id: Optional[str]
    properties: dict

class SnapshotListParameters(BaseModel):
    subscriptionId: str

class SnapshotListByRGParameters(BaseModel):
    subscriptionId: str
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
    subscriptionId: str
    resourceGroupName: str
    