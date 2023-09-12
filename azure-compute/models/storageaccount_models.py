from pydantic import BaseModel,constr
from typing import Optional, List

class StorageAccountCreationParameters(BaseModel):
    storageAccountName: str
    subscriptionId: str
    resourceGroupName: str
    # vmName: str
    location: str
    kind: str = "StorageAccount" 
    # kind2:str = constr(regex=r^'("StorageAccount"|"test")$')
    sku: str

class StorageAccountResponseModel(BaseModel):
    name: Optional[str]
    id: Optional[str]
    type: Optional[str]

class StorageSkuParametes(BaseModel):
    subscriptionId: str
