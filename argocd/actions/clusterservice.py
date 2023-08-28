from ..models.clusterservice import *
from .. import action_store as action_store
from ..argo_wrapper import *


#Something probably wrong with this
@action_store.kubiya_action()
def list_clusters(input: ListClustersInput):
    return get_wrapper("/clusters", params = dict(input, by_alias = True))
