import PySimpleGUI as sg
import os
from docx2pdf import convert
from PIL import Image

def changeDirectory():
    layout = [
        [sg.Text("Current location:"), sg.Text(os.getcwd(), key="dir")],
        [sg.Text("To search and select a directory, click on: "), sg.FolderBrowse("Search")],
        [sg.Text("To go to the selected directory, click on :"), sg.Button("Go to the selected directory")],
        [sg.Text("To exit, click on: "), sg.Button("Exit")]
    ]

    # Create the window
    window = sg.Window("Directory change", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Go to the selected directory":
            if values["Search"] is not None:
                newDirectory = values["Search"]
                os.chdir(newDirectory)
                sg.popup(f"Current directory changed to: {newDirectory}")
                break
            else:
                sg.popup("Directory is not changed")

    window.close()
    return os.getcwd()


def deleteMenu():
    layout = [
        [sg.Text("Select type of deletion")],
        [sg.Radio("Delete files starting with a substring", "RADIO1", default=True, key="option1")],
        [sg.Radio("Delete files ending with a substring", "RADIO1", key="option2")],
        [sg.Radio("Delete files containing a substring", "RADIO1", key="option3")],
        [sg.Radio("Delete files with a substring extension", "RADIO1", key="option4")],
        [sg.Button("Delete"), sg.Button("Cancel")]
    ]

    window = sg.Window("Deleting files", layout)

    while True:
        event, values = window.read()

        if event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            return None

        if event == "Delete":
            if values["option1"]:
                window.close()
                return 1
            elif values["option2"]:
                window.close()
                return 2
            elif values["option3"]:
                window.close()
                return 3
            elif values["option4"]:
                window.close()
                return 4


def delete(catalog):
    deleteOption = deleteMenu()

    if deleteOption is None:
        return

    substring = sg.popup_get_text("Enter a substring: ")

    files = []
    for file in os.listdir(catalog):
        if os.path.isfile(file):
            files.append(file)

    deleteFileList = []

    if deleteOption == 1:
        for file in files:
            if file[0:len(substring)] == substring:
                deleteFileList.append(file)

    if deleteOption == 2:
        for file in files:
            filename = file.split('.')[0]
            if filename[-len(substring):] == substring:
                deleteFileList.append(file)

    if deleteOption == 3:
        for file in files:
            filename = file.split('.')[0]
            if filename.__contains__(substring):
                deleteFileList.append(file)

    if deleteOption == 4:
        for file in files:
            format = file.split('.')[1]
            if format == substring:
                deleteFileList.append(file)

    if len(deleteFileList) == 0:
        sg.popup("Files to delete not found")
        return

    layout = [
        [sg.Text("Are you sure that you want to delete the selected files? ")],
        [sg.Listbox(deleteFileList, size=(50, len(deleteFileList)))],
        [sg.Button("Yes"), sg.Button("No")]
    ]

    window = sg.Window("Deleting files", layout)

    while True:
        event, values = window.read()

        if event == "No" or event == sg.WIN_CLOSED:
            window.close()
            break

        if event == "Yes":
            for file in deleteFileList:
                os.remove(file)
            sg.popup("Files deleted successfully")
            window.close()
            break

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