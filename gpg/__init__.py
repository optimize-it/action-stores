import time
from os import environ
from pprint import pprint

from kubiya import ActionStore, get_secret

actionstore = ActionStore("gpg-gen2", "0.1.0")
actionstore.uses_secrets(["GITHUB_PERSONAL_ACCESS_TOKEN","GPG_KEY_PASSPHRASE"])