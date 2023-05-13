import functions
import PySimpleGUI as sg

main_font = ("Arial", 14)
title = 'My Todo App'
input_label = sg.Text('Enter a todo')
add_button = sg.Button('Add')
exit_button = sg.Button('Exit')


layout = [[input_label],
          [sg.InputText(), add_button],
          [exit_button]]


sg.theme('DarkBlue2')
window = sg.Window(title, layout, font=main_font)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
    elif event == 'Add':
        functions.add_todo(values[0])
    print('You entered ', values[0])

window.close()
