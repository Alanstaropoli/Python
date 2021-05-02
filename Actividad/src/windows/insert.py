import PySimpleGUI as sg

def build():
    """
    Crea la ventana de acceso del año sobre el cual se ejecute el analisis
    """

    layout = [
        [sg.Text('Debe ingresar el año del dato que quiere recibir (1923-2020): ')], 
        [sg.Input(key='-YEAR_IN-')],
        [sg.Button('Confirmar', key='-CONFIRM-'), sg.Button('Cancelar', key='-CANCEL-')]
    ]

    yearIn_window = sg.Window(' ').Layout(layout)

    return yearIn_window