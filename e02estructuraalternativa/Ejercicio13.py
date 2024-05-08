"""
Escribir un programa que calcule el desglose mínimo en billetes y
monedas de una cantidad exacta de euros.
Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.

Por ejemplo, si deseamos conocer el desglose de 434€, el programa mostrará por pantalla el siguiente resultado:

2 billetes de 200 euros.
1 billete de 20 euros.
1 billete de 10 euros.
2 monedas de 2 euros.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para calcular el desglose de una cantidad de dinero')

money = int(input('Dame la cantidad de dinero que quieras desglosar '))

if money >= 500:
    final = money // 500
    print(final, 'billetes de 500€')
    money = money % 500
if money >= 200:
    final = money // 200
    print(final, 'billetes de 200€')
    money = money % 200
if money >= 100:
    final = money // 100
    print(final, 'billetes de 100€')
    money = money % 100
if money >= 50:
    final = money // 50
    print(final, 'billetes de 50€')
    money = money % 50
if money >= 20:
    final = money // 20
    print(final, 'billetes de 20€')
    money = money % 20
if money >= 10:
    final = money // 10
    print(final, 'billetes de 10€')
    money = money % 10
if money >= 5:
    final = money // 5
    print(final, 'billetes de 5€')
    money = money % 5
if money >= 2:
    final = money // 2
    print(final, 'monedas de 2€')
    money = money % 2
if money == 1:
    final = money // 1
    print(final, 'monedas de 1€')
