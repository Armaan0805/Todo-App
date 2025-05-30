FILEPATH ="todos.txt"


def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of to-do items, stripped and cleaned."""
    with open(filepath, "r") as file:
        todos = file.readlines()
    # Strip each line and remove empty ones
    return [todo.strip() for todo in todos if todo.strip()]



def  write_todos(todos_arg,filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
