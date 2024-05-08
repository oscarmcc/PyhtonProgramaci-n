"""
Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar
los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden
tener longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger todos los que
quedan del otro.

Ejemplos:

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]

Author: Óscar Martín-Castaño Carrillo
Date: 14/12/2023
"""

import funciones
import random


def create_array():
    array = [random.randint(1, 10) for _ in range(random.randint(1, 10))]
    return array


def combine_arrays():
    combination = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if i < len(a):
            combination.append(a[i])
            i += 1
        if j < len(b):
            combination.append(b[j])
            j += 1
    return combination


def main():
    funciones.print_title('Programa que mezcla dos listas de números alternando los elementos de cada lista')
    print(f"la combinación del array {a} y del array {b} es {combine_arrays()}")


if __name__ == '__main__':
    a = create_array()
    b = create_array()
    main()
