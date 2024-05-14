"""
Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de Eratóstenes.

Author: Óscar Martín-Castaño Carrillo
Date: 14/05/2024
"""


class PrimeIteratorEratosthenes:
    def __init__(self, maximum):
        self.max = maximum
        self.current = 1
        self.primes = self.sieve_of_eratosthenes(maximum)

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        while self.current < len(self.primes):
            if self.primes[self.current]:
                return self.current
            self.current += 1
        raise StopIteration

    @staticmethod
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime


primes = list(PrimeIteratorEratosthenes(15))
print(primes)
