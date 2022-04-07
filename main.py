import PySimpleGUI as sg
from PIL import Image


def update_image(
    original: Image,
    blur: sg.Slider,
    contrast: sg.Slider,
    emboss: sg.Checkbox,
    contour: sg.Checkbox,
    flipx: sg.Checkbox,
    flipy: sg.Checkbox,
):
    print(original)


image_path = "bird.png"
original = Image.open(image_path)

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
image_layout = sg.Column([[sg.Image(image_path)]])

layout = [[control_layout, image_layout]]

window = sg.Window("Image Editor", layout)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    update_image(
        original,
        values["-BLUR-"],
        values["-CONTRAST-"],
        values["-EMBOSS-"],
        values["-CONTOUR-"],
        values["-FLIPX-"],
        values["-FLIPY-"],
    )

window.close()
