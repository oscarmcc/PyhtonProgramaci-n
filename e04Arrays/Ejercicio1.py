"""
Escribe sentencias Python para realizar cada una de las siguientes tareas:

a) Muestra el valor del elemento 6 de un array f.
b) Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
c) Total de los 100 elementos de punto-flotante de un array c.
d) Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos.
e) Calcula y muestra el valor mayor y menor contenidos en un array w de 99 elementos de punto-flotante

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""

import random
f1 = [2, 5, 7, 8, 9, 20, 3, 0, 6]
print(f1[6])

f2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(f2[:5])

sum = 0
c = [random.random() for _ in range(100)]
for i in c:
    sum += i
print(f"La suma en la lista {c} da como resultado {sum}")

a = [n for n in range(12)]
print(a)
copy_a = a.copy()
b = [j for j in range(35)]
copy_a += b
print(copy_a)

w = [random.random()*100 for _ in range(99)]
minimum = maximum = w[0]
for n in w[1:]:
    if n < minimum:
        minimum = n
    elif n > maximum:
        maximum = n
print("El mínimo de los valores es:", minimum)
print("El máximo de los valores es:", maximum)
