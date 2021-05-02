import PySimpleGUI as sg
from src.component import trigo
from src.component import tourism
from src.windows import home

def start():
    """
    Ejecuta la ventana principal del programa
    """
    home_window = loop()
    home_window.close()

def loop():
    """
    Loop de la ventana principal del pograma
    """

    home_window = home.build()

    while True:
        event, _values = home_window.read()
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            break
        if event == '-TRIGO-':
            home_window.hide()
            trigo.start()
            home_window.un_hide()
        if event == '-TOURISM-':
            home_window.hide()
            tourism.start()
            home_window.un_hide()
    
    return home_window