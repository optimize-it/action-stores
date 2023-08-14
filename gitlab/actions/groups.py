from typing import List, Any, Optional, Union
from pydantic import BaseModel
from datetime import datetime
from ..models.groups import *

from .. import action_store as action_store
from ..http_wrapper import *

@action_store.kubiya_action()
def list_groups(input: GroupList):
    response = get_wrapper(endpoint='/groups', args=input.dict(exclude_none=True))
    return Groups(groups=response)

@action_store.kubiya_action()
def list_group_subgroups(input: GroupSubgroupsList):
    response = get_wrapper(endpoint=f'/groups/{input.id}/subgroups', args=input.dict(exclude_none=True))
    return Groups(groups=response)

@action_store.kubiya_action()
def list_group_descendant_groups(input: GroupSubgroupsList):
    response = get_wrapper(endpoint=f'/groups/{input.id}/descendant_groups', args=input.dict(exclude_none=True))
    return Groups(groups=response)

@action_store.kubiya_action()
def list_group_projects(input: GroupProjectsList):
    response = get_wrapper(endpoint=f'/groups/{input.id}/projects', args=input.dict(exclude_none=True))
    return Groups(groups=response)
    
@action_store.kubiya_action()
def list_group_shared_projects(input: GroupSharedProjectsList):
    response = get_wrapper(endpoint=f'/groups/{input.id}/projects/shared', args=input.dict(exclude_none=True))
    return Group(groups=response)


@action_store.kubiya_action()
def get_group_details(input: GroupDetails):
    response = get_wrapper(endpoint=f'/groups/{input.id}')
    return Group(groups = response)


# @action_store.kubiya_action()
# def download_group_avatar(input: GroupAvatar):
#     return get_wrapper(endpoint=f'/groups/{input.id}/avatar', args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def create_new_group(input: NewGroup):
    return post_wrapper(endpoint='/groups', args=input.dict(exclude_none=True))

# @action_store.kubiya_action()
# def transfer_project_to_group(input: TransferProjectToGroup):
#     return post_wrapper(endpoint=f'/groups/{input.id}/projects/{input.project_id}', args=input.dict(exclude_none=True))

# @action_store.kubiya_action()
# def transfer_group(input: TransferGroup):
#     return post_wrapper(endpoint=f'/groups/{input.id}/transfer', args=input.dict(exclude_none=True))

# @action_store.kubiya_action()
# def update_group(input: UpdateGroup):
#     return put_wrapper(endpoint=f'/groups/{input.id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def upload_group_avatar(input: UploadGroupAvatar):
#     return put_wrapper(endpoint=f'/groups/{input.id}', args=input.dict())
# @action_store.kubiya_action()
# def remove_group(input: RemoveGroup):
#     return delete_wrapper(endpoint=f'/groups/{input.id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def restore_group(input: RestoreGroup):
#     return post_wrapper(endpoint=f'/groups/{input.id}/restore', args=input.dict())
# @action_store.kubiya_action()
# def search_for_group(input: GroupSearch):
#     return get_wrapper(endpoint=f'/groups', args=input.dict())
# @action_store.kubiya_action()
# def list_provisioned_users(input: ListProvisionedUsers):
#     return get_wrapper(endpoint=f'/groups/{input.id}/provisioned_users', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def create_service_account_user(input: CreateServiceAccountUser):
#     return post_wrapper(endpoint=f'/groups/{input.id}/service_accounts', args=input.dict())
# @action_store.kubiya_action()
# def create_personal_access_token_for_service_account_user(input: CreatePersonalAccessTokenForServiceAccountUser):
#     return post_wrapper(endpoint=f'/groups/{input.id}/service_accounts/{input.user_id}/personal_access_tokens', args=input.dict())

@action_store.kubiya_action()
def list_group_hooks(input: ListGroupHooks):
    response = get_wrapper(endpoint=f'/groups/{input.id}/hooks', args=input.dict())
    return Hooks(hooks = response)

# @action_store.kubiya_action()
# def get_group_hook(input: GetGroupHook):
#     return get_wrapper(endpoint=f'/groups/{input.id}/hooks/{input.hook_id}', args=input.dict())
# @action_store.kubiya_action()
# def add_group_hook(input: AddGroupHook):
#     return post_wrapper(endpoint=f'/groups/{input.id}/hooks', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def edit_group_hook(input: EditGroupHook):
#     return put_wrapper(endpoint=f'/groups/{input.id}/hooks/{input.hook_id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_group_hook(input: DeleteGroupHook):
#     return delete_wrapper(endpoint=f'/groups/{input.id}/hooks/{input.hook_id}', args=input.dict())
# @action_store.kubiya_action()
# def sync_group_with_ldap(input: SyncGroupWithLDAP):
#     return post_wrapper(endpoint=f'/groups/{input.id}/ldap_sync', args=input.dict())
# @action_store.kubiya_action()
# def list_ldap_group_links(input: ListLDAPGroupLinks):
#     return get_wrapper(endpoint=f'/groups/{input.id}/ldap_group_links', args=input.dict())
# @action_store.kubiya_action()
# def add_ldap_group_link_with_cn_or_filter(input: AddLDAPGroupLinkWithCNOrFilter):
#     return post_wrapper(endpoint=f'/groups/{input.id}/ldap_group_links', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_ldap_group_link(input: DeleteLDAPGroupLink):
#     return delete_wrapper(endpoint=f'/groups/{input.id}/ldap_group_links/{input.cn}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_ldap_group_link_with_cn_or_filter(input: DeleteLDAPGroupLinkWithCNOrFilter):
#     return delete_wrapper(endpoint=f'/groups/{input.id}/ldap_group_links', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def list_saml_group_links(input: ListSAMLGroupLinks):
#     return get_wrapper(endpoint=f'/groups/{input.id}/saml_group_links', args=input.dict())
# @action_store.kubiya_action()
# def get_saml_group_link(input: GetSAMLGroupLink):
#     return get_wrapper(endpoint=f'/groups/{input.id}/saml_group_links/{input.saml_group_name}', args=input.dict())
# @action_store.kubiya_action()
# def add_saml_group_link(input: AddSAMLGroupLink):
#     return post_wrapper(endpoint=f'/groups/{input.id}/saml_group_links', args=input.dict())
# @action_store.kubiya_action()
# def delete_saml_group_link(input: DeleteSAMLGroupLink):
#     return delete_wrapper(endpoint=f'/groups/{input.id}/saml_group_links/{input.saml_group_name}', args=input.dict())
# @action_store.kubiya_action()
# def create_link_to_share_group_with_another_group(input: CreateLinkToShareGroupWithAnotherGroup):
#     return post_wrapper(endpoint=f'/groups/{input.id}/share', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_link_sharing_group_with_another_group(input: DeleteLinkSharingGroupWithAnotherGroup):
#     return delete_wrapper(endpoint=f'/groups/{input.id}/share/{input.group_id}', args=input.dict())

@action_store.kubiya_action()
def get_group_push_rules(input: GetGroupPushRules):
    response = get_wrapper(endpoint=f'/groups/{input.id}/push_rule', args=input.dict())
    return Rules(rules = response)

# @action_store.kubiya_action()
# def add_group_push_rule(input: GroupPushRule):
#     return post_wrapper(endpoint=f'/groups/{input.id}/push_rule', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def edit_group_push_rule(input: GroupPushRule):
#     return put_wrapper(endpoint=f'/groups/{input.id}/push_rule', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_group_push_rule(input: GroupID):
#     return delete_wrapper(endpoint=f'/groups/{input.id}/push_rule')