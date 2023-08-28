from github import Github ,InputGitTreeElement
from .secrets import get_github_personal_access_token
from .env_vars import get_git_user_name,get_orgname
import os

def get_github_instance() -> Github:
    # return Github(get_git_user_name(),get_github_personal_access_token())
    return Github(get_github_personal_access_token())

def get_entity(github: Github):
    if os.getenv('GITHUB_USER_MODE', 'False').lower() == 'true':
        return github.get_user()
    else:
        return github.get_organization(get_orgname())

def get_input_git_tree_element(path,sha):
    return InputGitTreeElement(path=path,mode='100644',type='blob',sha=sha)

