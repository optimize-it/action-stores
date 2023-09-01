from pydantic import BaseModel
from typing import Optional, List

class availabilitysetCreationParameters(BaseModel):
    availabilitySetName: str
    resourceGroupName: str
    subscriptionId:str
    
class availabilitysetResponseModel(BaseModel):
    availabilitySetName: Optional(str)
    resourceGroupName: Optional(str)
    location: Optional(str)
    subscriptionId: Optional(str)
    
class availabilitysetListParameters(BaseModel):
    resourceGroupName: Optional(str)
    subscriptionId: Optional(str)
    
class availabilitysetListModel(BaseModel):
    resourceGroupName: Optional(str)
    subscriptionId: Optional(str)
    
class availabilitysetListAvailableSizesParameters(BaseModel):
    availabilitySetName: str
    resourceGroupName: str
    subscriptionId: str
    
class availabilitysetListAvailableSizesResponse(BaseModel):
    name: Optional(str)