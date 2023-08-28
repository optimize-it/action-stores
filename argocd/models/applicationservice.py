from pydantic import BaseModel, Field
from typing import Optional, List, Any
import json

# List Applications

class ListApplications(BaseModel):
    name: Optional[str] = ""
    refresh: Optional[str] = ""
    projects: Optional[List[str]] = []
    resourceVersion: Optional[str] = ""
    selector: Optional[str] = ""
    repo: Optional[str] = ""
    appNamespace: Optional[str] = ""
    project: Optional[List[str]] = []

class v1alpha1ApplicationList(BaseModel):
    items: List[dict]
    metadata: dict

# Create Application

# Sync Application

# ApplicationSyncRequest Model
class ApplicationSyncRequest(BaseModel):
    name: str = "_replace_with_app_name_"
    # appNamespace: Optional[str] = "_replace_with_app_namespace_"
    # dryRun: Optional[bool] = False
    # infos_name: Optional[str] = "_replace_with_info_name_"
    # infos_value: Optional[str] = "_replace_with_info_value_"
    # manifests: Optional[List[str]] = ["_replace_with_manifests_"]
    # project: Optional[str] = "_replace_with_project_"
    # prune: Optional[bool] = False 
    # resource_group: Optional[str] = "_replace_with_resource_group_"
    # resource_kind: Optional[str] = "_replace_with_resource_kind_"
    # resource_name: Optional[str] = "_replace_with_resource_name_"
    # resource_namespace: Optional[str] = "_replace_with_resource_namespace_"
    # retry_backoff_duration: Optional[str] = "1m"
    # retry_backoff_factor: Optional[int] = 2
    # retry_backoff_maxDuration: Optional[str] = "5m"
    # retry_limit: Optional[int] = 3
    # revision: Optional[str] = "HEAD"
    # strategy_force: Optional[bool] = False
    # strategy_hook: Optional[bool] = False
    # syncOptions: Optional[List[str]] = ["_replace_with_sync_options_"]

class ApplicationSyncRequestName(BaseModel):
    name: str = "_replace_with_app_name_"

# Create Application
class CreateApplicationInput(BaseModel):
    name: str
    namespace: str = "argocd"
    repoURL: str
    path: str
    targetRevision: str = "HEAD"
    destinationServer: str = "https://kubernetes.default.svc"
    destinationNamespace: str
    project: str = "default"

class Metadata(BaseModel):
    creationTimestamp: str
    name: str
    namespace: str
    resourceVersion: str
    uid: str

class Destination(BaseModel):
    namespace: str
    server: str

class Source(BaseModel):
    path: str
    repoURL: str
    targetRevision: str

class Sync(BaseModel):
    comparedTo: dict
    status: str

class Status(BaseModel):
    health: dict
    summary: dict
    sync: Sync

class ApplicationDataResponse(BaseModel):
    metadata: Metadata
    spec: dict  # Nested dictionary with 'destination', 'project', and 'source'
    status: Status

# Sync Response
class Conditions(BaseModel):
    lastTransitionTime: str
    message: str
    type: str

class Resources(BaseModel):
    kind: str
    name: str
    namespace: str
    status: str
    version: str
    health: Optional[dict]
    group: Optional[str]

class SyncStatus(BaseModel):
    comparedTo: dict
    revision: str
    status: str

class Status(BaseModel):
    conditions: List[Conditions]
    controllerNamespace: str
    health: dict
    reconciledAt: str
    resources: List[Resources]
    sourceType: str
    summary: dict
    sync: SyncStatus

class SyncResponse(BaseModel):
    metadata: Metadata  # Reuse the previous Metadata model
    operation: dict  # Nested dictionary with 'initiatedBy' and 'sync'
    spec: dict  # Nested dictionary with 'destination', 'project', and 'source'
    status: Status


# Update Application

class UpdateApplicationInput(BaseModel):
    name: str
    namespace: str = "argocd"
    repoURL: str
    path: str
    targetRevision: str = "HEAD"
    destinationServer: str = "https://kubernetes.default.svc"
    destinationNamespace: str
    project: str = "default"

# Get ManifestsWithFiles

class applicationFileChunk(BaseModel):
    chunk: Any

class applicationApplicationManifestQueryWithFiles(BaseModel):
    appNameSpace: Optional[str]
    checksum: Optional[str]
    name: Optional[str]
    project: Optional[str]
    
class GetManifestsWithFiles(BaseModel):
    chunk: applicationFileChunk
    query: applicationApplicationManifestQueryWithFiles

class repositoryManifestResponse(BaseModel):
    manifests: List[str]
    namespace: str
    revision: str
    server: str
    sourceType: str
    verifyResult: str

# Update Updates an application

class GetApplicationInput(BaseModel):
    name: str
    appNamespace: Optional[str]
    project: Optional[List[str]]

class GetApplicationOutput(BaseModel):
    destinationNamespace: str
    server: str
    project: str
    sourcePath: str
    repoURL: str
    targetRevision: str
    deploymentHistory: List[dict]

# Delete Deletes an application

class DeleteApplicationInput(BaseModel):
    name: str
    cascade: Optional[bool] = ""
    propogationPolicy: Optional[str] = ""
    appNamespace: Optional[str]
    project: Optional[str] = "default"

# Patch patch an application

class PatchApplicationInput(BaseModel):
    name: str
    appNamespace: Optional[str]
    patch: Optional[str]
    patchType: Optional[str]
    project: Optional[str]

class PatchApplicationOutput(BaseModel):
    app: dict

# GetManifests returns application manifests

class GetManifestsInput(BaseModel):
    name: str
    revision: Optional[str]
    appNamespace: Optional[str]
    project: Optional[str]

# TerminateOperation terminates the currently running operation

class TerminateOperationInput(BaseModel):
    name: str
    appNamespace: Optional[str]
    project: Optional[str]
    
#PodLogs returns stream of log entries for the specified pod. Pod

class PodLogsInput(BaseModel):
    applicationName: str


#GetResource returns single application resource

class GetResourceInput(BaseModel):
    name: str
    resourceName: Optional[str] = ""
    version: Optional[str] = ""
    group: Optional[str] = ""
    kind: Optional[str]
    appNamespace: Optional[str] = ""
    project: Optional[str] = ""

# Rollback

class RollbackAppInput(BaseModel):
    name: str
    id: Optional[str] = "Get revision IDs through get_application"
    prune: Optional[bool] = False

# DeleteResource deletes a single application resource

class DeleteResourceInput(BaseModel):
    name: str
    namespace: Optional[str] = ""
    resourceName: Optional[str] = ""
    version: Optional[str] = ""
    group: Optional[str] = ""
    kind: Optional[str] = ""
    force: Optional[bool] = False
    orphan: Optional[bool] = False
    appNamespace: Optional[str] = ""
    project: Optional[str] = ""

# Run Resource Action

class RunResourceActionInput(BaseModel):
    name: str
    namespace: Optional[str] = ""
    resourceName: Optional[str] = ""
    version: Optional[str] = ""
    group: Optional[str] = ""
    kind: Optional[str] = ""
    appNamespace: Optional[str] = ""
    project: Optional[str] = ""

# Terminate Operation

class RunResourceActionInput(BaseModel):
    name: str
    namespace: Optional[str] = ""
    resourceName: Optional[str] = ""
    version: Optional[str] = ""
    group: Optional[str] = ""
    kind: Optional[str] = ""
    appNamespace: Optional[str] = ""
    project: Optional[str] = ""
