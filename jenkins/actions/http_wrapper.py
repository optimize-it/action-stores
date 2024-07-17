import requests
from .secrets import get_secrets
from security import safe_requests

def get_wrapper(path: str):
    host, username, password = get_secrets()
    ret = safe_requests.get(f"{host}/{path}", auth=(username, password), headers={"Accept": "application/json"})
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text
    
def get_wrapper_full_response(path: str):
    host, username, password = get_secrets()
    ret = safe_requests.get(f"{host}/{path}", auth=(username, password), headers={"Accept": "application/json"})
    return ret
    
def post_wrapper(endpoint: str, args: dict=None):
    host, username, password = get_secrets()
    ret = requests.post(f"{host}{endpoint}", auth=(username, password), data=args, headers={"Content-Type": "application/json", "Accept": "application/json"})
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text

def post_wrapper_full_response(endpoint: str, args: dict=None):
    host, username, password = get_secrets()
    ret = requests.post(f"{host}{endpoint}", auth=(username, password), data=args, headers={"Content-Type": "application/json", "Accept": "application/json"})
    return ret
