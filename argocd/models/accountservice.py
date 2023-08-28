from pydantic import BaseModel, Field
from typing import Optional, List, Union

#Inputs
class ListAccountsInput(BaseModel):
    pass

class GetAccounts(BaseModel):
    #name: str = Field(d    efault = "")
    name: str = "admin"

class CanI(BaseModel):
    resource: str
    action: str
    subresource: str

class UpdatePassword(BaseModel):
    currentPassword: str
    name: str
    newPassword: str

class CreateToken(BaseModel):
    name: str
    expiresIn: Optional[Union[str,int]] = "600"
    id: Optional[str]
    name: Optional[str] = "default"

class DeleteToken(BaseModel):
    name: str
    id: str

#Outputs

class accountToken(BaseModel):
    expiresAt: str
    id: str
    issuedAt: str

class accountAccount(BaseModel):
    name: str
    enabled: bool
    capabilities: List[str]
    tokens: Optional[List[accountToken]]
    
class accountAccountsList(BaseModel):
    items: List[accountAccount]

class accountCanIResponse(BaseModel):
    value: str

class accountCreateTokenResponse(BaseModel):
    token: str

