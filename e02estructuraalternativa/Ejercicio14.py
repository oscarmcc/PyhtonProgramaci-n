"""
La asociación de vinicultores tiene como política fijar un precio
inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en
tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un
solo tipo y tamaño, se requiere determinar cuánto recibirá un productor
por la uva que entrega en un embarque, considerando lo siguiente: si es
de tipo A, se le cargan 20 céntimos al precio inicial cuando es de
tamaño 1; y 30 céntimos si es de tamaño 2.
Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para saber la ganancia de un vinicultor')

sale = float(input('El precio inicial por kilo de uba es '))
type = str(input('Es de tipo A o B '))
size = str(input('Es del tamaño 1 o 2 '))

add = type + size

match add:
    case 'A1':
        final = sale + 0.20
        print('El precio sería de', final)
    case 'A2':
        final = sale + 0.30
        print('El precio sería de', final)
    case 'B1':
        final = sale - 0.30
        print('El precio sería de', final)
    case 'B2':
        final = sale - 0.50
        print('El precio sería de', final)
