"""
Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado como máximo.

Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]

Author: Óscar Martín-castaño Carrillo
Date: 14/05/2024
"""


class PrimeIterator:
    def __init__(self, maximum):
        self.max = maximum
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while self.current <= self.max:
            if self.is_prime(self.current):
                return self.current
            self.current += 1
        raise StopIteration

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


primes = list(PrimeIterator(15))
print(primes)
