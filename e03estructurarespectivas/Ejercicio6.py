"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia ni la función.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""

print('Programa para sacar el resultado de la potencia')

i = 1

BASE = int(input('Dame la base del número '))
EXPONENT = int(input('Dame el exponente del número '))
NUM = BASE
while i < EXPONENT:
    NUM *= BASE
    i += 1

print(f"La solución de la base {BASE} y el exponente {EXPONENT} es {NUM}")
