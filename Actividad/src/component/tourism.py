import PySimpleGUI as sg
from src.windows import tourism
from src.handlers import tourism as tourism_handler

def start():
    """
    Ejecuta la ventana del menu de analisis del turismo en Argentina
    """
    tourism_window = loop()
    tourism_window.close()

def loop():
    """
    Loop de la ventana del menu de analisis del turismo en Argentina
    """

    tourism_window = tourism.build()

    while True:
        event, _values = tourism_window.read()
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            break
        if event == '-TRANSPORT-':
            tourism_handler.transport_search()
            sg.popup('La operacion se ha realizado con exito!')
        if event == '-COUNTRY-':
            tourism_handler.country_search()
            sg.popup('La operacion se ha realizado con exito!')

    return tourism_window