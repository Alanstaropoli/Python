import csv
import json
import os
import os.path

path_files = 'db'
tourists_arch = 'trigo.csv'

path_arch = os.path.join(os.getcwd(), path_files)
archivo = open(os.path.join(path_arch, tourists_arch), 'r')
data = csv.reader(archivo, delimiter=',')
header, datos = next(data), list(data)

def check_data(dato, values):
    """
    Devuelve 'True' si el año de los datos a procesar ya se encuentra
    registrado en el archivo JSON, en caso contrario devuelve 'False'
    """

    try:
        with open(os.path.join(path_arch, dato+'.json'), 'r') as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        return False
    else:    
         return any(lista['year'] == values['-YEAR_IN-'] for lista in data)

def start_analysis(dato, values):
    """
    Comprueba el tipo de analisis que se busca
    y llama a la funcion que ejecuta el mismo
    """

    if (dato == 'sown'):
        analysis(dato, values, 1)
    elif (dato == 'harvested'):
        analysis(dato, values, 2)
    elif (dato == 'production'):
        analysis(dato, values, 3)

def analysis(dato, values, i):
    """
    Busca el año ingresado en la lista, toma su dato a procesar depende el tipo que 
    se le indico y llama a la funcion que va a crear un archivo JSON con dichos datos
    """

    flag = False
    for lista in datos:
        if flag == False:
            if lista[0] == values['-YEAR_IN-']:
                create_json(values['-YEAR_IN-'], lista[i], dato)
                flag = True
        else:
            break

def create_json(year, data, type):
    """
    Crea un archivo JSON con los datos recibidos
    """

    analyzed_data = {'year': year, type: data}
    d = [analyzed_data]
    try: 
        with open(os.path.join(path_arch, type+'.json'), 'r') as archivo:
            data_json = json.load(archivo)
        d.extend(data_json)
    except FileNotFoundError:
        print('Archivo no encontrado.')
    with open(os.path.join(path_arch, type+'.json'), 'w') as archivo:
        json.dump(d, archivo)

def check_year(year):
    try:
        if int(year) >= 1923 and int(year) <= 2020:
            return True
    except ValueError:
        return False
    else:
        return False 