import PySimpleGUI as sg
from src.windows import insert
from src.handlers import insert as insert_handler

def start(dato):
    """
    Ejecuta la ventana de acceso del año sobre el cual se ejecute el analisis
    """
    yearIn_window = loop(dato)
    yearIn_window.close()

def loop(dato):
    """
    Loop de la ventana la ventana de acceso del año sobre el cual se ejecute el analisis
    """

    yearIn_window = insert.build()

    while True:
        event, values = yearIn_window.read()
        if event in (sg.WIN_CLOSED, '-CANCEL-'):
            break
        if event == '-CONFIRM-':
            if values['-YEAR_IN-'] == '':
                sg.popup_error('Debes rellenar los campos')
            elif insert_handler.check_year(values['-YEAR_IN-']):
                if insert_handler.check_data(dato, values):
                    sg.popup('El dato ya ha sido procesado')
                else:
                    insert_handler.start_analysis(dato, values)
                    yearIn_window.hide()
                    sg.popup('La operacion se ha realizado con exito!')
                    break
            else:
                sg.popup_error('El dato ingresado no cumple con los requisitos')
    
    return yearIn_window