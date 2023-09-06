import logging

from .. import action_store as action_store
from ..azure_wrapper import *
# from ..models.vms_models import *
from ..models.snapshot_models import *
from typing import Union

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def create_or_update_azure_snapshots(params: SnapshotCreationParameters) -> Union[SnapshotResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        snapshots_data = {
                            "location": params.location,
                            "properties": {
                                "creationData": {
                                "createOption": "CopyStart",
                                "sourceResourceId": f"subscriptons/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{params.diskName}"
                                }
                            }
                            }
        endpoint = f"/subscriptons/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{params.snapshotName}"
        api_version = ""
        response_data = put_wrapper(endpoint, subscriptionId, api_version, data=snapshots_data)
        return SnapshotResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to create snapshot : {e}")
        raise

@action_store.kubiya_action()
def get_azure_snapshots(params: SnapshotGetParameters) -> Union[SnapshotGetResponseModel, dict]:
    try:
        subscriptionId = params.subscriptionId
        resourceGroupName = params.resourceGroupName
        # snapshotsName = params.snapshotsName
        endpoint = f"/subscriptons/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{params.snapshotName}"
        api_version = "2021-12-01"

        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)

        return SnapshotGetResponseModel(**response_data)
    except Exception as e:
        logger.error(f"Failed to get snapshot : {e}")
        raise

@action_store.kubiya_action()
def listall_azure_snapshots(params: SnapshotListParameters) -> List[SnapshotListModel]:
    try:
    #subscriptionId = params.subscriptionId
        endpoint = f"/subscriptons/{params.subscriptionId}/providers/Microsoft.Compute/snapshots"
        api_version = "2022-11-01"
        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
        snapshots_list = response_data.get('value', [])
        return [SnapshotListModel(**snapshots) for snapshots in snapshots_list]
    except Exception as e:
        logger.error(f"Failed to list all snapshots : {e}")
        raise

@action_store.kubiya_action()
def list_by_rg_azure_snapshots(params: SnapshotListByRGParameters) -> List[SnapshotListModel]:
    try:
        #subscriptionId = params.subscriptionId
        endpoint = f"/subscriptons/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/snapshots"
        api_version = "2022-11-01"
        response_data = get_wrapper(endpoint, params.subscriptionId, api_version)
        snapshots_list = response_data.get('value', [])
        return [SnapshotListModel(**snapshots) for snapshots in snapshots_list]
    except Exception as e:
        logger.error(f"Failed to list snapshot by RG : {e}")
        raise

@action_store.kubiya_action()
def delete_azure_snapshot(params: SnapshotDeleteParameters):
    try:
        endpoint = f"/subscriptons/{params.subscriptionId}/resourceGroups/{params.resourceGroupName}/providers/Microsoft.Compute/snapshots/{params.snapshotName}"
        api_version = "2022-11-01"
        response_data = delete_wrapper(endpoint, params.subscriptionId, api_version)
        return response_data
    except Exception as e:
        logger.error(f"Failed to delete snapshot : {e}")
        raise
    