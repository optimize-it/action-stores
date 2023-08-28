from .. github_wrapper import get_github_instance , get_entity, get_input_git_tree_element
from .. env_vars import get_orgname, get_gpg_user_mail
from .. secrets import get_gpg_key_passphrase
from  ..store_utils import remove_backticks
from .. import actionstore as store
from .. models.deploy_app import (
    DeployAppParams,DeployAppResponse
)

import logging
import gnupg
import base64
import html
import subprocess

logging.basicConfig(level=logging.INFO)

@store.kubiya_action()
def app_deploy(params: DeployAppParams)-> DeployAppResponse:
    # git_user_name = get_git_user_name()
    # org_name = get_orgname()
    # gpg_user_email = get_gpg_user_mail()

    # repo_name = params["repo_name"]
    # commit_user = params["commit_user"]
    # branch_name = params["branch_name"]


    # Files to update
    files_list = [
    {"path": f".github/{params.branch_name}.gpg",
                "content": params.env_file_content},

    {"path": f".github/workflows/{params.branch_name}.yml",
                             "content": params.github_workflows_file_content},

    {"path": "infra/docker/Dockerfile",
                   "content": params.docker_file_content},

    {"path": "infra/helm/Chart.yaml",
                  "content": params.chart_yaml_content},

    {"path": f"infra/helm/{params.branch_name}.values.yaml",
                   "content": params.values_yaml_content},

    {"path": "infra/helm/templates/deployment.yaml",
                       "content": params.deployment_yaml_content},

    {"path": "infra/helm/templates/service.yaml",
                    "content": params.service_yaml_content},

    {"path": "infra/helm/templates/hpa.yaml",
                "content": params.hpa_yaml_content}
    ]
    # files_list = [env_file,
    #               github_workflows_file,
    #               docker_file,
    #               chart_yaml, values_yaml,
    #               deployment_yaml,
    #               service_yaml,
    #               hpa_yaml]

    try:

        github = get_github_instance()
        entity = get_entity(github)

        # repo = entity.get_repo(f"{get_orgname()}/{params.repo_name}")
        repo = entity.get_repo(f"{params.repo_name}")
        base_tree = repo.get_git_tree(sha=params.branch_name)

        element_list = []

        for file in files_list:

            # remove ``` from the file content
            content = remove_backticks(string=file.get('content'))

            # remove < > from the file content #TODO: remove after KFI-3 solved
            content = content.replace("<", "").replace(">", "")

            # Handle html entities from slack (> < &) #TODO: remove after KFI-3 solved
            html_ents = ["&amp;",
                         "&lt;",
                         "&gt;"]

            for ent in html_ents:
                if ent in content:
                    content = content.replace(ent, html.unescape(ent))

            # Handle .gpg files:
            if file.get('path').endswith(".gpg"):
                gpg = gnupg.GPG()
                encrypted_data = gpg.encrypt(data=content,
                                             recipients=get_gpg_user_mail(),
                                             symmetric='AES256',
                                             passphrase=get_gpg_key_passphrase(),
                                             armor=False)

                file_content = encrypted_data.data
                file_content_base64 = base64.b64encode(file_content).decode()
                blob = repo.create_git_blob(file_content_base64, 'base64')
            else:
                file_content = content
                blob = repo.create_git_blob(file_content, 'utf-8')

            element = get_input_git_tree_element(path=file.get('path'), sha=blob.sha)
            # element = InputGitTreeElement(path=file.get('path'), mode="100644", type="blob", sha=blob.sha)
            element_list.append(element)

        tree = repo.create_git_tree(element_list, base_tree)

        # Create a new commit with that tree on top of the current branch head
        commit = repo.create_git_commit(
            message=f"Add files by {params.commit_user}",
            tree=repo.get_git_tree(sha=tree.sha),
            parents=[repo.get_git_commit(repo.get_branch(params.branch_name).commit.sha)],
        )

        # Push that commit to the branch by editing the reference
        ref = repo.get_git_ref(ref=f'heads/{params.branch_name}')
        ref.edit(sha=commit.sha)

        html_url=repo.get_git_commit(ref.object.sha).html_url
        return DeployAppResponse(html_url=html_url)

    except subprocess.CalledProcessError as e:
        logging.error(e.output)
        return e.output