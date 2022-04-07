import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from PIL.Image import Image as Im
from io import BytesIO


def update_image(
    original: Im,
    blur: sg.Slider,
    contrast: sg.Slider,
    emboss: sg.Checkbox,
    contour: sg.Checkbox,
    flipx: sg.Checkbox,
    flipy: sg.Checkbox,
):
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())

    if contour:
        image = image.filter(ImageFilter.CONTOUR())

    if flipx:
        image = ImageOps.mirror(image)

    if flipy:
        image = ImageOps.flip(image)

    # convert to bytes
    image_bytes = BytesIO()
    image.save(image_bytes, format="PNG")

    # update GUI
    window["-IMAGE-"].update(data=image_bytes.getvalue())

    return image


image_path = sg.popup_get_file("Open", no_window=True)
if not image_path:
    raise Exception("No image selected.")

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
image_layout = sg.Column([[sg.Image(image_path, key="-IMAGE-")]])

layout = [[control_layout, image_layout]]

window = sg.Window("Image Editor", layout)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    image = update_image(
        original,
        values["-BLUR-"],
        values["-CONTRAST-"],
        values["-EMBOSS-"],
        values["-CONTOUR-"],
        values["-FLIPX-"],
        values["-FLIPY-"],
    )

    if event == "-SAVE-":
        save_path = sg.popup_get_file("Save", save_as=True, no_window=True)
        if save_path:
            image.save(save_path)

window.close()
