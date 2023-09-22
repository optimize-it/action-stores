from . import action_store

def get_secrets():
    AZURE_CLIENT_SECRET = action_store.secrets.get("AZURE_CLIENT_SECRET")
    AZURE_CLIENT_ID = action_store.secrets.get("AZURE_CLIENT_ID")
    AZURE_TENANT_ID = action_store.secrets.get("AZURE_TENANT_ID")
    return AZURE_CLIENT_SECRET, AZURE_CLIENT_ID, AZURE_TENANT_ID

def get_subscription_id_secret():
    AZURE_SUBSCRIPTION_ID = action_store.secrets.get("AZURE_SUBSCRIPTION_ID")
    print(AZURE_SUBSCRIPTION_ID)
    return AZURE_SUBSCRIPTION_ID
