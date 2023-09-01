from pydantic import BaseModel
from typing import Optional, List

class SnapshotCreationParameters(BaseModel):
    SnapshotName: str
    subscriptionId: str
    resourceGroupName: str
    vmName: str
    location: str
    
class SnapshotModel(BaseModel):
    id: Optional(str)
    type: Optional(str)
    name: Optional(str)
    location: Optional(str)
    tags: Optional[dict] = {}
    properties: dict
    
class SnapshotListParameters(BaseModel):
    subscribtionId: str
    
class SnapshotListModel(BaseModel):
    SnapshotName: str
    location: str
    id: str
    properties: dict
    tags: Optional[dict] = {}
    