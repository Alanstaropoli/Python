string = '''
'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
 '''

string2 = '''
 81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
 '''
 
string3 = '''
 30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
 '''

def crear_lista():

    """ Esta funcion crea una lista y la devuelve con el nombre de los alumnos y sus notas totales. """
    
    nombres = string.split()
    evaluacion1 = string2.split()
    evaluacion2 = string3.split()

    # Le saco las "'" y las "," al contenido de las listas y paso los strings con las notas a int.
    for elemento in nombres:
        i = nombres.index(elemento)
        for car in elemento:
            if not car.isalpha():
                elemento = elemento.replace(car, '')
        nombres[i] = elemento
    for elemento in evaluacion1:
        i = evaluacion1.index(elemento)
        for num in elemento:
            if not num.isdigit():
                elemento = elemento.replace(num, ' ')
        evaluacion1[i] = int(elemento)
    for elemento in evaluacion2:
        i = evaluacion2.index(elemento)
        for num in elemento:
            if not num.isdigit():
                elemento = elemento.replace(num, ' ')
        evaluacion2[i] = int(elemento)

    # Creo un zip para unificar las notas de las evaluaciones.
    notas = zip(evaluacion1, evaluacion2)
    total_notas = []
    for estructura in notas:
        total_notas.append(estructura[0]+estructura[1])

    notas = list(zip(nombres, total_notas))
    return notas

def calcular_promedio(notas):
    
    """ Esta funcion calcula y devuelve el promedio de las notas totales de los alumnos. """
   
    suma = 0
    for nota in notas:
        suma += nota[1]
    promedio = suma/len(notas)
    print(f'El promedio de las notas totales de los alumnos es de {int(promedio)}.')
    return promedio

def notas_bajas(promedio):
    
    """ Esta funcion imprime el listado de los alumnos con peores notas. """

    print('Listado de alumnos con notas menores al promedio: ')
    for estructura in notas:
        if estructura[1] < promedio:
            print(f'{estructura[0]}.')

notas = crear_lista()
promedio = calcular_promedio(notas)
notas_bajas(promedio)