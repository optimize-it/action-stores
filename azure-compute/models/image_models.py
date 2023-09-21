from argparse import OPTIONAL
from pydantic import BaseModel
from typing import Optional, List, Literal


Regions = Literal["eastus", "eastus2", "westus", "northeurope", "westindia", "southindia"]

class ImageCreationParameters(BaseModel):
    imageName: str
    
    resourceGroupName: str
    vmName: str
    location: Regions

class ImageGetParameters(BaseModel):
    imageName: str
    
    resourceGroupName: str
    
class ImageModel(BaseModel):
    id: Optional[str]
    type: Optional[str]
    name: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: Optional[dict]
    
class ImageListParameters(BaseModel):
    None
    
class ImageListModel(BaseModel):
    imageName: str
    location: str
    id: str
    properties: dict
    tags: Optional[dict] = {}
    
class ImageDeletetionParameters(BaseModel):
    imageName: str
    
    resourceGroupName: str