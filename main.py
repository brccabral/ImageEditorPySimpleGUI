import PySimpleGUI as sg

control_layout = sg.Column([[]])
image_layout = sg.Column([[sg.Image("bird.png")]])

layout = [[image_layout]]

window = sg.Window("Image Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
