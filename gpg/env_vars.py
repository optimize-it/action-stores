import os
def get_orgname():
    return os.environ.get("GITHUB_ORGANIZATION_NAME", 'kubi-org')

def get_orgprefix():
    return get_orgname() + "/"

def get_gpg_user_mail():
    return os.environ.get("GPG_USER_MAIL", 'gpg mail')

def get_git_user_name():
    return os.environ.get("GIT_USER_NAME", 'name')

def get_git_user_mail():
    return os.environ.get("GIT_USER_MAIL", 'git mail')