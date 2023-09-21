import logging
import requests
from .secrets import get_secrets, get_subscription_id_secret
from requests import Session

logger = logging.getLogger(__name__)


def get_api_token():
    AZURE_CLIENT_SECRET, AZURE_CLIENT_ID, AZURE_TENANT_ID = get_secrets()

    token_url = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0/token"
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': AZURE_CLIENT_ID,
        'client_secret': AZURE_CLIENT_SECRET,
        'scope': 'https://management.azure.com/.default'
    }
    response = requests.post(token_url, data=token_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    response.raise_for_status()
    token = response.json().get('access_token')
    # print(token)
    logger.debug(f"Token: {token}")
    return token

def get_api_token_storage():
    AZURE_CLIENT_SECRET, AZURE_CLIENT_ID, AZURE_TENANT_ID = get_secrets()

    token_url = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/v2.0/token"
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': AZURE_CLIENT_ID,
        'client_secret': AZURE_CLIENT_SECRET,
        'resource': 'https://storage.azure.com/'
    }
    response = requests.post(token_url, data=token_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    response.raise_for_status()
    token = response.json().get('access_token')
    # print(token)
    logger.debug(f"Token: {token}")
    return token

def get_session():
    session = Session()
    session.headers.update({"Authorization": f"Bearer {get_api_token()}"})
    return session

def get_session_storage():
    session = Session()
    session.headers.update({"Authorization": f"Bearer {get_api_token_storage()}"})
    return session
# def get_subscription_id():
#     AZURE_SUBSCRIPTION_ID = get_subscription_id_secret()
#     if AZURE_SUBSCRIPTION_ID != None:       
#         return AZURE_SUBSCRIPTION_ID
#     else:
#         logger.debug(AZURE_SUBSCRIPTION_ID)
#         raise
        

def get_wrapper(endpoint: str, api_version: str) -> dict:
    session = get_session()
    subscriptionId = get_subscription_id_secret()
    print(subscriptionId)
    base_url = f"https://management.azure.com/subscriptions/{subscriptionId}"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.get(url)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        response.raise_for_status()

def post_wrapper(endpoint: str, api_version: str) -> dict:
    session = get_session()
    subscriptionId = get_subscription_id_secret()
    base_url = f"https://management.azure.com/subscriptions/{subscriptionId}"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.post(url)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful POST request: {url}")
        return response.status_code
    else:
        response.raise_for_status()

def put_wrapper(endpoint: str, api_version: str, data: dict = None) -> dict:
    session = get_session()
    subscriptionId = get_subscription_id_secret()
    base_url = f"https://management.azure.com/subscriptions/{subscriptionId}"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.put(url, json=data)
    if response.status_code == 200 or response.status_code == 201:
        logger.info(f"Successful PUT request: {url}")
        return response.json()
    elif response.status_code == 202:
        logger.info(f"Successful PUT request: {url} with status code {response.status_code}")
        return response
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"PUT request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}  # Return the error as a string
        
def delete_wrapper(endpoint: str, api_version: str) -> dict:
    session = get_session()
    subscriptionId = get_subscription_id_secret()
    base_url = f"https://management.azure.com/subscriptions/{subscriptionId}"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.delete(url)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful delete request: {url}")
        return response.status_code
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"DELETE request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}
        

def patch_wrapper(endpoint: str, api_version: str, data: dict = None) -> dict:
    session = get_session()
    subscriptionId = get_subscription_id_secret()
    base_url = f"https://management.azure.com/subscriptions/{subscriptionId}"
    url = f"{base_url}{endpoint}?api-version={api_version}"
    response = session.patch(url, json=data)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful delete request: {url}")
        return response.json()
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"PATCH request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}
        
def blob_get_wrapper(endpoint: str, storageAccountName: str) -> dict:
    session = get_session_storage()
    subscriptionId = get_subscription_id_secret()
    base_url = f"https://{storageAccountName}.blob.core.windows.net"
    url =f"{base_url}{endpoint}"
    response = session.get(url)
    if 200 <= response.status_code < 300:
        logger.info(f"Successful get request: {url}")
        return response.json()
    else:
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logger.error(f"GET request failed with status {response.status_code} for URL: {url}")
            logger.error(f"Error response: {response.text}")
            return {"error": str(err)}
# ############################################################################################################################################################
# #################################################################Azure DevOps###############################################################################
# ############################################################################################################################################################
# def get_token_for_azure_devops():
#     AZURE_CLIENT_SECRET, AZURE_CLIENT_ID, AZURE_TENANT_ID = get_secrets()
#     # ORGANISATION_NAME = 'kubiyaai'
#     # # Azure DevOps organization URL
#     # organization_url = f'https://dev.azure.com/{ORGANISATION_NAME}'
#     # # Construct the token endpoint
#     token_url = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}/oauth2/token"

#     # Define the token request data
#     token_data = {
#         'grant_type': 'client_credentials',
#         'client_id': AZURE_CLIENT_ID,
#         'client_secret': AZURE_CLIENT_SECRET,
#         'resource': 'https://management.core.windows.net/',
#     }

#     # Get the OAuth token
#     response = requests.post(token_url, data=token_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
#     print(response)
#     if response.status_code == 200:
#         token = response.json()['access_token']
#         print(token)
#         return token
#         # headers = {
#         #     'Authorization': f'Bearer {access_token}',
#         # }
#         # print(headers)
#         # Example: Make a GET request to list all projects in Azure DevOps
#         # projects_url = f"{organization_url}/_apis/projects?api-version=7.0"
#         # response = requests.get(projects_url, headers=headers)
#         # print(response)

#         # if response.status_code == 200:
#         #     projects = response.json()
#         #     for project in projects['value']:
#         #         print(f"Project ID: {project['id']}, Project Name: {project['name']}")
#         # else:
#         #     print(f"Failed to fetch projects. Status code: {response.status_code}")
#     else:
#         print(f"Failed to obtain access token. Status code: {response.status_code}")

# def get_devops_session():
#     session = Session()
#     session.headers.update({"Authorization": f"Bearer {get_token_for_azure_devops()}"})
#     return session

# def get_wrapper_azure_devops(endpoint: str, api_version: str) -> dict:
#     session = get_devops_session()
#     base_url = f"https://dev.azure.com"
#     url = f"{base_url}{endpoint}?api-version={api_version}"
#     response = session.get(url)
#     if 200 <= response.status_code < 300:
#         return response.json()
#     else:
#         response.raise_for_status()

# def post_wrapper_azure_devops(endpoint: str, api_version: str) -> dict:
#     session = get_devops_session()
#     base_url = f"https://dev.azure.com"
#     url = f"{base_url}{endpoint}?api-version={api_version}"
#     response = session.post(url)
#     if 200 <= response.status_code < 300:
#         return response.json()
#     else:
#         response.raise_for_status()