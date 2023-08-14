from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.repositories import *

from .. import action_store as action_store
from ..http_wrapper import *

@action_store.kubiya_action()
def list_repository_tree(input: ProjectsIdRepositoryTree):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/tree', args=input.dict(exclude_none=True))
    return ListDict(response=response)

@action_store.kubiya_action()
def get_a_blob_from_repository(input: ProjectsIdRepositoryBlobsSha):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/blobs/{input.sha}', args=input.dict(exclude_none=True))


@action_store.kubiya_action()
def raw_blob_content(input: ProjectsIdRepositoryBlobsShaRaw):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/blobs/{input.sha}/raw', args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_file_archive(input: ProjectsIdRepositoryArchive):
    format_suffix = f'.{input.format}' if input.format else ''
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/archive{format_suffix}', args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def compare_branches_tags_or_commits(input: ProjectsIdRepositoryCompare):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/repository/compare', args=input.dict(exclude_none=True, by_alias=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def contributors(input: ProjectsIdRepositoryContributors):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/contributors', args=input.dict(exclude_none=True))
    return ListDict(response=response)

@action_store.kubiya_action()
def get_merge_base(input: ProjectsIdRepositoryMergebase):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/merge_base', params={'refs[]': input.refs})
    return SingleDict(response=response)

@action_store.kubiya_action()
def add_changelog_data_to_a_changelog_file(input: ProjectsIdRepositoryChangelog):
    return post_wrapper(endpoint=f'/projects/{input.id}/repository/changelog', args=input.dict(by_alias=True, exclude_none=True))

@action_store.kubiya_action()
def generate_changelog_data(input: GenerateChangelogData):
    response = get_wrapper(endpoint=f'/projects/{input.id}/repository/changelog', args=input.dict(by_alias=True, exclude_none=True))
    return SingleDict(response=response)