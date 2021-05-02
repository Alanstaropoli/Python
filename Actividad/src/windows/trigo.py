import PySimpleGUI as sg

def build():
    """
    Crea la ventana del menu de analisis del trigo en Argentina
    """

    layout = [
        [sg.Button('Hectareas sembradas', size=(30, 2), key='-SOWN-')],
        [sg.Button('Hectareas cosechadas', size=(30, 2), key='-HARVESTED-')],
        [sg.Button('Produccion anual de trigo en toneladas', size=(30, 2), key='-PRODUCTION-')],
        [sg.Button('Salir', size=(30, 2), key="-EXIT-")]
    ]

    trigo_window = sg.Window('Trigo en Argentina: Serie historica', use_default_focus=False).Layout(layout)

    return trigo_window