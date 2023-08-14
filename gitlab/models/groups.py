from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime



# class Statistics(BaseModel):
#     storage_size: int
#     repository_siwe: int
#     wiki_size: int
#     lfs_objects_size: int
#     job_artifacts_size: int
#     pipeline_artifacts_size: int
#     packages_size: int
#     snippets_size: int
#     uploads_size: int


class Groups(BaseModel):
    groups: List[dict]

class Group(BaseModel):
    groups: dict


class Hooks(BaseModel):
    hooks: List[str]

class Hook(BaseModel):
    hook: str

class Rules(BaseModel):
    rules: List[Any]

# class Group(BaseModel):
#     id: int
#     name: str
#     path: str
#     description: str
#     visibility: str
#     share_with_group_lock: bool
#     require_two_factor_authentication: bool
#     two_factor_grace_period: int
#     project_creation_level: str
#     auto_devops_enabled: Optional[bool] = None
#     subgroup_creation_level: str
#     emails_disabled: Optional[bool] = None
#     mentions_disabled: Optional[bool] = None
#     lfs_enabled: bool
#     default_branch_protection: int
#     avatar_url: str
#     web_url: str
#     request_access_enabled: bool
#     full_name: str
#     full_path: str
#     file_template_project_id: int
#     parent_id: Optional[int] = None
#     created_at: str
#     statistics: Statistics
#     wiki_access_level: str

class GroupList(BaseModel):
    skip_groups: Optional[List[int]] = Field(None, description='Skip the group IDs passed')
    all_available: Optional[bool] = Field(None, description='Show all the groups you have access to')
    search: Optional[str] = Field(None, description='Return the list of authorized groups matching the search criteria')
    order_by: Optional[str] = Field(None, description='Order groups by name, path, id, or similarity')
    sort: Optional[str] = Field(None, description='Order groups in asc or desc order')
    statistics: Optional[bool] = Field(None, description='Include group statistics')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
    owned: Optional[bool] = Field(None, description='Limit to groups explicitly owned by the current user')
    min_access_level: Optional[int] = Field(None, description='Limit to groups where current user has at least this role (access_level)')
    top_level_only: Optional[bool] = Field(None, description='Limit to top level groups, excluding all subgroups')
class GroupSubgroupsList(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group of the immediate parent group')
    skip_groups: Optional[List[int]] = Field(None, description='Skip the group IDs passed')
    all_available: Optional[bool] = Field(None, description='Show all the groups you have access to')
    search: Optional[str] = Field(None, description='Return the list of authorized groups matching the search criteria')
    order_by: Optional[str] = Field(None, description='Order groups by name, path, or id')
    sort: Optional[str] = Field(None, description='Order groups in asc or desc order')
    statistics: Optional[bool] = Field(None, description='Include group statistics')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
    owned: Optional[bool] = Field(None, description='Limit to groups explicitly owned by the current user')
    min_access_level: Optional[int] = Field(None, description='Limit to groups where current user has at least this role (access_level)')
class GroupProjectsList(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    archived: Optional[bool] = Field(None, description='Limit by archived status')
    visibility: Optional[str] = Field(None, description='Limit by visibility public, internal, or private')
    order_by: Optional[str] = Field(None, description='Return projects ordered by id, name, path, created_at, updated_at, or last_activity_at fields')
    sort: Optional[str] = Field(None, description='Return projects sorted in asc or desc order')
    search: Optional[str] = Field(None, description='Return list of authorized projects matching the search criteria')
    simple: Optional[bool] = Field(None, description='Return only limited fields for each project')
    owned: Optional[bool] = Field(None, description='Limit by projects owned by the current user')
    starred: Optional[bool] = Field(None, description='Limit by projects starred by the current user')
    topic: Optional[str] = Field(None, description='Return projects matching the topic')
    with_issues_enabled: Optional[bool] = Field(None, description='Limit by projects with issues feature enabled')
    with_merge_requests_enabled: Optional[bool] = Field(None, description='Limit by projects with merge requests feature enabled')
    with_shared: Optional[bool] = Field(None, description='Include projects shared to this group')
    include_subgroups: Optional[bool] = Field(None, description='Include projects in subgroups of this group')
    min_access_level: Optional[int] = Field(None, description='Limit to projects where current user has at least this role (access_level)')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
    with_security_reports: Optional[bool] = Field(None, description='Return only projects that have security reports artifacts present in any of their builds')
class GroupList(BaseModel):
    skip_groups: Optional[List[int]] = Field(None, description='Skip the group IDs passed')
    all_available: Optional[bool] = Field(None, description='Show all the groups you have access to')
    search: Optional[str] = Field(None, description='Return the list of authorized groups matching the search criteria')
    order_by: Optional[str] = Field(None, description='Order groups by name, path, id, or similarity')
    sort: Optional[str] = Field(None, description='Order groups in asc or desc order')
    statistics: Optional[bool] = Field(None, description='Include group statistics')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
    owned: Optional[bool] = Field(None, description='Limit to groups explicitly owned by the current user')
    min_access_level: Optional[int] = Field(None, description='Limit to groups where current user has at least this role (access_level)')
    top_level_only: Optional[bool] = Field(None, description='Limit to top level groups, excluding all subgroups')
class GroupSubgroupsList(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group of the immediate parent group')
    skip_groups: Optional[List[int]] = Field(None, description='Skip the group IDs passed')
    all_available: Optional[bool] = Field(None, description='Show all the groups you have access to')
    search: Optional[str] = Field(None, description='Return the list of authorized groups matching the search criteria')
    order_by: Optional[str] = Field(None, description='Order groups by name, path, or id')
    sort: Optional[str] = Field(None, description='Order groups in asc or desc order')
    statistics: Optional[bool] = Field(None, description='Include group statistics')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
    owned: Optional[bool] = Field(None, description='Limit to groups explicitly owned by the current user')
    min_access_level: Optional[int] = Field(None, description='Limit to groups where current user has at least this role (access_level)')
class GroupProjectsList(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    archived: Optional[bool] = Field(None, description='Limit by archived status')
    visibility: Optional[str] = Field(None, description='Limit by visibility public, internal, or private')
    order_by: Optional[str] = Field(None, description='Return projects ordered by id, name, path, created_at, updated_at, or last_activity_at fields')
    sort: Optional[str] = Field(None, description='Return projects sorted in asc or desc order')
    search: Optional[str] = Field(None, description='Return list of authorized projects matching the search criteria')
    simple: Optional[bool] = Field(None, description='Return only limited fields for each project')
    owned: Optional[bool] = Field(None, description='Limit by projects owned by the current user')
    starred: Optional[bool] = Field(None, description='Limit by projects starred by the current user')
    topic: Optional[str] = Field(None, description='Return projects matching the topic')
    with_issues_enabled: Optional[bool] = Field(None, description='Limit by projects with issues feature enabled')
    with_merge_requests_enabled: Optional[bool] = Field(None, description='Limit by projects with merge requests feature enabled')
    with_shared: Optional[bool] = Field(None, description='Include projects shared to this group')
    include_subgroups: Optional[bool] = Field(None, description='Include projects in subgroups of this group')
    min_access_level: Optional[int] = Field(None, description='Limit to projects where current user has at least this role (access_level)')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
    with_security_reports: Optional[bool] = Field(None, description='Return only projects that have security reports artifacts present in any of their builds')
class GroupSharedProjectsList(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    archived: Optional[bool] = Field(None, description='Limit by archived status')
    visibility: Optional[str] = Field(None, description='Limit by visibility public, internal, or private')
    order_by: Optional[str] = Field(None, description='Return projects ordered by id, name, path, created_at, updated_at, or last_activity_at fields')
    sort: Optional[str] = Field(None, description='Return projects sorted in asc or desc order')
    search: Optional[str] = Field(None, description='Return list of authorized projects matching the search criteria')
    simple: Optional[bool] = Field(None, description='Return only limited fields for each project')
    starred: Optional[bool] = Field(None, description='Limit by projects starred by the current user')
    with_issues_enabled: Optional[bool] = Field(None, description='Limit by projects with issues feature enabled')
    with_merge_requests_enabled: Optional[bool] = Field(None, description='Limit by projects with merge requests feature enabled')
    min_access_level: Optional[int] = Field(None, description='Limit to projects where current user has at least this role (access_level)')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
class GroupDetails(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    with_custom_attributes: Optional[bool] = Field(None, description='Include custom attributes in response')
    with_projects: Optional[bool] = Field(True, description='Include details from projects that belong to the specified group')
class GroupAvatar(BaseModel):
    id: Union[int, str] = Field(description='ID of the group')
class NewGroup(BaseModel):
    name: str = Field(description='The name of the group.')
    path: str = Field(description='The path of the group.')
    auto_devops_enabled: Optional[bool] = Field(None, description='Default to Auto DevOps pipeline for all projects within this group.')
    avatar: Optional[str] = Field(None, description='Image file for avatar of the group. Introduced in GitLab 12.9')
    default_branch_protection: Optional[int] = Field(None, description='See Options for default_branch_protection. Default to the global level default branch protection setting.')
    description: Optional[str] = Field(None, description='The group’s description.')
    emails_disabled: Optional[bool] = Field(None, description='Disable email notifications.')
    lfs_enabled: Optional[bool] = Field(None, description='Enable/disable Large File Storage (LFS) for the projects in this group.')
    mentions_disabled: Optional[bool] = Field(None, description='Disable the capability of a group from getting mentioned.')
    parent_id: Optional[int] = Field(None, description='The parent group ID for creating nested group.')
    project_creation_level: Optional[str] = Field(None, description='Determine if developers can create projects in the group. Can be noone (No one), maintainer (users with the Maintainer role), or developer (users with the Developer or Maintainer role).')
    request_access_enabled: Optional[bool] = Field(None, description='Allow users to request member access.')
    require_two_factor_authentication: Optional[bool] = Field(None, description='Require all users in this group to setup Two-factor authentication.')
    share_with_group_lock: Optional[bool] = Field(None, description='Prevent sharing a project with another group within this group.')
    subgroup_creation_level: Optional[str] = Field(None, description='Allowed to create subgroups. Can be owner (Owners), or maintainer (users with the Maintainer role).')
    two_factor_grace_period: Optional[int] = Field(None, description='Time before Two-factor authentication is enforced (in hours).')
    visibility: Optional[str] = Field(None, description='The group’s visibility. Can be private, internal, or public.')
    membership_lock: Optional[bool] = Field(None, description='Users cannot be added to projects in this group.')
    extra_shared_runners_minutes_limit: Optional[int] = Field(None, description='Can be set by administrators only. Additional compute minutes for this group.')
    shared_runners_minutes_limit: Optional[int] = Field(None, description='Can be set by administrators only. Maximum number of monthly compute minutes for this group. Can be nil (default; inherit system default), 0 (unlimited), or > 0.')
    wiki_access_level: Optional[str] = Field(None, description='The wiki access level. Can be disabled, private, or enabled.')
class TransferProjectToGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the target group')
    project_id: Union[int, str] = Field(description='The ID or URL-encoded path of the project')
class TransferGroup(BaseModel):
    id: int = Field(description='ID of the group to transfer.')
    group_id: Optional[int] = Field(None, description='ID of the new parent group. When not specified, the group to transfer is instead turned into a top-level group.')
class UpdateGroup(BaseModel):
    id: int = Field(description='The ID of the group.')
    name: Optional[str] = Field(None, description='The name of the group.')
    path: Optional[str] = Field(None, description='The path of the group.')
    auto_devops_enabled: Optional[bool] = Field(None, description='Default to Auto DevOps pipeline for all projects within this group.')
    avatar: Optional[str] = Field(None, description='Image file for avatar of the group. Introduced in GitLab 12.9')
    default_branch_protection: Optional[int] = Field(None, description='See Options for default_branch_protection. Default to the global level default branch protection setting.')
    description: Optional[str] = Field(None, description='The description of the group.')
    emails_disabled: Optional[bool] = Field(None, description='Disable email notifications.')
    lfs_enabled: Optional[bool] = Field(None, description='Enable/disable Large File Storage (LFS) for the projects in this group.')
    mentions_disabled: Optional[bool] = Field(None, description='Disable the capability of a group from getting mentioned.')
    parent_id: Optional[int] = Field(None, description='The parent group ID for creating nested group.')
    project_creation_level: Optional[str] = Field(None, description='Determine if developers can create projects in the group. Can be noone (No one), maintainer (users with the Maintainer role), or developer (users with the Developer or Maintainer role).')
    request_access_enabled: Optional[bool] = Field(None, description='Allow users to request member access.')
    require_two_factor_authentication: Optional[bool] = Field(None, description='Require all users in this group to setup Two-factor authentication.')
    share_with_group_lock: Optional[bool] = Field(None, description='Prevent sharing a project with another group within this group.')
    subgroup_creation_level: Optional[str] = Field(None, description='Allowed to create subgroups. Can be owner (Owners), or maintainer (users with the Maintainer role).')
    two_factor_grace_period: Optional[int] = Field(None, description='Time before Two-factor authentication is enforced (in hours).')
    visibility: Optional[str]
class UploadGroupAvatar(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    avatar: str = Field(description='Image file for avatar of the group')
class RemoveGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    permanently_remove: Optional[bool] = Field(None, description='Immediately deletes a subgroup if it is marked for deletion')
    full_path: Optional[str] = Field(None, description='Full path of subgroup to use with permanently_remove')
class RestoreGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class GroupSearch(BaseModel):
    search: str = Field(description='String to match in group name or path')
class ListProvisionedUsers(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the group')
    username: Optional[str] = Field(None, description='Return single user with a specific username')
    search: Optional[str] = Field(None, description='Search users by name, email, username')
    active: Optional[bool] = Field(None, description='Return only active users')
    blocked: Optional[bool] = Field(None, description='Return only blocked users')
    created_after: Optional[str] = Field(None, description='Return users created after the specified time')
    created_before: Optional[str] = Field(None, description='Return users created before the specified time')
class CreateServiceAccountUser(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class CreatePersonalAccessTokenForServiceAccountUser(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    user_id: Union[int, str] = Field(description='The ID of a service account user')
    scopes: List[str] = Field(description='Scopes for the personal access token')
    name: str = Field(description='Name of the personal access token')
class ListGroupHooks(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class GetGroupHook(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    hook_id: int = Field(description='The ID of a group hook')
class AddGroupHook(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    url: str = Field(description='The hook URL')
    push_events: Optional[bool] = Field(None, description='Trigger hook on push events')
    push_events_branch_filter: Optional[str] = Field(None, description='Trigger hook on push events for matching branches only.')
    issues_events: Optional[bool] = Field(None, description='Trigger hook on issues events')
    confidential_issues_events: Optional[bool] = Field(None, description='Trigger hook on confidential issues events')
    merge_requests_events: Optional[bool] = Field(None, description='Trigger hook on merge requests events')
    tag_push_events: Optional[bool] = Field(None, description='Trigger hook on tag push events')
    note_events: Optional[bool] = Field(None, description='Trigger hook on note events')
    confidential_note_events: Optional[bool] = Field(None, description='Trigger hook on confidential note events')
    job_events: Optional[bool] = Field(None, description='Trigger hook on job events')
    pipeline_events: Optional[bool] = Field(None, description='Trigger hook on pipeline events')
    wiki_page_events: Optional[bool] = Field(None, description='Trigger hook on wiki page events')
    deployment_events: Optional[bool] = Field(None, description='Trigger hook on deployment events')
    releases_events: Optional[bool] = Field(None, description='Trigger hook on release events')
    subgroup_events: Optional[bool] = Field(None, description='Trigger hook on subgroup events')
    enable_ssl_verification: Optional[bool] = Field(None, description='Do SSL verification when triggering the hook')
    token: Optional[str] = Field(None, description='Secret token to validate received payloads; not returned in the response')
class EditGroupHook(AddGroupHook):
    hook_id: int = Field(description='The ID of the group hook')
class DeleteGroupHook(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    hook_id: int = Field(description='The ID of the group hook')
class SyncGroupWithLDAP(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class UploadGroupAvatar(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    avatar: str = Field(description='Image file for avatar of the group')
class RemoveGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    permanently_remove: Optional[bool] = Field(None, description='Immediately deletes a subgroup if it is marked for deletion')
    full_path: Optional[str] = Field(None, description='Full path of subgroup to use with permanently_remove')
class RestoreGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class GroupSearch(BaseModel):
    search: str = Field(description='String to match in group name or path')
class ListProvisionedUsers(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the group')
    username: Optional[str] = Field(None, description='Return single user with a specific username')
    search: Optional[str] = Field(None, description='Search users by name, email, username')
    active: Optional[bool] = Field(None, description='Return only active users')
    blocked: Optional[bool] = Field(None, description='Return only blocked users')
    created_after: Optional[str] = Field(None, description='Return users created after the specified time')
    created_before: Optional[str] = Field(None, description='Return users created before the specified time')
class CreateServiceAccountUser(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class CreatePersonalAccessTokenForServiceAccountUser(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    user_id: Union[int, str] = Field(description='The ID of a service account user')
    scopes: List[str] = Field(description='Scopes for the personal access token')
    name: str = Field(description='Name of the personal access token')
class ListGroupHooks(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class GetGroupHook(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    hook_id: int = Field(description='The ID of a group hook')
class AddGroupHook(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    url: str = Field(description='The hook URL')
    push_events: Optional[bool] = Field(None, description='Trigger hook on push events')
    push_events_branch_filter: Optional[str] = Field(None, description='Trigger hook on push events for matching branches only.')
    issues_events: Optional[bool] = Field(None, description='Trigger hook on issues events')
    confidential_issues_events: Optional[bool] = Field(None, description='Trigger hook on confidential issues events')
    merge_requests_events: Optional[bool] = Field(None, description='Trigger hook on merge requests events')
    tag_push_events: Optional[bool] = Field(None, description='Trigger hook on tag push events')
    note_events: Optional[bool] = Field(None, description='Trigger hook on note events')
    confidential_note_events: Optional[bool] = Field(None, description='Trigger hook on confidential note events')
    job_events: Optional[bool] = Field(None, description='Trigger hook on job events')
    pipeline_events: Optional[bool] = Field(None, description='Trigger hook on pipeline events')
    wiki_page_events: Optional[bool] = Field(None, description='Trigger hook on wiki page events')
    deployment_events: Optional[bool] = Field(None, description='Trigger hook on deployment events')
    releases_events: Optional[bool] = Field(None, description='Trigger hook on release events')
    subgroup_events: Optional[bool] = Field(None, description='Trigger hook on subgroup events')
    enable_ssl_verification: Optional[bool] = Field(None, description='Do SSL verification when triggering the hook')
    token: Optional[str] = Field(None, description='Secret token to validate received payloads; not returned in the response')
class EditGroupHook(AddGroupHook):
    hook_id: int = Field(description='The ID of the group hook')
class DeleteGroupHook(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    hook_id: int = Field(description='The ID of the group hook')
class SyncGroupWithLDAP(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class ListLDAPGroupLinks(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class AddLDAPGroupLinkWithCNOrFilter(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    cn: Optional[str] = Field(None, description='The CN of an LDAP group')
    filter: Optional[str] = Field(None, description='The LDAP filter for the group')
    group_access: int = Field(description='Role (access_level) for members of the LDAP group')
    provider: str = Field(description='LDAP provider for the LDAP group link')
class DeleteLDAPGroupLink(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    cn: str = Field(description='The CN of an LDAP group')
    provider: Optional[str] = Field(None, description='LDAP provider for the LDAP group link')
class DeleteLDAPGroupLinkWithCNOrFilter(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    cn: Optional[str] = Field(None, description='The CN of an LDAP group')
    filter: Optional[str] = Field(None, description='The LDAP filter for the group')
    provider: str = Field(description='LDAP provider for the LDAP group link')
class ListSAMLGroupLinks(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the group')
class GetSAMLGroupLink(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the group')
    saml_group_name: str = Field(description='Name of an SAML group')
class AddSAMLGroupLink(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the group')
    saml_group_name: str = Field(description='Name of a SAML group')
    access_level: int = Field(description='Role (access_level) for members of the SAML group')
class DeleteSAMLGroupLink(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the group')
    saml_group_name: str = Field(description='Name of a SAML group')
class CreateLinkToShareGroupWithAnotherGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    group_id: int = Field(description='The ID of the group to share with')
    group_access: int = Field(description='The role (access_level) to grant the group')
    expires_at: Optional[str] = Field(None, description='Share expiration date in ISO 8601 format: 2016-09-26')
class DeleteLinkSharingGroupWithAnotherGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    group_id: int = Field(description='The ID of the group to share with')
class GetGroupPushRules(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
class AddGroupPushRule(BaseModel):
    id: Union[int, str] = Field()
class GroupPushRule(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')
    deny_delete_tag: Optional[bool] = Field(None, description='Deny deleting a tag')
    member_check: Optional[bool] = Field(None, description='Allows only GitLab users to author commits')
    prevent_secrets: Optional[bool] = Field(None, description='Files that are likely to contain secrets are rejected')
    commit_message_regex: Optional[str] = Field(None, description='Commit message must match the regex')
    commit_message_negative_regex: Optional[str] = Field(None, description='Commit message must not match the regex')
    branch_name_regex: Optional[str] = Field(None, description='Branch name must match the regex')
    author_email_regex: Optional[str] = Field(None, description='Author email must match the regex')
    file_name_regex: Optional[str] = Field(None, description='Filename must not match the regex')
    max_file_size: Optional[int] = Field(None, description='Maximum file size (MB) allowed')
    commit_committer_check: Optional[bool] = Field(None, description='Only allow commits from verified emails')
    reject_unsigned_commits: Optional[bool] = Field(None, description='Only allow commits signed through GPG')
class GroupID(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group')