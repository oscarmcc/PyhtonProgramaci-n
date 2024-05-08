"""
 Implementa la clase Mobile como subclase de Terminal (la clase del ejercicio anterior que ya no hace falta modificar).
 Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes controlar esto). El coste por
 minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos. La tarifa se puede cambiar.
 Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada. A continuación se
 proporciona el contenido del programa principal que usa esta clase y el resultado que debe aparecer por pantalla. El
 total tarificado debe aparecer con dos decimales.

Programa principal:

m1 = Mobile("678112233", "rata")
m2 = Mobile("644744469", "mono")
m3 = Mobile("622328909", "bisonte")
print(m1)
print(m2)
m1.call(m2, 320)
m1.call(m3, 200)
m2.call(m3, 550)
print(m1)
print(m2)
print(m3)
Salida:

Nº 678 11 22 33 - 0s de conversación - tarificados 0,00 euros
Nº 644 74 44 69 - 0s de conversación - tarificados 0,00 euros
Nº 678 11 22 33 - 520s de conversación - tarificados 0,52 euros
Nº 644 74 44 69 - 870s de conversación - tarificados 1,10 euros
Nº 622 32 89 09 - 750s de conversación - tarificados 0,00 euros

Author: Óscar Martín-Castaño Carrillo
Date 19/02/2024
"""
from __future__ import annotations
from Ejercicio11 import Terminal
from typeguard import typechecked


@typechecked
class Mobile(Terminal):
    LIST_FEE = ["rata", "mono", "bisonte"]
    PRICE_FEE_RATA = 0.06
    PRICE_FEE_MONO = 0.12
    PRICE_FEE_BISONTE = 0.3
    SECONDS_PER_MINUTE = 60

    def __init__(self, number: str, fee: str):
        super().__init__(number)
        if fee not in Mobile.LIST_FEE:
            raise ValueError("Las tarifas válidas son: rata, mono y bisonte")
        self.fee = fee
        self.__price = 0

    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self, value):
        self.__fee = value

    @property
    def price(self):
        return self.__price

    def call(self, other: Mobile, duration: int):
        if self.__fee == "rata":
            self.__price = self.__price + Mobile.PRICE_FEE_RATA * (duration / Mobile.SECONDS_PER_MINUTE)
        elif self.__fee == "mono":
            self.__price = self.__price + Mobile.PRICE_FEE_MONO * (duration / Mobile.SECONDS_PER_MINUTE)
        else:
            self.__price = self.__price + Mobile.PRICE_FEE_BISONTE * (duration / Mobile.SECONDS_PER_MINUTE)
        other.time += duration
        self.time += duration

    def __str__(self):
        return f"{super().__str__()} - tarificados: {self.__price:.2f} euros"


if __name__ == "__main__":
    m1 = Mobile("678112233", "rata")
    m2 = Mobile("644744469", "mono")
    m3 = Mobile("622328909", "bisonte")
    print(m1)
    print(m2)
    m1.call(m2, 320)
    m1.call(m3, 200)
    m2.call(m3, 550)
    print(m1)
    print(m2)
    print(m3)
