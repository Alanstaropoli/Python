import csv
import json
import os
import os.path
from collections import Counter

path_files = 'db'
tourists_arch = 'turistas.csv'

path_arch = os.path.join(os.getcwd(), path_files)
archivo = open(os.path.join(path_arch, tourists_arch), 'r')
data = csv.reader(archivo, delimiter=',')
header, datos = next(data), list(data)

def transport_search():
    """
    Busca en la lista el transporte que mas se utilizo por los 
    turistas y registra dicha informacion en un archivo JSON
    """
    
    transportes = {}
    for lista in datos:
        if lista[1] in transportes.keys():
            transportes[lista[1]] += int(float(lista[3]))
        else:
            transportes[lista[1]] = int(float(lista[3]))
    max = Counter(transportes).most_common(1)
    create_json(max[0], 'transport')

def country_search():
    """
    Busca en la lista el pais origen de los turistas que mas visito
    Argentina y registra dicha informacion en un archivo JSON
    """

    paises = {}
    for lista in datos:
        if lista[2] in paises.keys():
            paises[lista[2]] += int(float(lista[3]))
        else:
            paises[lista[2]] = int(float(lista[3]))
    max = Counter(paises).most_common(1)
    create_json(max[0], 'country')

def create_json(data, type):
    """
    Crea un archivo JSON con los datos recibidos
    """

    analyzed_data = {type: data[0], 'tourists': data[1]}
    d = [analyzed_data]
    with open(os.path.join(path_arch, type+'.json'), 'w') as archivo:
        json.dump(d, archivo)
