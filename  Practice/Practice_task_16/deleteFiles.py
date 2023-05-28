import os
import PySimpleGUI as sg


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