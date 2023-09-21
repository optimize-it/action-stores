from pydantic import BaseModel,constr
from typing import Optional, List, Literal


Regions = Literal["eastus", "eastus2", "westus", "northeurope", "westindia", "southindia"]
class StorageAccountCreationParameters(BaseModel):
    storageAccountName: str
    
    resourceGroupName: str
    # vmName: str
    location: Regions
    kind: str = "Storage" 
    # kind2:str = constr(regex=r^'("StorageAccount"|"test")$')
    sku: str = "Standard_LRS"

class StorageAccountResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    kind: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    sku: Optional[dict]
    tags: Optional[dict]
    extendedLocation: Optional[dict]


class StorageSkuParametes(BaseModel):
    None

class ListStorageParametes(BaseModel):
    None

class ListStorageResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]
    kind: Optional[str]
    location: Optional[str]
    properties: Optional[dict]
    sku: Optional[dict]
    tags: Optional[dict] = {}