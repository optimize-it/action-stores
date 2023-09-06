from pydantic import BaseModel
from typing import Optional, List


class VMSSCreationParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmName: str
    networkInterfaceName: str
    location: str
    vmSize: str
    computer_name: str
    admin_username: str
    admin_password: str
    publisher: str
    offer: str
    sku: str
    version: str


class VirtualMachineSSResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    tags: Optional[dict]
    properties: dict


class VMSSQueryParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str


class VirtualMachineSSListModel(BaseModel):
    id: str
    name: str
    type: str
    location: str
    properties: dict
    tags: Optional[dict] = {}


class VMSSListParameters(BaseModel):
    subscriptionId: str

class VMSSGetParametersByLocation(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str
    location: str

class VMSSDeleteInstance(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str
    instanceIds: list

class ListInstancesParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str

class ListInstancesResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]

class VMSSInstanceQueryParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str
    instanceId: str

class VMSSInstanceDeleteParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str
    instanceId: str

class vmssAvailableSkus(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str