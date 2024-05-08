"""
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

Author: Óscar Martín-Castaño Carrillo
Date: 30/10/2023
"""
import math

while True:
    num_primes_to_show = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if num_primes_to_show > 0:
        break

print("1º: 2")
num_primes_displayed = 1

prime_candidate = 3
while num_primes_displayed < num_primes_to_show:
    is_prime = True
    divider = 3
    while divider <= math.sqrt(prime_candidate):
        if prime_candidate % divider == 0:
            is_prime = False
            break
        divider += 2
    if is_prime:
        num_primes_displayed += 1
        print(f"{num_primes_displayed}º: {prime_candidate}")
    prime_candidate += 2
