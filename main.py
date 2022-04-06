import PySimpleGUI as sg


control_layout = sg.Column(
    [
        [
            sg.Frame(
                "Blur",
                layout=[[sg.Slider(range=(0, 10), orientation="h", key="-BLUR-")]],
            )
        ],
        [
            sg.Frame(
                "Contrast",
                layout=[[sg.Slider(range=(0, 10), orientation="h", key="-CONTRAST-")]],
            )
        ],
        [
            sg.Checkbox("Emboss", key="-EMBOSS-"),
            sg.Checkbox("Contour", key="-CONTOUR-"),
        ],
        [sg.Checkbox("Flip x", key="-FLIPX-"), sg.Checkbox("Flip y", key="-FLIPY-")],
        [sg.Button("Save image", key="-SAVE-")],
    ]
)
image_layout = sg.Column([[sg.Image("bird.png")]])

layout = [[control_layout, image_layout]]

window = sg.Window("Image Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
