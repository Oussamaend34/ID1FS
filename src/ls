import click
import os
import sys
import id1fs_functions as id1fs

cwd = id1fs.get_cwd()

@click.command()
@click.argument("path", type=click.STRING, required=0, default=cwd)
def list_files(path):
    """List files in the given directory."""
    path = id1fs.generate_full_path(path)
    root = id1fs.get_root()
    if not id1fs.check_status():
        click.echo("The filesystem is not started.")
        sys.exit()
    if not id1fs.check_user():
        click.echo("You are not connected to ID1FS.")
        sys.exit()
    if os.path.isdir(path):
        click.echo(f"Listing files in {path.replace(root,"")}")
        for file in os.listdir(path):
            click.echo(file)
    else:
        click.echo(f"cannot access {path.replace(root,"")} : No such directory")

list_files()