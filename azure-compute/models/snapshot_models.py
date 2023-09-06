from pydantic import BaseModel
from typing import Optional, List

class SnapshotCreationParameters(BaseModel):
    snapshotName: str
    subscriptionId: str
    resourceGroupName: str
    diskName: str
    location: str
    
class SnapshotResponseModel(BaseModel):
    id: Optional[str]
    type: Optional[str]
    name: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: dict

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
    subscribtionId: str

class SnapshotListByRGParameters(BaseModel):
    subscriptionId: Optional[str]
    resourceGroupName: Optional[str]
    
class SnapshotListModel(BaseModel):
    SnapshotName: Optional[str]
    location: Optional[str]
    id: Optional[str]
    properties: dict
    tags: Optional[dict] = {}

class SnapshotDeleteParameters(BaseModel):
    snapshotName: str
    subscriptionId: str
    resourceGroupName: str
    