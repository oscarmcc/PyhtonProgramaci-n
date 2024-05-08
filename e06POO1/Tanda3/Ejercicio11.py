"""
Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar unos a
otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del programa principal
que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono tienen que validarse como
tales al crear el objeto (solo dígitos, empiezan por 9, 6 ó 7, su longitud es de nueve dígitos) y no puede haber dos
terminales con el mismo número.

Programa principal:

t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.call(t2, 320)
t1.call(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)
Salida:

No 678 11 22 33 - 0s de conversación
No 644 74 44 69 - 0s de conversación
No 678 11 22 33 - 520s de conversación
No 644 74 44 69 - 320s de conversación
No 622 32 89 09 - 200s de conversación
No 664 73 98 18 - 0s de conversación

Author: Óscar Martín-castaño Carrillo
Date: 19/02/2024
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class TerminalManager:
    existing_numbers = []

    @classmethod
    def add_number(cls, number: str):
        if cls.number_exists(number):
            raise ValueError("El número de teléfono ya existe")
        cls.existing_numbers.append(number)

    @classmethod
    def number_exists(cls, number: str) -> bool:
        return number in cls.existing_numbers

    @classmethod
    def remove_number(cls, number: str):
        cls.existing_numbers.remove(number)


@typechecked
class Terminal:

    def __init__(self, number: str):
        if not self.__validation_number(number):
            raise ValueError(f"Número incorrecto")
        if TerminalManager.number_exists(number):
            raise ValueError("El número ya existe")

        TerminalManager.add_number(number)
        self.number = number
        self.time = 0

    @staticmethod
    def __validation_number(number: str):
        if number[0] in '967' and number.isdigit() and len(number) == 9:
            return True

    def call(self, other: Terminal, duration: int):
        other.time += duration
        self.time += duration

    def __str__(self):
        return (f"No {self.number[:3]} {self.number[3:5]} {self.number[5:7]} {self.number[7:9]} "
                f"- {self.time}s de conversación")


if __name__ == "__main__":
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")
    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    t6 = Terminal("567878665")
    t5 = Terminal("678112233")
