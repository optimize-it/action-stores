from argparse import OPTIONAL
from pydantic import BaseModel
from typing import Optional, List

class ImageCreationParameters(BaseModel):
    imageName: str
    subscriptionId: str
    resourceGroupName: str
    vmName: str
    location: str
    
class ImageModel(BaseModel):
    id: Optional[str]
    type: Optional[str]
    name: Optional[str]
    location: Optional[str]
    tags: Optional[dict] = {}
    properties: dict
    
class ImageListParameters(BaseModel):
    subscribtionId: str
    
class ImageListModel(BaseModel):
    imageName: str
    location: str
    id: str
    properties: dict
    tags: Optional[dict] = {}
    
class ImageDeletetionParameters(BaseModel):
    imageName: str
    subscriptionId: str
    resourceGroupName: str