from pydantic import BaseModel
from typing import Optional, List

class VNETCreationParameters(BaseModel):
    vnetName: str
    subscriptionId: str
    resourceGroupName: str
    # vmName: str
    location: str
    cidr: list
    subnet_cidr: list
    
class VirtualNetworkResponseModel(BaseModel):
    vnetName: Optional(str)
    location: Optional(str)
    properties: dict
    
class VnetListParameters(BaseModel):
    vnetName: str

class VnetListModel(BaseModel):
    vnetName: Optional(str)
    location: Optional(str)
    
class VnetDeleteParameters(BaseModel):
    vnetName: str
    resourceGroupName: str
    subscriptionId: str