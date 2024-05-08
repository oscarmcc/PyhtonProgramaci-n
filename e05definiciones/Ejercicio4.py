"""
Haz un programa que muestre un menú y, usando las funciones anteriores, ejecute las siguientes opciones:

Muestra los números primos que hay entre 1 y 1000.
Muestra los números capicúa que hay entre 1 y 99999.
Muestra la moda de 50 números enteros aleatorios entre 1 y 10.
Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.
Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.
Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.

Author: Óscar Martín-Castaño Carrillo
Date: 9/12/2023
"""

import funciones
import Ejercicio2
import Ejercicio3
import random

funciones.print_title('Dado el siguiente menú decide que ejecutar')
while True:
    funciones.menu(['Muestra los números primos que hay entre 1 y 1000. '
                    'Da True en caso de ser primo; False en caso contrario.',
                    'Muestra los números capicúa que hay entre 1 y 99999.',
                    'Muestra la moda de 50 números enteros aleatorios entre 1 y 10.',
                    'Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.',
                    'Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.',
                    'Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.',
                    'Finalizar el programa'])
    try:
        selector = int(input('Introduce la opción que deseas '))
        match selector:
            case 1:
                start = 1
                finish = 1000
                for n in range(start, finish):
                    print(f"{n} = {Ejercicio2.es_primo(n)}")
            case 2:
                start = 1
                finish = 99999
                for n in range(start, finish):
                    Ejercicio2.es_capicua(n)
            case 3:
                random_start = 1
                random_finish = 10
                finish = 50
                array = [random.randint(random_start, random_finish) for _ in range(finish)]
                print(Ejercicio3.mode(array))
            case 4:
                random_start = 1
                random_finish = 50
                finish = 10
                array = [random.randint(random_start, random_finish) for _ in range(finish)]
                print(Ejercicio3.median(array))
            case 5:
                random_start = 1
                random_finish = 50000
                finish = 1000
                array = [random.randint(random_start, random_finish) for _ in range(finish)]
                print(Ejercicio3.maximun(array))
                print(Ejercicio3.minimun(array))
            case 6:
                random_start = 1
                random_finish = 5
                finish = 10
                array = [random.randint(random_start, random_finish) for _ in range(finish)]
                print(Ejercicio3.variance(array))
            case 7:
                print('Gracias por utilizar el programa, hasta la próxima')
                exit(0)
    except ValueError:
        print('Introduce un valor numérico')
