"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y
así sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará
después de los 20 meses.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""
FIRST_PAYMENT = 10
TOTAL_MONTHS = 20

print('Programa para saber cuánto pagarás en 20 meses')

total_price = 0
monthly_price = FIRST_PAYMENT

for month in range(TOTAL_MONTHS):
    print(f"El precio que pagas el mes {month + 1} es de {monthly_price:.2f} euros")
    total_price += monthly_price
    monthly_price *= 2

print(f"El total que debes de pagar es {total_price:.2f} euros")
