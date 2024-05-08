"""
Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los elementos de ese array,
es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra
en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido del array.

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""
TOTAL_NUMBERS = 15

print('Programa que pide 15 números y los pasa a una posición más en la lista,'
      ' siendo el último número pasado al primer índice de la lista')

numbers = []

for i in range(TOTAL_NUMBERS):
    numbers.append(int(input('Introduce un número entero por favor ')))
print("\nLa lista original es:", numbers)

aux = numbers[-1]
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]
numbers[0] = aux
print("\nLa lista rotada una posición a la derecha es:", numbers)
