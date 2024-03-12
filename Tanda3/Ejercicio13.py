"""
Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta
se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo número de cuenta.
 La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente. En una
 cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra. No se
 permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de éste, en el que se pide
 llevar un registro de los movimientos realizados.

Programa principal:

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)
Salida

Número de cta: 6942541557 Saldo: 0,00 €
Número de cta: 9319536518 Saldo: 1500,00 €
Número de cta: 7396941518 Saldo: 6000,00 €
Número de cta: 6942541557 Saldo: 1945,00 €
Número de cta: 9319536518 Saldo: 800,00 €
Número de cta: 7396941518 Saldo: 6175,00 €

Author: Óscar Martín-Castaño Carrillo
Date: 19/02/2024
"""
from __future__ import annotations
from typeguard import typechecked
from random import randint


@typechecked
class BankAccount:
    __account_created = []

    def __init__(self, start_balance: float = 0.0):
        self.__account = BankAccount.__create_account()
        self.__balance = start_balance
        BankAccount.__account_created.append(self.__account)

    @property
    def account(self):
        return self.__account

    @property
    def balance(self):
        return self.__balance

    @classmethod
    def __create_account(cls):
        while True:
            number = randint(1, 9999999999)
            if number not in cls.__account_created:
                break
        return number

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("No puede ser el ingreso negativo")
        self.__balance += amount

    def transfer(self, other: BankAccount, amount: float):
        self.__check_transfer(amount, other)
        self.__balance -= amount
        other.deposit(amount)

    def __check_transfer(self, amount, other):
        if self.__account == other.__account:
            raise ValueError("No se puede realizar una transferencia a la misma cuenta del banco")
        if amount > self.__balance or amount < 0:
            raise ValueError("Lo siento no se ha podido realizar la transferencia, comprueba que la cantidad que "
                             "se desea transferir es una cantidad positiva y la cuenta del banco tiene el "
                             "saldo suficiente")

    def withdraw(self, amount: float):
        self.__check_withdraw(amount)
        self.__balance -= amount

    def __check_withdraw(self, amount):
        if amount < 0 or amount > self.__balance:
            raise ValueError("Lo siento no se puede realizar el gasto, compruebe que la cantidad del gasto sea "
                             "un valor positivo y que su cuenta tiene el saldo suficiente")

    def __str__(self):
        return f"Número de cta: {self.__account:010d} Saldo: {self.__balance:.2f}€"


if __name__ == "__main__":
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
