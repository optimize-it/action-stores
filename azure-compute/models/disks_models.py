<<<<<<< HEAD
from pydantic import BaseModel
from typing import Optional, List

class DiskCreationParameters(BaseModel):
    diskName: str
    subscriptionId: str
    resourceGroupName: str
    location: str
    
class DiskResponseModel(BaseModel):
    id: str
    type: str
    name: str
    location: str
    tags: Optional[dict] = {}
    properties: dict
    
class DiskListParameters(BaseModel):
    subscribtionId: Optional(str)
    
class DiskListModel(BaseModel):
    diskName: str
    location: str
    id: str
    properties: dict
    tags: Optional[dict] = {}
    
class DiskDeleteParameters(BaseModel):
    diskName: str
    subscriptionId: str
    resourceGroupName: str