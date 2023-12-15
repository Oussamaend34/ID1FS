import click
import sys
import getpass
import json
import id1fs_functions as id1fs


@click.command()
@click.argument("user", type=str, required=1)
def login(user):
    """connect to ID1FS."""
    try:
        with open("system/login.json", "r")as f:
            users = json.load(f)
    except FileNotFoundError:
        click.echo("No users found.")
        sys.exit()
    except json.decoder.JSONDecodeError:
        click.echo("No users found.")
        sys.exit()
    if user not in users.keys():
        click.echo("This user doesn't exist.\nPlease sign up first.")
        sys.exit()
    password=getpass.getpass("Enter the user password :")
    password=id1fs.hash_string(password)
    if password == users[user].strip():
        with open("system/id1fs_status.json", "r") as f:
            stat = json.load(f)
        stat["connected_user"] = user
        with open("system/id1fs_status.json", "w")as f:
            json.dump(stat, f)
    else:
        click.echo("Wrong password.")
        sys.exit()


if __name__== "__main__":
    login()