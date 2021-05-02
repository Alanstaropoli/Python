import PySimpleGUI as sg
from src.component import insert
from src.windows import trigo

def start():
    """
    Ejecuta la ventana del menu de analisis del trigo en Argentina
    """
    trigo_window = loop()
    trigo_window.close()

def loop():
    """
    Loop de la ventana del menu de analisis del trigo en Argentina
    """

    trigo_window = trigo.build()

    while True:
        event, _values = trigo_window.read()
        if event in (sg.WIN_CLOSED, '-EXIT-'):
            break
        if event == '-SOWN-':
            insert.start('sown')
        if event == '-HARVESTED-':
            insert.start('harvested')
        if event == '-PRODUCTION-':
            insert.start('production')
    
    return trigo_window