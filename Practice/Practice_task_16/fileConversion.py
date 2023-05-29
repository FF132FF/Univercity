import os
import PySimpleGUI as sg
from docx2pdf import convert
from pdf2docx import parse
from PIL import Image

def fileSearch(dir, format):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            if format.__contains__(file.split('.')[-1]):
                files.append(file)

    return files


def fileConversation(file):
    fileFormat = file.split('.')[-1]

    if fileFormat == "docx" or fileFormat == "doc":
        convertedFile = file.replace(fileFormat, "pdf")

        try:
            convert(file, convertedFile)
        except:
            sg.popup(f"Unable to convert file {file} to pdf")

    elif fileFormat == "pdf":
        convertedFile = file.replace(fileFormat, "docx")

        try:
            convert(file, convertedFile)
        except:
            sg.popup(f"Unable to convert file {file} to docx")
    else:
        layout = [
            [sg.Text("Select compression options in percent (%):"), sg.Input(key="quality", size=(5, 1))],
            [sg.Button("Compress the file"), sg.Button("Cancel")]
        ]

        window = sg.Window("File compression", layout)

        while True:
            event, values = window.read()

            if event == "Cancel" or event == sg.WINDOW_CLOSED:
                break

            if event == "Compress the file":
                quality = values["quality"]

                try:
                    imgPath = file
                    imgFile = Image.open(imgPath)
                    imgFile.save(file, quality=quality)
                    break
                except:
                    sg.popup(f"Unable to compress file: {file}")

        window.close()

def change(dir, format):
    files = fileSearch(dir, format)
    if len(files) == 0:
        sg.popup(f"There are no files with the format {', '.join(format)} in the selected directory")
        return

    layout = [[sg.Text("Select files to conversion: ")],
              [sg.Listbox(values=files, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(40, 10), key="files")],
              [sg.Button("Convert files"), sg.Button("Cancel")]]

    window = sg.Window("File converter", layout)

    while True:
        event, values = window.read()

        if event in (None, "Cancel"):
            break

        if event == "Convert files":
            selectedFiles = values["files"]
            for file in selectedFiles:
                fileConversation(os.path.join(dir, file))

            sg.popup("Conversion completed")
            break

    window.close()
