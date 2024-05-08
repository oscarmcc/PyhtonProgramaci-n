"""
Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a
continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de
asteriscos o cualquier otro carácter.

Author: Óscar Martín-Castaño Carrillo
Date: 16/11/2023
"""

print('Programa que pide la temperatura media en un año y muestra los datos en barras horizontales')

MONTHS = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
          "Octubre", "Noviembre", "Diciembre"]
temperatures = [0] * 12

for i in range(len(MONTHS)):
    temperatures[i] = float(input(f"Temperatura media del mes {MONTHS[i]}: "))

for c in range(len(MONTHS)):
    print(f"{MONTHS[c]+':':11} {'*' * round(temperatures[c])}")
