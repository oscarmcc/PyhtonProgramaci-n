"""
Title: Números perfectos

Se dice que un número es “perfecto” si es igual a la suma de todos sus divisores excluido él mismo.
Por ejemplo, 28 es un número perfecto, pues sus divisores (excepto él mismo) son 1, 2, 4, 7 y 14,
que suman 28.

Author: Óscar Martín-Castaño Carrillo
Date: 10/11/2023
"""
import sys

print('Programa que nos indica si un número es perfecto,'
      ' además nos dice cuantas iteraciones se han realizado y cuantos números son perfectos')

while True:
    is_perfect = 0
    iterations = 0
    while True:
        number_perfect = int(input('Dame un número entero positivo para indicar si es perfecto o no '))
        while number_perfect < 0:
            print(f"Error; Recuerda el número introducido debe ser positivo, es decir mayor que cero", file=sys.stderr)
            number_perfect = int(input('Vuelve a introducir un número que sea positivo '))
        divisor = 1
        perfect = 0
        for i in range(1, number_perfect):
            rest = number_perfect % divisor
            if rest == 0:
                perfect += divisor
            if perfect == number_perfect:
                is_perfect += 1

                print(f"El número {number_perfect} es perfecto")
                break
            divisor += 1
        while True:
            answer = input('¿Deseas continuar comprobando números? Debes responder con S/N ').upper()
            while answer != 'S' and answer != 'N':
                print(f"Error; Recuerda solo puedes responder con S o N", file=sys.stderr)
                answer = input('Vuelve a responder la pregunta por favor ').upper()
            if answer == 'S' or answer == 'N':
                break
        iterations += 1
        if answer == 'N':
            print(f"En este programa has realizado {iterations} iteraciones y "
                  f"has encontrado {is_perfect} números perfectos")
            exit(0)
