from . import actionstore as action_store

def get_github_personal_access_token():
    token = action_store.secrets.get("GITHUB_PERSONAL_ACCESS_TOKEN")
    if token is None:
        raise EnvironmentError("GITHUB_PERSONAL_ACCESS_TOKEN is not set as secret.")
    return token

def get_gpg_key_passphrase():
    token = action_store.secrets.get("GPG_KEY_PASSPHRASE")
    if token is None:
        raise EnvironmentError("GPG_KEY_PASSPHRASE is not set as secret.")
    return token
