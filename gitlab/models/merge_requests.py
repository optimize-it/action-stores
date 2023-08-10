from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime

class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict

class ListMergeRequests(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    approved_by_ids: Optional[List[int]] = Field(None, description='Returns merge requests which have been approved by all the users with the given id. Maximum of 5. None returns merge requests with no approvals. Any returns merge requests with an approval.')
    approver_ids: Optional[List[int]] = Field(None, description='Returns merge requests which have specified all the users with the given id as individual approvers. None returns merge requests without approvers. Any returns merge requests with an approver.')
    approved: Optional[str] = Field(None, description='Filters merge requests by their approved status. yes returns only approved merge requests. no returns only non-approved merge requests.')
    assignee_id: Optional[int] = Field(None, description='Returns merge requests assigned to the given user id. None returns unassigned merge requests. Any returns merge requests with an assignee.')
    author_id: Optional[int] = Field(None, description='Returns merge requests created by the given user id. Mutually exclusive with author_username. Combine with scope=all or scope=assigned_to_me.')
    author_username: Optional[str] = Field(None, description='Returns merge requests created by the given username. Mutually exclusive with author_id.')
    created_after: Optional[datetime] = Field(None, description='Returns merge requests created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    created_before: Optional[datetime] = Field(None, description='Returns merge requests created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    deployed_after: Optional[datetime] = Field(None, description='Returns merge requests deployed after the given date/time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    deployed_before: Optional[datetime] = Field(None, description='Returns merge requests deployed before the given date/time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    environment: Optional[str] = Field(None, description='Returns merge requests deployed to the given environment.')
    in_: Optional[str] = Field(None, description='Modify the scope of the search attribute. title, description, or a string joining them with comma. Default is title,description.', alias='in')
    labels: Optional[str] = Field(None, description='Returns merge requests matching a comma-separated list of labels. None lists all merge requests with no labels. Any lists all merge requests with at least one label. Predefined names are case-insensitive.')
    milestone: Optional[str] = Field(None, description='Returns merge requests for a specific milestone. None returns merge requests with no milestone. Any returns merge requests that have an assigned milestone.')
    my_reaction_emoji: Optional[str] = Field(None, description='Returns merge requests reacted by the authenticated user by the given emoji. None returns issues not given a reaction. Any returns issues given at least one reaction.')
    not_: Optional[str] = Field(None, description='Returns merge requests that do not match the parameters supplied. Accepts: labels, milestone, author_id, author_username, assignee_id, assignee_username, reviewer_id, reviewer_username, my_reaction_emoji.', alias='not')
    order_by: Optional[str] = Field(None, description='Returns requests ordered by created_at, title, or updated_at fields. Default is created_at.')
    reviewer_id: Optional[int] = Field(None, description='Returns merge requests which have the user as a reviewer with the given user id. None returns merge requests with no reviewers. Any returns merge requests with any reviewer. Mutually exclusive with reviewer_username.')
    reviewer_username: Optional[str] = Field(None, description='Returns merge requests which have the user as a reviewer with the given username. None returns merge requests with no reviewers. Any returns merge requests with any reviewer. Mutually exclusive with reviewer_id.')
    scope: Optional[str] = Field(None, description='Returns merge requests for the given scope: created_by_me, assigned_to_me or all. Defaults to created_by_me.')
    search: Optional[str] = Field(None, description='Search merge requests against their title and description.')
    sort: Optional[str] = Field(None, description='Returns requests sorted in asc or desc order. Default is desc.')
    source_branch: Optional[str] = Field(None, description='Returns merge requests with the given source branch.')
    state: Optional[str] = Field(None, description='Returns all merge requests or just those that are opened, closed, locked, or merged.')
    target_branch: Optional[str] = Field(None, description='Returns merge requests with the given target branch.')
    updated_after: Optional[datetime] = Field(None, description='Returns merge requests updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    updated_before: Optional[datetime] = Field(None, description='Returns merge requests updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    view: Optional[str] = Field(None, description='If simple, returns the iid, URL, title, description, and basic state of merge request.')
    with_labels_details: Optional[bool] = Field(None, description='If true, response returns more details for each label in labels field: :name, :color, :description, :description_html, :text_color. Default is false.')
    with_merge_status_recheck: Optional[bool] = Field(None, description='If true, this projection requests (but does not guarantee) that the merge_status field be recalculated asynchronously. Default is false.')
    wip: Optional[str] = Field(None, description='Filter merge requests against their wip status. yes to return only draft merge requests, no to return non-draft merge requests.')
class ListProjectMergeRequests(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    approved_by_ids: Optional[List[int]] = Field(None, description='Returns merge requests which have been approved by all the users with the given id. Maximum of 5. None returns merge requests with no approvals. Any returns merge requests with an approval.')
    approver_ids: Optional[List[int]] = Field(None, description='Returns merge requests which have specified all the users with the given id as individual approvers. None returns merge requests without approvers. Any returns merge requests with an approver.')
    approved: Optional[str] = Field(None, description='Filters merge requests by their approved status. yes returns only approved merge requests. no returns only non-approved merge requests.')
    assignee_id: Optional[int] = Field(None, description='Returns merge requests assigned to the given user id. None returns unassigned merge requests. Any returns merge requests with an assignee.')
    author_id: Optional[int] = Field(None, description='Returns merge requests created by the given user id. Mutually exclusive with author_username.')
    author_username: Optional[str] = Field(None, description='Returns merge requests created by the given username. Mutually exclusive with author_id.')
    created_after: Optional[datetime] = Field(None, description='Returns merge requests created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    created_before: Optional[datetime] = Field(None, description='Returns merge requests created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    environment: Optional[str] = Field(None, description='Returns merge requests deployed to the given environment.')
    iids: Optional[List[int]] = Field(None, description='Returns the request having the given iid.')
    labels: Optional[str] = Field(None, description='Returns merge requests matching a comma-separated list of labels. None lists all merge requests with no labels. Any lists all merge requests with at least one label. Predefined names are case-insensitive.')
    milestone: Optional[str] = Field(None, description='Returns merge requests for a specific milestone. None returns merge requests with no milestone. Any returns merge requests that have an assigned milestone.')
    my_reaction_emoji: Optional[str] = Field(None, description='Returns merge requests reacted by the authenticated user by the given emoji. None returns issues not given a reaction. Any returns issues given at least one reaction.')
    not_: Optional[str] = Field(None, description='Returns merge requests that do not match the parameters supplied. Accepts: labels, milestone, author_id, author_username, assignee_id, assignee_username, reviewer_id, reviewer_username, my_reaction_emoji.', alias='not')
    order_by: Optional[str] = Field(None, description='Returns requests ordered by created_at, title, or updated_at fields. Default is created_at.')
    reviewer_id: Optional[int] = Field(None, description='Returns merge requests which have the user as a reviewer with the given user id. None returns merge requests with no reviewers. Any returns merge requests with any reviewer. Mutually exclusive with reviewer_username.')
    reviewer_username: Optional[str] = Field(None, description='Returns merge requests which have the user as a reviewer with the given username. None returns merge requests with no reviewers. Any returns merge requests with any reviewer. Mutually exclusive with reviewer_id.')
    scope: Optional[str] = Field(None, description='Returns merge requests for the given scope: created_by_me, assigned_to_me, or all.')
    search: Optional[str] = Field(None, description='Search merge requests against their title and description.')
    sort: Optional[str] = Field(None, description='Returns requests sorted in asc or desc order. Default is desc.')
    source_branch: Optional[str] = Field(None, description='Returns merge requests with the given source branch.')
    state: Optional[str] = Field(None, description='Returns all merge requests or just those that are opened, closed, locked, or merged.')
    target_branch: Optional[str] = Field(None, description='Returns merge requests with the given target branch.')
    updated_after: Optional[datetime] = Field(None, description='Returns merge requests updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    updated_before: Optional[datetime] = Field(None, description='Returns merge requests updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    view: Optional[str] = Field(None, description='If simple, returns the iid, URL, title, description, and basic state of merge request.')
    wip: Optional[str] = Field(None, description='Filter merge requests against their wip status. yes to return only draft merge requests, no to return non-draft merge requests.')
    with_labels_details: Optional[bool] = Field(None, description='If true, response returns more details for each label in labels field: :name, :color, :description, :description_html, :text_color. Default is false.')
    with_merge_status_recheck: Optional[bool] = Field(None, description='If true, this projection requests (but does not guarantee) that the merge_status field be recalculated asynchronously. Default is false.')
class ListGroupMergeRequests(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the group owned by the authenticated user.')
    approved_by_ids: Optional[List[int]] = Field(None, description='Returns merge requests which have been approved by all the users with the given id. Maximum of 5. None returns merge requests with no approvals. Any returns merge requests with an approval.')
    approved_by_usernames: Optional[List[str]] = Field(None, description='Returns merge requests which have been approved by all the users with the given username. Maximum of 5. None returns merge requests with no approvals. Any returns merge requests with an approval.')
    approver_ids: Optional[List[int]] = Field(None, description='Returns merge requests which have specified all the users with the given id as individual approvers. None returns merge requests without approvers. Any returns merge requests with an approver.')
    approved: Optional[str] = Field(None, description='Filters merge requests by their approved status. yes returns only approved merge requests. no returns only non-approved merge requests.')
    assignee_id: Optional[int] = Field(None, description='Returns merge requests assigned to the given user id. None returns unassigned merge requests. Any returns merge requests with an assignee.')
    author_id: Optional[int] = Field(None, description='Returns merge requests created by the given user id. Mutually exclusive with author_username.')
    author_username: Optional[str] = Field(None, description='Returns merge requests created by the given username. Mutually exclusive with author_id.')
    created_after: Optional[datetime] = Field(None, description='Returns merge requests created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    created_before: Optional[datetime] = Field(None, description='Returns merge requests created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    labels: Optional[str] = Field(None, description='Returns merge requests matching a comma-separated list of labels. None lists all merge requests with no labels. Any lists all merge requests with at least one label. Predefined names are case-insensitive.')
    milestone: Optional[str] = Field(None, description='Returns merge requests for a specific milestone. None returns merge requests with no milestone. Any returns merge requests that have an assigned milestone.')
    my_reaction_emoji: Optional[str] = Field(None, description='Returns merge requests reacted by the authenticated user by the given emoji. None returns issues not given a reaction. Any returns issues given at least one reaction.')
    non_archived: Optional[bool] = Field(None, description='Returns merge requests from non archived projects only. Default is true.')
    not_: Optional[str] = Field(None, description='Returns merge requests that do not match the parameters supplied. Accepts: labels, milestone, author_id, author_username, assignee_id, assignee_username, reviewer_id, reviewer_username, my_reaction_emoji.', alias='not')
    order_by: Optional[str] = Field(None, description='Returns requests ordered by created_at, title, or updated_at fields. Default is created_at.')
    reviewer_id: Optional[int] = Field(None, description='Returns merge requests which have the user as a reviewer with the given user id. None returns merge requests with no reviewers. Any returns merge requests with any reviewer. Mutually exclusive with reviewer_username.')
    reviewer_username: Optional[str] = Field(None, description='Returns merge requests which have the user as a reviewer with the given username. None returns merge requests with no reviewers. Any returns merge requests with any reviewer. Mutually exclusive with reviewer_id.')
    scope: Optional[str] = Field(None, description='Returns merge requests for the given scope: created_by_me, assigned_to_me, or all.')
    search: Optional[str] = Field(None, description='Search merge requests against their title and description.')
    source_branch: Optional[str] = Field(None, description='Returns merge requests with the given source branch.')
    sort: Optional[str] = Field(None, description='Returns merge requests sorted in asc or desc order. Default is desc.')
    state: Optional[str] = Field(None, description='Returns all merge requests or just those that are opened, closed, locked, or merged.')
    target_branch: Optional[str] = Field(None, description='Returns merge requests with the given target branch.')
    updated_after: Optional[datetime] = Field(None, description='Returns merge requests updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    updated_before: Optional[datetime] = Field(None, description='Returns merge requests updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).')
    view: Optional[str] = Field(None, description='If simple, returns the iid, URL, title, description, and basic state of merge request.')
    with_labels_details: Optional[bool] = Field(None, description='If true, response returns more details for each label in labels field: :name, :color, :description, :description_html, :text_color. Default is false.')
    with_merge_status_recheck: Optional[bool] = Field(None, description='If true, this projection requests (but does not guarantee) that the merge_status field be recalculated asynchronously. Default is false.')
class GetSingleMR(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
    include_diverged_commits_count: Optional[bool] = Field(None, description='If true, response includes the commits behind the target branch.')
    include_rebase_in_progress: Optional[bool] = Field(None, description='If true, response includes whether a rebase operation is in progress.')
    render_html: Optional[bool] = Field(None, description='If true, response includes rendered HTML for title and description.')
class GetMergeRequestParticipants(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class GetMergeRequestCommits(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class GetMergeRequestChanges(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
    access_raw_diffs: Optional[bool] = Field(None, description='Retrieve change diffs via Gitaly.')
class ListMergeRequestDiffs(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
    page: Optional[int] = Field(None, description='The page of results to return.')
    per_page: Optional[int] = Field(None, description='The number of results per page.')
class ListMergeRequestPipelines(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class CreateMergeRequestPipeline(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description='Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description='The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description='Allow users who can merge to the target branch to push to the source branch.')
    assignee_id: Optional[int] = Field(None, description='The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description='The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description='The description of merge request.')
    labels: Optional[str] = Field(None, description='Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description='The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description='Flag indicating if a merge request should remove the source branch when merging.')
    reviewer_ids: Optional[List[int]] = Field(None, description='The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description='Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description='Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description='The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.')
class UpdateMergeRequest(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
    add_labels: Optional[str] = Field(None, description='Comma-separated label names to add to a merge request.')
    allow_collaboration: Optional[bool] = Field(None, description='Allow commits from members who can merge to the target branch.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description='Alias of allow_collaboration.')
    assignee_id: Optional[int] = Field(None, description='The ID of the user to assign the merge request to.')
    assignee_ids: Optional[List[int]] = Field(None, description='The ID of the users to assign the merge request to.')
    description: Optional[str] = Field(None, description='Description of the merge request.')
    discussion_locked: Optional[bool] = Field(None, description='Flag indicating if the merge request’s discussion is locked.')
    labels: Optional[str] = Field(None, description='Comma-separated label names for a merge request.')
    milestone_id: Optional[int] = Field(None, description='The global ID of a milestone to assign the merge request to.')
    remove_labels: Optional[str] = Field(None, description='Comma-separated label names to remove from a merge request.')
    remove_source_branch: Optional[bool] = Field(None, description='Flag indicating if a merge request should remove the source branch when merging.')
    reviewer_ids: Optional[List[int]] = Field(None, description='The ID of the users set as a reviewer to the merge request.')
    squash: Optional[bool] = Field(None, description='If true, the commits are squashed into a single commit on merge.')
    squash_on_merge: Optional[bool] = Field(None, description='Indicates if the merge request will be squashed when merged.')
    state_event: Optional[str] = Field(None, description='New state (close/reopen).')
    target_branch: Optional[str] = Field(None, description='The target branch.')
    title: Optional[str] = Field(None, description='Title of MR.')
class DeleteMergeRequest(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class MergeMergeRequest(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
    merge_commit_message: Optional[str] = Field(None, description='Custom merge commit message.')
    merge_when_pipeline_succeeds: Optional[bool] = Field(None, description='If true, the merge request is merged when the pipeline succeeds.')
    sha: Optional[str] = Field(None, description='If present, then this SHA must match the HEAD of the source branch, otherwise the merge fails.')
    should_remove_source_branch: Optional[bool] = Field(None, description='If true, removes the source branch.')
    squash_commit_message: Optional[str] = Field(None, description='Custom squash commit message.')
    squash: Optional[bool] = Field(None, description='If true, the commits are squashed into a single commit on merge.')
class MergeToDefaultMergeRefPath(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class CancelMergeWhenPipelineSucceeds(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class RebaseMergeRequest(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
    skip_ci: Optional[bool] = Field(None, description='Set to true to skip creating a CI pipeline.')
class ListIssuesThatCloseOnMerge(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(..., description='The internal ID of the merge request.')
class SubscribeMergeRequest(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(description='The internal ID of the merge request.')
class UnsubscribeMergeRequest(SubscribeMergeRequest):
    pass
class CreateTodoItem(SubscribeMergeRequest):
    pass
class GetMergeRequestDiffVersions(SubscribeMergeRequest):
    pass
class GetSingleMergeRequestDiffVersion(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(description='The internal ID of the merge request.')
    version_id: int = Field(description='The ID of the merge request diff version.')
class SetTimeEstimateMergeRequest(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    merge_request_iid: int = Field(description='The internal ID of the merge request.')
    duration: str = Field(description='The duration in human format, such as 3h30m.')
class ResetTimeEstimateMergeRequest(SubscribeMergeRequest):
    pass
class AddSpentTimeMergeRequest(SetTimeEstimateMergeRequest):
    summary: Optional[str] = Field(None, description='A summary of how the time was spent.')
class ResetSpentTimeMergeRequest(SubscribeMergeRequest):
    pass
class GetTimeTrackingStatsMergeRequest(SubscribeMergeRequest):
    pass