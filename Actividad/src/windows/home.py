import PySimpleGUI as sg

def build():
    """
    Crea la ventana del menu principal del programa
    """

    layout = [
        [sg.Text('¿Que datos analizamos?', justification='center')], 
        [sg.Button('Trigo en Argentina: Siembra, cosecha, produccion.', size=(30, 2), key='-TRIGO-')],
        [sg.Button('Turismo receptivo en Argentina', size=(30, 2), key='-TOURISM-')],
        [sg.Button('Salir', size=(30, 2), key="-EXIT-")]
    ]

    home_window = sg.Window('Python - Teoria', element_justification='center', use_default_focus=False).Layout(layout)

    return home_window