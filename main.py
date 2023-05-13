import functions
import PySimpleGUI as sg
import time

main_font = ("Helvetica", 20)
title = 'My Todo App'
clock = sg.Text("", key="clock", font=("Helvetica", 14))

input_label = sg.Text("Enter a todo",font=("Helvetica", 32))
input_box = sg.InputText(tooltip="Enter a todo", key="todo")


add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
exit_button = sg.Button('Exit')
complete_button = sg.Button('Complete')

todos_list_box = sg.Listbox(functions.read_todos(),
                            size=(44, len(functions.read_todos())),
                            enable_events=True,
                            key="todos-list"
                            )

layout = [[clock],
          [input_label],
          [input_box, add_button],
          [todos_list_box, edit_button, complete_button],
          [exit_button]]

sg.theme('DarkBlue2')
window = sg.Window(title, layout, font=main_font)


while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == 'Add':
        functions.add_todo(values["todo"])
        functions.refresh_window(window)

    elif event == 'Edit':
        try:
            selected_todo = values["todos-list"][0]
            selected_index = functions.read_todos().index(selected_todo)
            functions.edit_todo(selected_index, values['todo'])
            functions.refresh_window(window)
        except IndexError:
            sg.popup("select something to edit", font=("Helvetica", 20))

    elif event == "todos-list":
        selected_todo = values["todos-list"][0]
        window['todo'].update(value=selected_todo.strip('\n'))

    elif event == 'Complete':
        try:
            selected_todo = values["todos-list"][0]
            selected_index = functions.read_todos().index(selected_todo)
            functions.complete_todo(selected_index)
            functions.refresh_window(window)
        except IndexError:
            sg.popup("select something to complete", font=("Helvetica", 20))

    elif event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break

window.close()
