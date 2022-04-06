import PySimpleGUI as sg


layout = [[]]

window = sg.Window("Image Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
