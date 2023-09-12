from pydantic import BaseModel
from typing import Optional, List

class availabilitysetCreationParameters(BaseModel):
    availabilitySetName: str
    resourceGroupName: str
    subscriptionId: str
    update_domain: int
    fault_domain: int
    location: str

class availabilitysetGetParameters(BaseModel):
    availabilitySetName: str
    resourceGroupName: str
    subscriptionId: str
    
class availabilitysetResponseModel(BaseModel):
    name: Optional[str]
    type: Optional[str]
    id: Optional[str]
    sku: Optional[dict]
    location: Optional[str]
    properties: Optional[dict]
    
class availabilitysetListParameters(BaseModel):
    resourceGroupName: Optional[str]
    subscriptionId: Optional[str]
    
class availabilitysetListAllParameters(BaseModel):
    subscriptionId: Optional[str]

class availabilitysetListModel(BaseModel):
    name: Optional[str]
    type: Optional[str]
    id: Optional[str]
    sku: Optional[dict]
    location: Optional[str]
    properties: Optional[dict]
    
class availabilitysetListAvailableSizesParameters(BaseModel):
    availabilitySetName: str
    resourceGroupName: str
    subscriptionId: str
    
class availabilitysetListAvailableSizesResponse(BaseModel):
    name: Optional[str]
    numberOfCores: Optional[int]
    osDiskSizeInMB: Optional[int]
    resourceDiskSizeInMB: Optional[int]
    memoryInMB: Optional[int]
    maxDataDiskCount: Optional[int]

class availabilitysetDeletetionParameters(BaseModel):
    availabilitySetName: str
    resourceGroupName: str
    subscriptionId: str
    