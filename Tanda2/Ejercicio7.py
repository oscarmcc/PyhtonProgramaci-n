"""
Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos
hacer las siguientes operaciones:

Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye
simplificada, no se puede dividir por cero.
Obtener resultado de la fracción (número real).
Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
Comparar fracciones entre sí o con enteros usando los operadores relacionales.

Author: Óscar Martín-Castaño Carrillo
Date: 08/02/2024
"""
from typeguard import typechecked


def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True


@typechecked
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator
        self.simplify()

    @property
    def numerator(self):
        return int(self.__numerator)

    @property
    def denominator(self):
        return int(self.__denominator)

    def simplify(self):
        max_divisor = 0
        ederly = self.__denominator

        for n in range(1, ederly + 1):
            if self.__denominator % n == 0 and self.__numerator % n == 0:
                max_divisor = n
        self.__numerator //= max_divisor
        self.__denominator //= max_divisor

    def __mul__(self, other: int):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.__numerator
            denominator = self.__denominator * other.__denominator
        else:
            numerator = self.__numerator * other
            denominator = self.__denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other: int):
        if isinstance(other, Fraction):
            numerator = self.__numerator * other.denominator
            denominator = self.__denominator * other.numerator
        else:
            numerator = self.__numerator
            denominator = self.__denominator * other
        return Fraction(numerator, denominator)

    def __add__(self, other):
        self.common_min(other)

        self.__numerator += other.numerator
        self.simplify()
        return self.__str__()

    def common_min(self, other):
        if isinstance(other, Fraction):
            if is_prime(self.__denominator) and is_prime(other.__denominator):
                self.__numerator *= other.__denominator
                other.__numerator *= self.__denominator
                help_denominator = self.__denominator
                self.__denominator *= other.__denominator
                other.__denominator *= help_denominator
            else:
                if other.__denominator > self.__denominator:
                    for i in range(2, other.__denominator + 1):
                        if self.__denominator % i == 0:
                            self.__denominator *= i
                            self.__numerator *= i
                            break
                elif other.__denominator == 1:
                    other.__numerator *= self.__denominator
                elif self.__denominator == 1:
                    self.__numerator *= other.__denominator
                else:
                    for i in range(2, self.__denominator + 1):
                        if other.__denominator % i == 0:
                            other.__numerator *= i
                            break

    def __sub__(self, other):
        self.common_min(other)

        self.__numerator -= other.numerator
        self.simplify()
        return self.__str__()

    def __str__(self):
        return (f"La fracción {int(self.__numerator)} / {int(self.__denominator)} "
                f"= {self.__numerator / self.__denominator}")


if __name__ == "__main__":
    fraction1 = Fraction(3, 4)
    print(fraction1)
    fraction2 = Fraction(6, 3)
    print(fraction2)
    fraction3 = Fraction(169, 26)
    print(fraction3)
    fraction2 *= 2
    print(fraction2)
    fraction1 += fraction3
    print(fraction1)
    f4 = Fraction(4, 7)
    print(f4)
    f5 = f4 - fraction2
    print(f5)
