"""
Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las
palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""
COUNT = 10
print('Programa que pide 10 números y nos indica cuál es el máximo y cuál es el mínimo')

i = 0
list_to_add = []

while i < COUNT:
    number_to_add = float(input('Dame el número que quieras '))
    list_to_add.append(number_to_add)
    i += 1

list_to_add.sort()
max = list_to_add[0]
min = list_to_add[0]
for numero in list_to_add:
    if numero > max:
        max = numero
    elif numero < min:
        min = numero

for numero in list_to_add:
    if numero == max:
        print(f"{numero} máximo")
    elif numero == min:
        print(f"{numero} mínimo")
    else:
        print(numero)
