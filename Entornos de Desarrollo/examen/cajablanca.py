"""
Clase "CambioCaja"
	Calcula el cambio que debe dar la caja de un supermercado.
	Dado un precio y una cantidad de dinero, el resultado será el número de monedas
	que deben darse como cambio de tal forma que el número total de monedas sea mínimo.

Autor: Jaime Rabasco Ronda
Fecha: 22/02/2024.
"""
monedas = [[2, 1, 0.50, 0.10, 0.02, 0.01], [0, 0, 0, 0, 0, 0]]
cantidad = 0
i = 0

cantidad = float(input('Dame una cantidad en euros. Te diré el total de monedas que tienes que entregar (el mínimo): '))
print("Cantidad introducida: ", cantidad)
while True:
    if monedas[0][i] <= cantidad:
        monedas[1][i] = monedas[1][i] + 1
        cantidad = cantidad - monedas[0][i]
        cantidad = round(cantidad,2)
    else:
        i = i + 1
    print('Cantidad = ', cantidad)
    if cantidad == 0:
        break
for i in range(0, len(monedas[0]), 1):
    print('Monedas de ', monedas[0][i], ' euros: ', monedas[1][i])

