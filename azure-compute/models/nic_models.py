from argparse import OPTIONAL
from pydantic import BaseModel
from typing import Optional, List

class NetworkInterfaceCreationParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str = "optit"
    nicName: str
    # ipName: str
    # vnetName: str
    # subnetName: str
    location: str = "eastus"

class NetworkInterfaceResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    location: Optional[str]
    properties: Optional[dict] = {}
    type: Optional[str]

class NetworkInterfaceListAllParameters(BaseModel):
    subscriptionId: str

class PublicIpCreationParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    ipName: str
    location: str

class PublicIpResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    sku: Optional[dict]

class NetworkInterfaceListParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str

class NetworkInterfaceGetParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    nicName: str