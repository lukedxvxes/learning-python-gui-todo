
def get_user_action():
    action = input("Type add [todo], show, edit [todo num], complete [todo num] or exit: ")
    action = action.strip()
    return action


def format_string(string):
    return string + '\n'


def read_todos(filepath='todos.txt'):
    # Using with-context-manager, removes need to manually close the file
    with open(filepath, 'r') as file:
        todo_list = file.readlines()
        return todo_list


def write_todos(todos_list, filepath='todos.txt'):
    # Using with-context-manager, removes need to manually close the file
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


def add_todo(action):
    todo = format_string(action[4:])
    all_todos = read_todos()
    all_todos.append(todo)
    write_todos(all_todos)


def edit_todo(action):
    edit_item = int(action[5:])
    todos = read_todos()
    edit_item = edit_item - 1
    todos[edit_item] = format_string(input("update " + todos[edit_item] + " to be: "))
    write_todos(todos)


def complete_todo(action):
    todos = read_todos()
    completed_item = action[9:]
    if completed_item == 'all':
        todos = []
    else:
        completed_item = int(action[9:])
        todos.pop(completed_item - 1)
    write_todos(todos)


def show_todos():
    all_todos = read_todos()
    # example of inline for-loop or list comprehension
    # for each item in todos, return item.strip
    formatted_todos = [item.strip('\n') for item in all_todos]

    for index, item in enumerate(formatted_todos):
        index = index + 1
        formatted_str = f"{index}-{item}"
        print(formatted_str)

