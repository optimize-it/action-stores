from pydantic import BaseModel
from typing import Optional, List

class VNETCreationParameters(BaseModel):
    vnetName: str
    subscriptionId: str
    resourceGroupName: str
    location: str
    cidr: str = "10.10.0.0/16"
    subnet_cidr: str = "10.10.0.0/24"

class VNETGetParameters(BaseModel):
    vnetName: str
    subscriptionId: str
    resourceGroupName: str

    
class VirtualNetworkResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    
class VnetListParameters(BaseModel):
    subscriptionId: str

class VnetListByRGParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str

class VnetListModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    
class VnetDeleteParameters(BaseModel):
    vnetName: str
    resourceGroupName: str
    subscriptionId: str

class VnetTagsUpdateParameters(BaseModel):
    vnetName: str
    resourceGroupName: str
    subscriptionId: str
    tags: dict = {}

class VnetTagsUpdateResponse(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: Optional[dict] = {}