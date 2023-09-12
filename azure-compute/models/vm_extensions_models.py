from pydantic import BaseModel
from typing import Optional, List


class ExtensionsGetParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    extensionName: str
    vmName: str

class ExtensionGetResponseModel(BaseModel):
    name: Optional[str]
    type: Optional[str]
    id: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    tags: Optional[dict]

class ExtensionsListParameters(BaseModel):
    subscriptionId: str
    resourceGroupName: str
    vmName: str

class ExtensionsListResponse(BaseModel):
    name: Optional[str]
    type: Optional[str]
    id: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    tags: Optional[dict]