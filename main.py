import functions
import PySimpleGUI as sg

main_font = ("Helvetica", 20)
title = 'My Todo App'

input_label = sg.Text("Enter a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")

add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
exit_button = sg.Button('Exit')

todos_list_box = sg.Listbox(functions.read_todos(),
                            size=(44, len(functions.read_todos())),
                            enable_events=True,
                            key="todos-list"
                            )

layout = [[input_label],
          [input_box, add_button],
          [todos_list_box, edit_button],
          [exit_button]]

sg.theme('DarkBlue2')
window = sg.Window(title, layout, font=main_font)


def refresh_window():
    window['todos-list'].update(values=functions.read_todos())
    window['todo'].update(value="")


while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    if event == 'Add':
        functions.add_todo(values["todo"])
        refresh_window()

    elif event == 'Edit':
        selected_todo = values["todos-list"][0]
        selected_index = functions.read_todos().index(selected_todo)
        functions.edit_todo(selected_index, values['todo'])
        refresh_window()

    elif event == "todos-list":
        selected_todo = values["todos-list"][0]
        window['todo'].update(value=selected_todo.strip('\n'))

    elif event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
    print('You entered ', values["todo"])

window.close()
