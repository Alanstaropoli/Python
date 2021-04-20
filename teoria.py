import csv
from collections import Counter

with open("bgg_db_1806.csv", "r", encoding = "utf-8") as archivo:
    reader = csv.reader(archivo, delimiter = ',')
    juego_cartas = filter(lambda linea: linea[5] == '1' or linea[5] == '2' and linea[17] == "Card Game", reader)
    print('Lista de juegos de cartas que se juegue con menos de 3 jugadores: ')
    for elemento in juego_cartas:
        print (elemento[3])