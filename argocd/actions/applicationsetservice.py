from ..models.applicationsetservice import *
from .. import action_store as action_store
from ..argo_wrapper import *

@action_store.kubiya_action()
def list_applicationset_applicationset(input: ListApplicationSetInput):
    return get_wrapper("/applicationsets")

@action_store.kubiya_action()
def get_applicationset_by_name(input: ListApplicationSetInput):
    return get_wrapper("/applicationsets/{input.name}")