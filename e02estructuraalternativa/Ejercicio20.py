"""
Una compañía de transporte internacional tiene servicio en algunos
países de América del Norte, América Central, América del Sur,
Europa y Asia. El costo por el servicio de transporte se basa en
el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

ZONA	UBICACIÓN	COSTO/GRAMO
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros
Parte de su política implica que los paquetes con un peso superior
a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
Realice un algoritmo para determinar el cobro por la entrega de un
paquete o, en su caso, el rechazo de la entrega.

Author: Óscar Martín-Castaño Carrillo
Date: 22/10/2023
"""

print('Programa para saber cuánto cuesta el envío e nuestro paquete')

print('Menú de zonas')
print('--------------')
print('1. América del Norte')
print('2. América Central')
print('3. América del Sur')
print('4. Europa')
print('5. Asia')


zone = int(input('Por favor indica el número de la zona del servicio '))
size = int(input('Indica el peso del paquete en gramos '))

if size > 5000:
    print('El paquete supera el peso de 5 kg por lo que no puede ser enviado')

match zone:
    case 1:
        price = 24.00 * size
    case 2:
        price = 20.00 * size
    case 3:
        price = 21.00 * size
    case 4:
        price = 10.00 * size
    case 5:
        price = 18.00 * size

print(f"El precio del envio del paquete es de {price} €")
