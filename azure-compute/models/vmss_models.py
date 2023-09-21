from pydantic import BaseModel
from typing import Optional, List, Literal

Regions = Literal["eastus", "eastus2", "westus", "northeurope", "westindia", "southindia"]
Sizes = Literal["Standard_DS2_v2", "Standard_D2s_v4","Standard_D4s_v4","Standard_B2s_v2"]

class VMSSCreationParameters(BaseModel):
    resourceGroupName: str
    vmssName: str
    #networkInterfaceName: str
    location: Regions
    vmssSize: Sizes
    admin_username: str
    admin_password: str
    publisher: str = "Canonical"
    offer: str = "UbuntuServer"
    sku: str = "18.04-LTS"
    vnetName: str = "default"
    subnetName: str = "default-subnet"


class VirtualMachineSSResponseModel(BaseModel):
    sku: Optional[dict]
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: Optional[dict]


class VMSSQueryParameters(BaseModel):
    
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
    None

class VMSSGetParametersByLocation(BaseModel):
    
    resourceGroupName: str
    vmssName: str
    location: str

class VMSSDeleteInstance(BaseModel):
    
    resourceGroupName: str
    vmssName: str

class ListInstancesParameters(BaseModel):
    
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
    
    resourceGroupName: str
    vmssName: str

class VMSSInstanceDeleteParameters(BaseModel):
    
    resourceGroupName: str
    vmssName: str
    instanceId: str

class vmssAvailableSkus(BaseModel):
    
    resourceGroupName: str
    vmssName: str


class VirtualMachineScaleSetInstanceViewResponseModel(BaseModel):
    extensions: Optional[dict]
    statuses: Optional[dict]
    orchestrationServices: Optional[dict]
    virtualMachine: Optional[dict]