import PySimpleGUI as sg

def build():
    """
    Crea la ventana del menu de analisis del turismo en Argentina
    """

    layout = [
        [sg.Button('Transporte mas utilizado por los turistas', size=(30, 2), key='-TRANSPORT-')],
        [sg.Button('Pais origen que mas visito Argentina', size=(30, 2), key='-COUNTRY-')],
        [sg.Button('Salir', size=(30, 2), key="-EXIT-")]
    ]

    tourism_window = sg.Window('Turismo receptivo en Argentina', use_default_focus=False).Layout(layout)

    return tourism_window