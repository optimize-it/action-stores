from pydantic import BaseModel
from typing import Optional, List

class DiskCreationParameters(BaseModel):
    diskName: str
    subscriptionId: str
    resourceGroupName: str
    location: str
    diskSizeGB: int
    
class DiskResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    location: Optional[str]
    type: Optional[str]
    properties: dict

class DiskGetParameters(BaseModel):
    diskName: str
    subscriptionId: str
    resourceGroupName: str
    
class DiskListParameters(BaseModel):
    subscriptionId: str

class DiskListByRGParameters(BaseModel):
    subscriptionId: str
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
    subscriptionId: str
    resourceGroupName: str