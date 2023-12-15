import click


@click.group()
def my_commands():
    pass

@click.command()
@click.option("--name", prompt="Enter your name ", help="This is the name of the person to greet.")
def hello(name):
    click.echo(f"Hello, {name}!")

PRIORITIES ={
    "o" : "Optional",
    "l" : "Low",
    "m" : "Medium",
    "h" : "High",
    "c" : "Critical",
} 





@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Enter the todo name", help="The name of the todo")
@click.option("-d", "--desc", prompt="Describe the todo", help="The description of the todo")
def add_todo(name, desc, priority, todofile):
    """Add a todo to the todo list."""
    filename = todofile if todofile is not None else "todo.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {desc} Priority: {PRIORITIES[priority]}\n")





@click.command()
@click.argument("idx", type=int, required=1)
def delete_todo(idx):
    """Delete a todo from the todo list."""
    with open("todo.txt", "r") as f:
        todo_list = f.readlines()
        todo_list.pop(idx)
    with open("todo.txt", "w") as f:
        f.writelines(todo_list)

@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()), help="List todos")
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    """List todos from the todo list."""
    filename = todofile if todofile is not None else "todo.txt"
    with open(filename, "r") as f:
        todo_list = f.readlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            click.echo(f"{idx +1}: {todo}")
    if priority is not None:
        for idx, todo in enumerate(todo_list):
            if todo.split()[-1] == PRIORITIES[priority]:
                click.echo(f"{idx + 1}: {todo}")

my_commands.add_command(hello)
my_commands.add_command(add_todo)
my_commands.add_command(delete_todo)



if __name__ == "__main__":
    my_commands()