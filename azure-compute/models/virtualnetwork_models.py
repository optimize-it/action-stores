from pydantic import BaseModel
from typing import Optional, List, Literal

Regions = Literal["eastus", "eastus2", "westus", "northeurope", "westindia", "southindia"]


class VNETCreationParameters(BaseModel):
    vnetName: str
    resourceGroupName: str
    location: Regions
    cidr: str = "10.10.0.0/16"
    subnet_cidr: str = "10.10.0.0/24"

class VNETGetParameters(BaseModel):
    vnetName: str
    resourceGroupName: str

    
class VirtualNetworkResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    
class VnetListParameters(BaseModel):
    None

class VnetListByRGParameters(BaseModel):
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
    # subscriptionId: str

class VnetTagsUpdateParameters(BaseModel):
    vnetName: str
    resourceGroupName: str
    # subscriptionId: str
    tags: dict = {}

class VnetTagsUpdateResponse(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: Optional[dict] = {}