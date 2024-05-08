"""
Title: Calcular cuota hipoteca y tabla amortización

Queremos calcular la cuota mensual de una hipoteca y su tabla de amortización, conocido el monto
del préstamo a pedir, su interés anual (un valor entre 0 y 1) y su duración en años.
Calcular la cuota de una hipoteca y crear una tabla de amortización mensual implica usar una
fórmula matemática específica y realizar algunos cálculos

Author: Óscar Martín-Castaño Carrillo
Date: 10/11/2023
"""

print('Programa que calcula la couta de una hipoteca y la tabla de amortización')

while True:
    mortgage = int(input('Necesite el dato de la hipoteca '))
    interest = int(input('Dame el porcentaje de interés que tiene la hipoteca ')) / 100
    years = int(input('Necesito que me facilites el dato de los años a los que vas a pagar la hipoteca '))
    years *= 12
    outstandard_balance = mortgage
    print('Mes\tPago principal\tInterés mensual\tResto por pagar')
    for i in range(1, years):
        # Primero se calcula el interés mensual
        monthly_interest = (outstandard_balance * interest) / 12
        # Calculamos el pago mensual
        first_part_monthly_payment = mortgage * (interest / 12) * ((interest / 12) + 1) ** years
        second_part_monthly_payment = ((1 + (interest / 12)) ** years) - 1
        monthly_payment = (first_part_monthly_payment / second_part_monthly_payment)
        # Calculamos el pago principal
        principal_payment = monthly_payment - monthly_interest
        # Calculamos lo que queda del préstamos
        outstandard_balance = outstandard_balance - principal_payment
        # Escribimos en cada mes lo que pagamos, el interés y lo que nos queda por pagar
        print(f"{i}\t{principal_payment}\t{monthly_interest}\t{outstandard_balance}")
