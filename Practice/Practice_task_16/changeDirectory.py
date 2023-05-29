import os
import PySimpleGUI as sg


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
