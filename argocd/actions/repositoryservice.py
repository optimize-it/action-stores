from ..models.repositoryservice import *
from .. import action_store as action_store
from ..argo_wrapper import *

@action_store.kubiya_action()
def list_repositories(input: ListRepositories):
    return get_wrapper("/repositories")

    