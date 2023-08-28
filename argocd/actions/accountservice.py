from ..models.accountservice import *
from .. import action_store as action_store
from ..argo_wrapper import *

@action_store.kubiya_action()
def list_accounts(input: ListAccountsInput):
    #return get_wrapper("/account")
    response = get_wrapper("/account")
    return accountAccountsList(**response)

@action_store.kubiya_action()
def can_i(input: CanI):
    response = get_wrapper(f"/account/can-i/{input.resource}/{input.action}/{input.subresource}")
    return accountCanIResponse(**response)

@action_store.kubiya_action()
def update_password(input: UpdatePassword):
    params = input.dict(exclude_none=True)
    return put_wrapper(f"/account/password", params = params)

@action_store.kubiya_action()
def get_accounts(input: GetAccounts):
    response = get_wrapper(f"/account/{input.name}")
    return accountAccount(**response)

@action_store.kubiya_action()
def create_token(input: CreateToken):
    response = post_wrapper(f"/account/{input.name}/token")
    return accountCreateTokenResponse(**response)

@action_store.kubiya_action()
def delete_token(input: DeleteToken):
    return delete_wrapper(f"/account/{input.name}/token{input.id}")