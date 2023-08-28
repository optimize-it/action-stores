import requests
from typing import Any
from .secrets import *
import json

def get_token() -> str:
    ARGO_USER = get_user()
    ARGO_PASS = get_password()
    ARGO_SERVER = get_server()
    payload = {"username": f"{ARGO_USER}", "password": f"{ARGO_PASS}"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{ARGO_SERVER}/api/v1/session", json=payload, headers=headers, verify=False)
    response.raise_for_status()
    token = response.json()["token"]
    return token

def get_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.get(f"{ARGO_SERVER}/api/v1{endpoint}",  params=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def get_wrapper_logs(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.get(f"{ARGO_SERVER}/api/v1{endpoint}",  params=params, headers=headers, verify=False)
    logs = [json.loads(line) for line in response.text.splitlines() if line]
    return logs 

def post_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(f"{ARGO_SERVER}/api/v1{endpoint}",  params=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def post_json_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(f"{ARGO_SERVER}/api/v1{endpoint}",  json=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()


def put_json_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.put(f"{ARGO_SERVER}/api/v1{endpoint}",  json=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def put_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.put(f"{ARGO_SERVER}/api/v1{endpoint}",  params=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def delete_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.delete(f"{ARGO_SERVER}/api/v1{endpoint}",  params=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def delete_json_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.delete(f"{ARGO_SERVER}/api/v1{endpoint}",  json=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

def patch_wrapper(endpoint: str, params: dict = None) -> Any:
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.patch(f"{ARGO_SERVER}/api/v1{endpoint}",  params=params, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()


# def post_wrapper(endpoint: str, args: Dict = None) -> Any:
#     token = get_token()
#     ARGO_SERVER = get_server()

#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json",
#         "Accept": "application/json"
#     }
#     response = requests.post(f"{ARGO_SERVER}/api/v1{endpoint}", json=args, headers=headers, verify=False)
#     response.raise_for_status()
#     return response.json()

# def get_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
#     host,token = get_secrets()

#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", }
#     ret = requests.get(f"{host}{endpoint}", headers=headers, params=args)

#     if not ret.ok:
#         raise Exception(f"Error: {ret.status_code} {ret.text}")
#     if ret.headers.get("Content-Type", "").startswith("application/json"):
#         return ret.json()
#     else:
#         return ret.text