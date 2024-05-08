"""
Amplía el ejercicio de la tanda anterior que implementaba cuentas corrientes de un banco de tal forma que cada cuenta
lleve un registro de todos los movimientos realizados: ingresos, cargos y transferencias
(tanto enviadas como recibidas).
"""
from __future__ import annotations
from typing import List
from random import randint
from typeguard import typechecked


class Transaction:
    def __init__(self, type: str, amount: float, from_account: int = None, to_account: int = None):
        self.type = type
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account

    def __str__(self):
        if self.type == "transfer_in":
            return (f"Transferencia recibida de {self.amount:.2f} € de la cuenta {self.from_account} "
                    f"Saldo: {self.to_account:.2f} €")
        elif self.type == "transfer_out":
            return (f"Transferencia emitida de {self.amount:.2f} € a la cuenta {self.to_account} "
                    f"Saldo: {self.from_account:.2f} €")
        else:
            return f"{self.type.capitalize()} de {self.amount:.2f} € Saldo: {self.to_account:.2f} €"


@typechecked
class BankAccount:
    __account_created = []

    def __init__(self, start_balance: float = 0.0):
        self.__account = BankAccount.__create_account()
        self.__balance = start_balance
        self.__transactions: List[Transaction] = []
        BankAccount.__account_created.append(self.__account)

    @property
    def account(self):
        return self.__account

    @property
    def balance(self):
        return self.__balance

    @property
    def transactions(self):
        return self.__transactions

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
        self.__transactions.append(Transaction("ingreso", amount, to_account=self.__balance))

    def transfer(self, other: BankAccount, amount: float):
        self.__check_transfer(amount, other)
        self.__balance -= amount
        other.deposit(amount)
        self.__transactions.append(Transaction("transfer_out", amount, self.__balance, other.balance))
        other.__transactions.append(Transaction("transfer_in", amount, self.balance, other.__balance))

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
        self.__transactions.append(Transaction("cargo", amount, to_account=self.__balance))

    def __check_withdraw(self, amount):
        if amount < 0 or amount > self.__balance:
            raise ValueError("Lo siento no se puede realizar el gasto, compruebe que la cantidad del gasto sea "
                             "un valor positivo y que su cuenta tiene el saldo suficiente")

    def __str__(self):
        return f"Número de cta: {self.__account:010d} Saldo: {self.__balance:.2f}€"

    def movements(self) -> str:
        movements_str = f"Movimientos de la cuenta {self.__account}\n-----------------------------------\n"
        for transaction in self.__transactions:
            movements_str += str(transaction) + "\n"
        return movements_str


if __name__ == "__main__":
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    cuenta1.deposit(2000)
    cuenta1.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta1, 100)
    cuenta1.transfer(cuenta3, 250)
    cuenta3.transfer(cuenta1, 22)
    print(cuenta1.movements())
