"""
Crea una biblioteca de funciones (statistics) dentro de un paquete (util) que contenga las siguientes funciones:

maximum
recibiendo como parámetro un array de enteros
recibiendo un conjunto de parámetros enteros
minimum
recibiendo como parámetro un array de enteros 
recibiendo un conjunto de parámetros enteros
mean
recibiendo como parámetro un array de enteros 
recibiendo un conjunto de parámetros enteros
variance
recibiendo como parámetro un array de enteros y haciendo uso de la función anterior
recibiendo un conjunto de parámetros enteros y haciendo uso de la función anterior
median
recibiendo como parámetro un array de enteros 
recibiendo un conjunto de parámetros enteros
mode
recibiendo como parámetro un array de enteros 
recibiendo un conjunto de parámetros enteros
devuelve un array de enteros (puede haber varias modas)

Author: Óscar Martín-Castaño Carrillo
Date: 8/12/2023
"""

import funciones

funciones.print_title('Programa que tiene funciones aceptando una lista o diferentes parámetros, las funciones son de'
                      'máximo, mínimo, media, mediana, varianza y el modo')


def maximun(*number):
    if len(number) == 1 and isinstance(number[0], (list, tuple)):
        number = number[0]
    max_number = number[0]
    for i in number:
        if max_number < i:
            max_number = i
    return max_number


def minimun(*number):
    if len(number) == 1 and isinstance(number[0], (list, tuple)):
        number = number[0]
    min_number = number[0]
    for i in number:
        if min_number > i:
            min_number = i
    return min_number


def mean_number(*number):
    if len(number) == 1 and isinstance(number[0], (list, tuple)):
        number = number[0]
    count = 0
    number_to_split = 0
    for i in range(len(number)):
        count += 1
    for n in number:
        number_to_split += n
    mean = number_to_split / count
    return mean


def variance(*number):
    if len(number) == 1 and isinstance(number[0], (list, tuple)):
        number = number[0]
    mean = mean_number(number)
    count = 0
    sum = 0
    for n in number:
        sum += (n - mean) ** 2
        count += 1
    final_variance = sum / count
    return final_variance


def median(*number):
    if len(number) == 1 and isinstance(number[0], (list, tuple)):
        number = number[0]
    len_number = len(number)
    order_number = sorted(number)
    if len_number % 2 == 1:
        median_number = order_number[len_number // 2]
    else:
        median_number = (order_number[len_number // 2 - 1] + order_number[len_number // 2]) / 2
    return median_number


def mode(*number):
    if len(number) == 1 and isinstance(number[0], (list, tuple)):
        number = number[0]
    for n in number:
        if not isinstance(n, int):
            raise TypeError(f"Encontrado {n} que no es int")

    individual_numbers, frequency_numbers = [], []
    for n in number:
        if n in individual_numbers:
            index_number = individual_numbers.index(n)
            frequency_numbers[index_number] += 1
        else:
            individual_numbers.append(n)
            frequency_numbers.append(1)
    max_frequencies = max(frequency_numbers)
    modes = []
    for n in range(len(individual_numbers)):
        if frequency_numbers[n] == max_frequencies:
            modes.append(individual_numbers[n])
    return tuple(modes)


if __name__ == '__main__':
    print(maximun(1, 3, 4))
    print(maximun([1, 2, 4, 5, 3, 2]))
    print(minimun(1, 2, 3, 4, ))
    print(minimun([2, 3, 1, 5, 3]))
    print(mean_number(2, 3, 43, 2, ))
    print(mean_number([2, 3, 4, 5, 6, 4, 3]))
    print(variance(3, 4, 13, 6, 2, 4))
    print(variance([2, 3, 4, 5, 6]))
    print(median(2, 4, 3, 2, 14, 5))
    print(median([1, 2, 3, 4, 5]))
    array = [2, 4, 5, 3, 5, 5, 2, 2]
    print(mode(array))
    print(mode(1, 3, 4, 2, 5, 3, 5, 2, 3))
