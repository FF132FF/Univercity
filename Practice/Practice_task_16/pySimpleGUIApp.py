from changeDirectory import *
from fileConversion import *
from deleteFiles import *
import PySimpleGUI as sg
import os

layout = [
    [sg.Text("Choose an action: ")],
    [sg.Radio("Change working directory", "action", default=True, key="changeDirectory")],
    [sg.Radio("Convert PDF to Docx", "action", key="pdfToDocx")],
    [sg.Radio("Convert Doc, Docx to PDF", "action", key="docToPdf")],
    [sg.Radio("Compress image", "action", key="imgCompress")],
    [sg.Radio("Delete group of files", "action", key="deleteFiles")],
    [sg.Button("Execute", key="execute"), sg.Button("Exit", key="exit")]
]

window = sg.Window("File manager").Layout(layout)

catalog = os.getcwd()

while True:
    event, values = window.Read()
    if event is None or event == "exit":
        break
    if event == "execute":
        if values["changeDirectory"]:
            catalog = changeDirectory()
            pass

        elif values["pdfToDocx"]:
            change(catalog, ["pdf"])
            pass

        elif values["docToPdf"]:
            change(catalog, ["doc", "docx"])
            pass

        elif values["imgCompress"]:
            change(catalog, ["img", "png", "jpg", "jpeg", "bmp"])
            pass

        elif values["deleteFiles"]:
            delete(catalog)
            pass

window.Close()