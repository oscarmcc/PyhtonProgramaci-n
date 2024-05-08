"""
Realiza un programa que calcule la estatura media, mínima y máxima en centímetros de personas de diferentes países.
El array que contiene los nombres de los países es el siguiente:

paises = [“España”, “Rusia”, “Japón”, “Australia”]

Los datos sobre las estaturas se deben simular mediante un array de 4 filas por 10 columnas con números aleatorios
generados al azar entre 140 y 210. Los decimales de la media se pueden despreciar. Los nombres de los países se deben
mostrar utilizando el array de países (no se pueden escribir directamente).

Author: Óscar Martín-Castaño Carrillo
Date: 22/11/2023
"""
import random

print('Programa que calcula la estatura '
      'media, mínima y máxima en centímetros de los países de España, Rusia, Japón y Australia')

COLUMNS = 10
MIN_HEIGHT = 140
MAX_HEIGHT = 210
LEN_COUNTRY_NAME = 10
LEN_HEIGHT = 3


def mean_height_per_country():
    mean_height = 0
    for height in country_heights:
        mean_height += height
    mean_height /= COLUMNS
    return mean_height


def maximum_height_per_country():
    max_height = MIN_HEIGHT
    for column in range(COLUMNS):
        if max_height < country_heights[column]:
            max_height = country_heights[column]
    return max_height


def minimum_height_per_country():
    min_height = MAX_HEIGHT
    for column in range(COLUMNS):
        if min_height > country_heights[column]:
            min_height = country_heights[column]
    return min_height


countries = ["España", "Rusia", "Japón", "Australia"]
heights_by_country = [[0] * COLUMNS for _ in range(len(countries))]

for country in heights_by_country:
    for i in range(len(country)):
        country[i] = random.randint(MIN_HEIGHT, MAX_HEIGHT)

print(" "*(LEN_COUNTRY_NAME+3) + " "*COLUMNS*(LEN_HEIGHT+1) + "MED MIN MAX")
for row in range(len(countries)):
    print(f"{countries[row]+':':{LEN_COUNTRY_NAME}} ", end="")
    country_heights = heights_by_country[row]
    for height in country_heights:
        print(f"{height:{LEN_HEIGHT}} ", end="")
    print(f"| {round(mean_height_per_country()):{LEN_HEIGHT}} "
          f"{minimum_height_per_country():{LEN_HEIGHT}} {maximum_height_per_country():{LEN_HEIGHT}}")
