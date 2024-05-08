"""
Define tres arrays de 20 números enteros cada uno, con nombres numero, cuadrado y cubo. Carga el array numero con
valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el
array numero. En el array cubo se deben almacenar los cubos de los valores que hay en numero. A continuación, muestra
el contenido de los tres arrays dispuesto en tres columnas.

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""
import random
print('Programa que de una lista saca dos una con el cuadrado de la primera y la otra con el cubo de la primera')

numero = [random.randint(1, 100) for _ in range(21)]
print(f"La lista numero es: {numero}\n")

cuadrado = [n ** 2 for n in numero]
print(f"El cuadrado de los valores en la lista numero es: {cuadrado}\n")

cubo = [c ** 3 for c in numero]
print(f"El cubo de cada valor de la lista numero es: {cubo}")

print(f"\nComo resultado tenemos esta tabla donde la primera columna es la lista original, "
      f"la segunda los cuadrados y la tercera los cubos\n")
for i in range(21):
    print(f"{numero[i]:3d}|{cuadrado[i]:5d}|{cubo[i]:7d}")
