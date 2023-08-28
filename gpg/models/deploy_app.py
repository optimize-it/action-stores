from pydantic import BaseModel
from typing import List

class DeployAppParams(BaseModel):
    repo_name: str
    commit_user: str
    branch_name: str
    env_file_content: str
    github_workflows_file_content: str
    docker_file_content: str
    chart_yaml_content: str
    values_yaml_content: str
    deployment_yaml_content: str
    service_yaml_content: str
    hpa_yaml_content: str

class DeployAppResponse(BaseModel):
    html_url: str