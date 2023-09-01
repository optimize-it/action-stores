
from pydantic import BaseModel
from typing import Optional, List

class networkInterfaceCreationParameters(BaseModel):
    networkInterfaceName: str
    subscriptionId: str
    resourceGroupName: str
    vmName: str
    location: str
    
class networkInterfaceModel(BaseModel):
    id: Optional(str)
    type: Optional(str)
    name: Optional(str)
    location: Optional(str)
    tags: Optional[dict] = {}
    properties: dict
    
class networkInterfaceListParameters(BaseModel):
    subscribtionId: str
    
class networkInterfaceListModel(BaseModel):
    networkInterfaceName: str
    location: str
    id: str
    properties: dict
    tags: Optional[dict] = {}
    