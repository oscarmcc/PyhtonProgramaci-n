"""
Haz el ejercicio 1 usando una función generadora.

Author: Óscar Martín-Castaño Carrillo
Date: 14/05/2024
"""


def prime_generator(maximum):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, maximum + 1):
        if is_prime(num):
            yield num


primes = list(prime_generator(15))
print(primes)
