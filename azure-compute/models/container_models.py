from pydantic import BaseModel
from typing import Optional, List


class ContainerListParameters(BaseModel):
    storageAccountName: str
    
    resourceGroupName: str

    
class ContainerResponseModel(BaseModel):
    id: Optional[str]
    type: Optional[str]
    etag: Optional[str]
    name: Optional[str]
    properties: Optional[dict]

class ContainerCreateParameters(BaseModel):
    
    resourceGroupName: str
    storageAccountName: str
    containerName: str

class ContainerCreateResponseModel(BaseModel):
    id: Optional[str]
    name: Optional[str]
    type: Optional[str]
    properties: Optional[dict]

class SetContainerPropertiesParameters(BaseModel):
    storageAccountName: str
    blobName: str
    resourceGroupName: str

class GetContainerPropertiesParameters(BaseModel):
    storageAccountName: str
    BlobServicesName: str
    
    resourceGroupName: str

class GetContainerPropertiesResponseModel(BaseModel):
    id: Optional[str]
    name: Optional[str]    
    type: Optional[str]
    properties: Optional[dict]
    sku: Optional[dict]

class GetBlobParameters(BaseModel):
    storageAccountName: str
    containerName: str
    blobName: str

class DeleteContainerParams(BaseModel):
    storageAccountName: str
    containerName: str
    resourceGroupName: str

class GetContainerAcl(BaseModel):
    storageAccountName: str
    containerName: str
    resourceGroupName: str