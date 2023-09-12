from pydantic import BaseModel
from typing import Optional, List


class VMSSCreationParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str
    networkInterfaceName: str
    location: str
    vmssSize: str
    computer_name: str
    admin_username: str
    admin_password: str
    publisher: str
    offer: str
    sku: str
    version: str


class VirtualMachineSSResponseModel(BaseModel):
    sku: Optional[dict]
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: Optional[dict]


class VMSSQueryParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str


class VirtualMachineSSListModel(BaseModel):
    sku: Optional[dict]
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: Optional[dict]


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

class ListInstancesParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str

class ListInstancesResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    tags: Optional[dict]

class VMSSInstanceQueryParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str

class VMSSInstanceDeleteParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str
    instanceId: str

class vmssAvailableSkus(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmssName: str


class VirtualMachineScaleSetInstanceViewResponseModel(BaseModel):
    extensions: Optional[dict]
    statuses: Optional[dict]
    orchestrationServices: Optional[dict]
    virtualMachine: Optional[dict]