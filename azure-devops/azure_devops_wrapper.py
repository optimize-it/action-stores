import logging
import requests
from .secrets import get_secrets, get_subscription_id_secret
from requests import Session

logger = logging.getLogger(__name__)


############################################################################################################################################################
#################################################################Azure DevOps###############################################################################
############################################################################################################################################################
def get_token_for_azure_devops():
    AZURE_CLIENT_SECRET, AZURE_CLIENT_ID, AZURE_TENANT_ID = get_secrets()
    # ORGANISATION_NAME = 'kubiyaai'
    # # Azure DevOps organization URL
    # organization_url = f'https://dev.azure.com/{ORGANISATION_NAME}'
    # # Construct the token endpoint
    token_url = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/token"

    # Define the token request data
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': AZURE_CLIENT_ID,
        'client_secret': AZURE_CLIENT_SECRET,
        'resource': 'https://management.core.windows.net/',
    }

    # Get the OAuth token
    response = requests.post(token_url, data=token_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    if response.status_code == 200:
        token = response.json()['access_token']
        return token
        # headers = {
        #     'Authorization': f'Bearer {access_token}',
        # }
        # print(headers)
        # Example: Make a GET request to list all projects in Azure DevOps
        # projects_url = f"{organization_url}/_apis/projects?api-version=7.0"
        # response = requests.get(projects_url, headers=headers)
        # print(response)

        # if response.status_code == 200:
        #     projects = response.json()
        #     for project in projects['value']:
        #         print(f"Project ID: {project['id']}, Project Name: {project['name']}")
        # else:
        #     print(f"Failed to fetch projects. Status code: {response.status_code}")
    else:
        print(f"Failed to obtain access token. Status code: {response.status_code}")

def get_devops_session():
    session = Session()
    session.headers.update({"Content-Type": "application/json","Authorization": f"Bearer {get_token_for_azure_devops()}",})
    return session

def get_wrapper_azure_devops(endpoint: str, api_version: str) -> dict:
    session = get_devops_session()
    base_url = f"https://dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.get(url)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        response.raise_for_status()

def head_wrapper(endpoint: str, api_version: str) -> dict:
    session = get_devops_session()
    base_url = f"https://dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    print(url)
    response = session.head(url)
    print(response)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        response.raise_for_status()

def post_wrapper_azure_devops(endpoint: str, api_version: str, post_data: dict = None) -> dict:
    session = get_devops_session()
    base_url = f"https://dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.post(url,data=post_data)
    print(response)
    if 200 <= response.status_code < 300:
        print(response.json())
        return response.json()
    else:   
        response.raise_for_status()

# def delete_wrapper_azure_devops(endpoint: str, api_version: str) -> dict:
#     session = get_devops_session()

def delete_wrapper(endpoint: str, api_version: str) -> dict:
    session = get_devops_session()
    # subscriptionId = get_subscription_id_secret()
    base_url = f"https://dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.delete(url)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful delete request: {url}")
        return {"successfully accepted with status code:" : response.status_code}
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"DELETE request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}


def patch_wrapper(endpoint: str,api_version: str, patch_data: dict = None) -> dict:
    session = get_devops_session()
    # subscriptionId = get_subscription_id_secret()
    base_url = f"https://dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.patch(url,json=patch_data)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful PATCH request: {url}")
        return response.status_code
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"PATCH request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}
        
def put_wrapper_azure_devops(endpoint: str, api_version: str, data: dict = None) -> dict:
    session = get_devops_session()
    base_url = f"https://dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.put(url,json=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:   
        response.raise_for_status()

def post_wrapper_new(endpoint: str, api_version: str, data: dict = None) -> dict:
    session = get_devops_session()
    base_url = f"https://vsrm.dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.post(url,json=data)
    if 200 <= response.status_code < 300:
        return response.json()
    else:   
        response.raise_for_status()

def patch_wrapper_new(endpoint: str, data: dict = None) -> dict:
    session = get_devops_session()
    # subscriptionId = get_subscription_id_secret()
    base_url = f"https://vsrm.dev.azure.com"
    url = f"{base_url}{endpoint}"
    response = session.delete(url,json=data)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful PATCH request: {url}")
        return response.status_code
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"PATCH request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}
        
def delete_wrapper_new(endpoint: str, api_version: str) -> dict:
    session = get_devops_session()
    # subscriptionId = get_subscription_id_secret()
    base_url = f"https://vsrm.dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.delete(url)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful delete request: {url}")
        return {"successfully accepted with status code:" : response.status_code}
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"DELETE request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}
        
def get_wrapper_new(endpoint: str, api_version: str) -> dict:
    session = get_devops_session()
    base_url = f"https://vsrm.dev.azure.com"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.get(url)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful GET request: {url}")
        return response.json()
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"GET request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}