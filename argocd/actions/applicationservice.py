from ..models.applicationservice import *
from .. import action_store as action_store
from ..argo_wrapper import *

@action_store.kubiya_action()
def list_applications(input: ListApplications):
    return get_wrapper("/applications")
    #return v1alpha1ApplicationList(**response)

@action_store.kubiya_action()
def get_application(input: GetApplicationInput):
    response = get_wrapper(f"/applications/{input.name}")
    return response['output']['status']['history']
    return GetApplicationOutput(
        destinationNamespace = response['output']['spec']['destination']['namespace'],
        server = response['output']['spec']['destination']['server'],
        project = response['output']['spec']['project'],
        sourcePath = response['output']['spec']['source']['path'],
        repoURL = response['output']['spec']['source']['repoURL'],
        targetRevision = response['output']['spec']['source']['targetRevision'],
        deploymentHistory = response['output']['status']['history']
    )


@action_store.kubiya_action()
def create_application(input: CreateApplicationInput):
    #return get_wrapper("/account")
    body = {
        "metadata": {
            "name": input.name,
            "namespace": input.namespace
        },
        "spec": {
            "source": {
                "repoURL": input.repoURL,
                "path": input.path,
                "targetRevision": input.targetRevision
            },
            "destination": {
                "server": input.destinationServer,
                "namespace": input.destinationNamespace
            },
            "project": input.project
        }
    }
    response = post_json_wrapper(f"/applications", params=body)
    return ApplicationDataResponse(**response)


@action_store.kubiya_action()
def update_application(input: UpdateApplicationInput):
    #return get_wrapper("/account")
    body = {
        "metadata": {
            "name": input.name,
            "namespace": input.namespace
        },
        "spec": {
            "source": {
                "repoURL": input.repoURL,
                "path": input.path,
                "targetRevision": input.targetRevision
            },
            "destination": {
                "server": input.destinationServer,
                "namespace": input.destinationNamespace
            },
            "project": input.project
        }
    }
    return put_json_wrapper(f"/applications/{input.name}", params=body)


@action_store.kubiya_action()
def get_manifests_with_files(input: GetManifestsWithFiles):
    return get_wrapper("/applications/manifestsWithFiles")
    #return repositoryManifestResponse(**response)

@action_store.kubiya_action()
def delete_application(input: DeleteApplicationInput):
    return delete_wrapper(f"/applications/{input.name}")

@action_store.kubiya_action()
def patch_application(input: PatchApplicationInput): 
    return patch_wrapper(f"/applications/{input.name}") 

@action_store.kubiya_action()
def get_application_manifests(input: GetManifestsInput):
    return get_wrapper(f"/applications/{input.name}/manifests")

@action_store.kubiya_action()
def terminate_operation(input: TerminateOperationInput):
    body = {
        "appNamespace": input.appNamespace,
        "project": input.project
    }
    return delete_json_wrapper(f"/applications/{input.name}/rollback", params = body)

@action_store.kubiya_action()
def pod_logs_for_app(input: PodLogsInput):
    return get_wrapper_logs(f"/applications/{input.applicationName}/logs")

@action_store.kubiya_action()
def get_resource(input: GetResourceInput):
    return get_wrapper(f"/applications/{input.name}/resource")

@action_store.kubiya_action()
def sync_app(input: ApplicationSyncRequestName):
    response = post_wrapper(f"/applications/{input.name}/sync")
    return response

@action_store.kubiya_action()
def rollback_app(input: RollbackAppInput):
    body = {
        "id": input.id,
        "prune": input.prune
    }
    return post_json_wrapper(f"/applications/{input.name}/rollback", params= body)

# @action_store.kubiya_action()
# def run_resource_action(input: RunResourceActionInput):
#     return post_wrapper(f"/applications/{input.name}/resource/actions")