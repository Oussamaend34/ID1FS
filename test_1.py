from cryptography.fernet import Fernet
import json



def get_user():
    with open("system/id1fs_status.json", "r") as f:
        stat = json.load(f)
    return stat["connected_user"]


# Generate a key
def load_key():
    with open("system/key.key", "rb") as f:
        key = f.read()
    return key

def get_cwd():
    """Return the current working directory."""
    with open("system/env.json", "r") as f:
        stat = json.load(f)
    return stat["cwd"]


def check_if_full_path(path):
    """Check if the path is a full path."""
    if path[0] == "/":
        return True
    else:
        return False

def get_root():
    """Return the root directory."""
    with open("system/env.json", "r") as f:
        stat = json.load(f)
    return stat["root"]

def generate_full_path(path):
    """Generate a name for a file."""
    if check_if_full_path(path):
        name = path
        return get_root() + name
    else:
        if path[0] == ".":
            name = path[1:]
            name = get_cwd() + name
            return name
        else:
            return get_cwd() + '/' +path


def generate_md_name(path):
    """generate the backup name"""
    key = load_key()
    fernet = Fernet(key)
    md_name= path + '|' +get_user()
    md_name = fernet.encrypt(md_name.encode()).decode('utf-8')
    return md_name


def restore_bp_name(bp_name):
    """Restore the backup path and owner."""
    key = load_key()
    fernet = Fernet(key)
    temp = fernet.decrypt(bp_name).decode('utf-8')
    path = temp.split("|")[0]
    owner = temp.split("|")[1]
    return [path, owner]