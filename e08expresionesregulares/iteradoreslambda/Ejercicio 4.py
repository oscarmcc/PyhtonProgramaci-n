"""
Vamos a crear una lista de 100 números enteros aleatorios entre -5000 y 5000 y vamos a averiguar:

Usando map:
Una lista con los números elevados al cuadrado.
Una lista con los números como cadena de texto.
Usando filter:
Los números múltiplos de 3.
El total de números negativos.
Los números primos.
El máximo número primo.
Usando reduce:
La suma de todos los números.
La suma de todos los números pares.
La multiplicación de todos los números primos.

Author: Óscar Martín-Castaño Carrillo
Date: 14/05/2024
"""
import random
from functools import reduce

random_numbers = [random.randint(-5000, 5000) for _ in range(100)]

squared_numbers = list(map(lambda x: x ** 2, random_numbers))
string_numbers = list(map(str, random_numbers))

multiples_of_3 = list(filter(lambda x: x % 3 == 0, random_numbers))
negative_numbers = list(filter(lambda x: x < 0, random_numbers))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers = list(filter(is_prime, random_numbers))
max_prime_number = max(prime_numbers) if prime_numbers else None

sum_of_numbers = reduce(lambda x, y: x + y, random_numbers)
sum_of_even_numbers = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, random_numbers))
product_of_primes = reduce(lambda x, y: x * y, prime_numbers, 1) if prime_numbers else None

print("Random numbers:", random_numbers)
print("Squared numbers:", squared_numbers)
print("String numbers:", string_numbers)
print("Multiples of 3:", multiples_of_3)
print("Total of negative numbers:", len(negative_numbers))
print("Prime numbers:", prime_numbers)
print("Max prime number:", max_prime_number)
print("Sum of all numbers:", sum_of_numbers)
print("Sum of even numbers:", sum_of_even_numbers)
print("Product of prime numbers:", product_of_primes)
