import logging
from github import GithubException
from .. import action_store as action_store
from ..github_wrapper import get_github_instance, get_entity
from time import sleep
from ..models.workflow import (
    ListWorkflowRunsParams, ListWorkflowRunsResponse,
    TriggerWorkflowParams, TriggerWorkflowResponse,
    GetWorkflowRunParams, GetWorkflowRunResponse,
    CancelWorkflowRunParams, CancelWorkflowRunResponse,
    TrackWorkflowRunParams, TrackWorkflowRunResponse,
    ListWorkflowFilesParams, ListWorkflowFilesResponse,
    GetWorkflowFileParams, GetWorkflowFileResponse, ListWorkflowJobRunsParams, ListWorkflowJobRunsResponse,
    WorkflowFileModel, WorkflowRunModel, WorkflowJobRunModel,
    GetWorkflowJobRunParams, GetWorkflowJobRunResponse,
    ListWorkflowPullRequestsParams, ListWorkflowPullRequestsResponse,
    DownloadWorkflowArtifactParams, DownloadWorkflowArtifactResponse,
    WorkflowPullRequestModel


)

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def list_workflow_runs(params: ListWorkflowRunsParams) -> ListWorkflowRunsResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)

        workflow_runs = []
        for workflow_run in repo.get_workflow_runs():
            workflow_run_model = WorkflowRunModel(
                id=workflow_run.id,
                workflow_name=workflow_run.name,
                created_at=str(workflow_run.created_at),
                updated_at=str(workflow_run.updated_at),
                status=workflow_run.status,
                conclusion=workflow_run.conclusion
            )
            workflow_runs.append(workflow_run_model)

        return ListWorkflowRunsResponse(workflow_runs=workflow_runs)
    except GithubException as e:
        logger.error(f"Failed to list workflow runs: {e}")
        raise

@action_store.kubiya_action()
def trigger_workflow(params: TriggerWorkflowParams) -> TriggerWorkflowResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        workflow = repo.get_workflow(params.workflow_id)
        # https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch
        workflow_run = workflow.create_dispatch(ref=params.branch)

        if workflow_run:
            return TriggerWorkflowResponse(success=True)
    except GithubException as e:
        logger.error(f"Failed to trigger workflow: {e}")
        raise

@action_store.kubiya_action()
def get_workflow_run(params: GetWorkflowRunParams) -> GetWorkflowRunResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        workflow_run = repo.get_workflow_run(params.workflow_run_id)
        return GetWorkflowRunResponse(
            workflow_run_id=workflow_run.id,
            workflow_run_url=workflow_run.html_url,
            status=workflow_run.status,
            conclusion=workflow_run.conclusion
        )
    except GithubException as e:
        logger.error(f"Failed to get workflow run details: {e}")
        raise

# @action_store.kubiya_action()
def cancel_workflow_run(params: CancelWorkflowRunParams) -> CancelWorkflowRunResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        workflow_run = repo.get_workflow_run(params.workflow_run_id)
        workflow_run.cancel()
        return CancelWorkflowRunResponse(message="Workflow run canceled successfully.")
    except GithubException as e:
        logger.error(f"Failed to cancel workflow run: {e}")
        raise

# @action_store.kubiya_action()
def track_workflow_run(params: TrackWorkflowRunParams) -> TrackWorkflowRunResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)

        while True:
            workflow_run = repo.get_workflow_run(params.workflow_run_id)
            if workflow_run.status != "in_progress":
                break
            sleep(params.polling_interval)

        return TrackWorkflowRunResponse(
            workflow_run_id=workflow_run.id,
            workflow_run_url=workflow_run.html_url,
            status=workflow_run.status,
            conclusion=workflow_run.conclusion,
            is_completed=True
        )
    except GithubException as e:
        logger.error(f"Failed to track workflow run: {e}")
        raise

# @action_store.kubiya_action()
# def list_workflow_files(params: ListWorkflowFilesParams) -> ListWorkflowFilesResponse:
#     try:
#         github = get_github_instance()
#         entity = get_entity(github)
#         repo = entity.get_repo(params.repo_name)
#
#         workflow_files = []
#         for workflow_file in repo.get_workflow_files():
#             workflow_file_model = WorkflowFileModel(
#                 path=workflow_file.path,
#                 size=workflow_file.size,
#                 url=workflow_file.url
#             )
#             workflow_files.append(workflow_file_model)
#
#         return ListWorkflowFilesResponse(workflow_files=workflow_files)
#     except GithubException as e:
#         logger.error(f"Failed to list workflow files: {e}")
#         raise
#
# @action_store.kubiya_action()
# def get_workflow_file(params: GetWorkflowFileParams) -> GetWorkflowFileResponse:
#     try:
#         github = get_github_instance()
#         entity = get_entity(github)
#         repo = entity.get_repo(params.repo_name)
#         workflow_file = repo.get_workflow_file(params.file_path)
#         return GetWorkflowFileResponse(
#             path=workflow_file.path,
#             size=workflow_file.size,
#             url=workflow_file.url,
#             content=workflow_file.content
#         )
#     except GithubException as e:
#         logger.error(f"Failed to get workflow file: {e}")
#         raise

@action_store.kubiya_action()
def list_workflow_job_runs(params: ListWorkflowJobRunsParams) -> ListWorkflowJobRunsResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        workflow_run = repo.get_workflow_run(params.workflow_run_id)

        job_runs = []
        for job in workflow_run.jobs():
            job_run_model = WorkflowJobRunModel(
                id=job.id,
                name=job.name,
                status=job.status,
                conclusion=job.conclusion
            )
            job_runs.append(job_run_model)

        return ListWorkflowJobRunsResponse(job_runs=job_runs)
    except GithubException as e:
        logger.error(f"Failed to list workflow job runs: {e}")
        raise

# @action_store.kubiya_action()
def get_workflow_job_run(params: GetWorkflowJobRunParams) -> GetWorkflowJobRunResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        workflow_run = repo.get_workflow_run(params.workflow_run_id)
        job = workflow_run.get_job(params.job_id)

        return GetWorkflowJobRunResponse(
            job_run_id=job.id,
            job_name=job.name,
            status=job.status,
            conclusion=job.conclusion
        )
    except GithubException as e:
        logger.error(f"Failed to get workflow job run details: {e}")
        raise

# @action_store.kubiya_action()
def download_workflow_artifact(params: DownloadWorkflowArtifactParams) -> DownloadWorkflowArtifactResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        workflow_run = repo.get_workflow_run(params.workflow_run_id)
        artifact = workflow_run.get_artifact(params.artifact_name)
        download_url = artifact.archive_download_url

        return DownloadWorkflowArtifactResponse(download_url=download_url)
    except GithubException as e:
        logger.error(f"Failed to download workflow artifact: {e}")
        raise

# @action_store.kubiya_action()
def list_workflow_pull_requests(params: ListWorkflowPullRequestsParams) -> ListWorkflowPullRequestsResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        workflow_run = repo.get_workflow_run(params.workflow_run_id)

        pull_requests = []
        for pr in workflow_run.get_pull_requests():
            pull_request_model = WorkflowPullRequestModel(
                number=pr.number,
                title=pr.title,
                url=pr.html_url,
                state=pr.state,
                head_branch=pr.head.ref,
                base_branch=pr.base.ref
            )
            pull_requests.append(pull_request_model)

        return ListWorkflowPullRequestsResponse(pull_requests=pull_requests)
    except GithubException as e:
        logger.error(f"Failed to list workflow pull requests: {e}")
        raise