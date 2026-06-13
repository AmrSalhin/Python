FILEPATH = "ToDo.txt"

def get_todos(file_path=FILEPATH):
    """Read todos from file and return a list"""
    todos_local = []
    try:
        with open(file_path, "r") as f:
            todos_local =f.readlines()
    except FileNotFoundError:
        pass
    return todos_local

def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list to a text file. """
    with open(file_path, "w") as file:
        file.writelines(todos_arg)