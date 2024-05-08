from __future__ import annotations
from datetime import datetime
from typeguard import typechecked


@typechecked
class CashRegistrer:
    def __init__(self, balance: float = 0.0):
        self.__movements = []
        self.__date_movements = []
        self.__balance = balance
        self.__identifier = 0
        self.__indentifier_movement = []
        self.__amounts = []

    @property
    def balance(self):
        return self.__balance

    def add_money(self, concept: str, identifier: int, amount: float, date: datetime = datetime.now()):
        self.__check_add_money(amount, date, identifier)
        self.__identifier = Movement.number(identifier)
        self.__balance += amount
        self.__append_in_lists(amount, concept, date, identifier)

    def __append_in_lists(self, amount, concept, date, identifier):
        self.__amounts.append(Movement.amount(amount))
        self.__date_movements.append(Movement.date_time(date))
        self.__movements.append(Movement.concept(concept))
        self.__indentifier_movement.append(Movement.number(identifier))

    def __check_add_money(self, amount, date, identifier):
        if date < self.__date_movements[-1]:
            raise ValueError(f"La fecha no puede ser anterior a la fecha del último registro")
        if identifier == self.__identifier or identifier == self.__indentifier_movement[-1]:
            raise ValueError(f"No puede tener el mismo identificador que la operación anterior")
        if self.__balance + amount < 0:
            raise ValueError(f"No se puede realizar la operación ya que la cuenta se queda en números rojos")

    def delete_last(self):
        self.__date_movements.pop(-1)
        self.__movements.pop(-1)
        self.__indentifier_movement.pop(-1)

    def __str__(self):
        return (f"Cash Registrer:\n"
                f"{self.__identifier}\n"
                f"{self.__movements}\n"
                f"{self.__date_movements}\n")


@typechecked
class Movement:
    @classmethod
    def number(cls, number: int):
        return number + 1

    @classmethod
    def date_time(cls, date_time: datetime):
        return date_time

    @classmethod
    def amount(cls, amount: float):
        return amount

    @classmethod
    def concept(cls, concept: str):
        return concept
