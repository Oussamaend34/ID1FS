import json 
import subprocess

env = {}
User =subprocess.run("whoami", capture_output=True).stdout.decode("utf-8").strip()
env["root"] = f"/home/{User}/.id1fs/ID1FS"
env["bf"] = f"/home/{User}/.id1fs/ID1FS/backup"
env["md"] = f"/home/{User}/.id1fs/ID1FS/metadata"
env["log"] = f"/home/{User}/.id1fs/ID1FS/system/log"
env["systm"] = f"/home/{User}/.id1fs/ID1FS/system"
env["cwd"] = f"/home"

with open('system/env.json','w') as f:
    json.dump(env, f, indent=4)

with open('system/logs','w') as f:
    f.write("")
