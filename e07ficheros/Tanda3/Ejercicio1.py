from __future__ import annotations
import datetime
from abc import ABC
from random import randint
import json
from typeguard import typechecked
from typing import List


@typechecked
class Movement(ABC):

    def __init__(self, movement_date=datetime.datetime.now()):
        self.__datetime = str(movement_date)

    @property
    def datetime(self):
        return self.__datetime


@typechecked
class InternalMovement(Movement):

    __ALLOWED_INTERNAL_MOVEMENTS = ["Ingreso", "Retirada", "Creación de cuenta"]

    def __init__(self, movement_type: str, amount: float, final_balance: float, source_account: str,
                 movement_date=datetime.datetime.now()):
        super().__init__(movement_date)
        self.__movement_type = self.__errorcheck(movement_type)
        self.__amount = amount
        self.__final_balance = final_balance
        self.__source_account = source_account

    @property
    def movement_type(self):
        return self.__movement_type

    @property
    def amount(self):
        return self.__amount

    @property
    def final_balance(self):
        return self.__final_balance

    @property
    def source_account(self):
        return self.__source_account

    @staticmethod
    def allowed_internal_movements():
        return InternalMovement.__ALLOWED_INTERNAL_MOVEMENTS

    def __errorcheck(self, checked_value):
        if checked_value not in InternalMovement.__ALLOWED_INTERNAL_MOVEMENTS:
            raise InternalMovementError
        return checked_value

    def __str__(self):
        return (f"{self.__movement_type}. Importe: {self.__amount}€. Cuenta {self.__source_account}."
                f" Saldo resultante: {self.__final_balance}€. Hecho en {super().datetime}")

    def __repr__(self):
        return f"{self.__movement_type}"


@typechecked
class Transference(Movement):

    def __init__(self, amount: float, source_account: str,
                 receiving_account: str, this_account: str, this_accounts_final_balance: float,
                 movement_date=datetime.datetime.now()):
        super().__init__(movement_date)
        self.__movement_type = "Transferencia"
        self.__amount = amount
        self.__source_account = source_account
        self.__receiving_account = receiving_account
        self.__this_account = this_account
        self.__this_accounts_final_balance = this_accounts_final_balance

    @property
    def movement_type(self):
        return self.__movement_type

    @property
    def amount(self):
        return self.__amount

    @property
    def source_account(self):
        return self.__source_account

    @property
    def receiving_account(self):
        return self.__receiving_account

    @property
    def this_account(self):
        return self.__this_account

    @property
    def this_accounts_final_balance(self):
        return self.__this_accounts_final_balance

    def __str__(self):
        return (f"{self.__movement_type} de la cuenta {self.__source_account} hacia la cuenta "
                f"{self.__receiving_account}. Importe: {self.__amount}€. Saldo resultante de la cuenta "
                f"{self.__this_account}: {self.__this_accounts_final_balance}€. Hecho en {super().datetime}")

    def __repr__(self):
        return f"Transferencia"


@typechecked
class BankAccount:  # I notice the warnings, but I consider that neither of those methods must be static.

    __EXISTING_ACCOUNT_NUMBERS = []

    def __init__(self, balance: float = 0, account_number="", movements: List[Movement] = []):
        self.__balance = self.__errorproof_balance(balance)
        if account_number == "":
            self.__account_number = self.__generate_account_number()
        else:
            self.__account_number = self.__errorproof_account_number(account_number)
        if movements == []:
            self.__movements_register = [InternalMovement("Creación de cuenta", self.__balance,
                                                          self.__balance, self.__account_number)]
        else:
            self.__movements_register = movements

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @property
    def movements(self):
        movements = f"Movimientos de la cuenta {self.__account_number}:\n-----------------------\n"
        for n in range(len(self.__movements_register)):
            movements += f"{self.__movements_register[n]}\n"
        return movements

    def __generate_account_number(self):
        while True:
            aspiring_number = str(10000000000 + randint(0, 99999999999))[1:]
            if aspiring_number not in BankAccount.__EXISTING_ACCOUNT_NUMBERS:
                BankAccount.__EXISTING_ACCOUNT_NUMBERS.append(aspiring_number)
                return aspiring_number

    def __errorproof_balance(self, amount: float):
        if amount < 0:
            raise NegativeBalanceError
        return amount

    def __errorproof_account_number(self, account_number):
        test_number = account_number
        int_test_number = int(test_number)  # This will (on purpose) raise error if account_number is not a number.
        if test_number in BankAccount.__EXISTING_ACCOUNT_NUMBERS or (float(test_number) - int_test_number) != 0:
            raise ValueError("Número de cuenta no válido.")
        BankAccount.__EXISTING_ACCOUNT_NUMBERS.append(account_number)
        return account_number

    def deposit(self, amount: float,  transference_warning: bool = False):
        self.__balance += self.__errorproof_balance(amount)
        if not transference_warning:
            self.__register_movement(1, amount)

    def withdraw(self, amount: float,  transference_warning: bool = False):
        self.__errorproof_balance(amount)
        if amount > self.__balance:
            raise ExcessiveWithdrawalError
        self.__balance -= amount
        if not transference_warning:
            self.__register_movement(2, amount)
        return amount

    def transfer(self, receiver: BankAccount, amount: float):
        receiver.deposit(self.withdraw(amount, True), True)
        self.__register_transference(receiver, amount)

    def __register_movement(self, operation_code: int, amount: float = 0):
        if operation_code == 1:
            self.__movements_register.append(InternalMovement("Ingreso", amount, self.__balance,
                                                              self.__account_number))
        elif operation_code == 2:
            self.__movements_register.append(InternalMovement("Retirada", amount, self.__balance,
                                                              self.__account_number))
        else:
            raise RegisterMovementError

    def __register_transference(self, other: BankAccount, amount: float):
        self.__movements_register.append(Transference(amount, self.__account_number, other.__account_number,
                                                      self.__account_number, self.__balance))

        other.__movements_register.append(Transference(amount, self.__account_number, other.__account_number,
                                                       other.__account_number, other.__balance))

    def __movements_register_to_dict_list(self):
        dict_list = []
        for movement in self.__movements_register:
            if isinstance(movement, InternalMovement):
                dict_list.append({"movement_type": movement.movement_type, "amount": movement.amount,
                                  "final_balance": movement.final_balance, "source_account": movement.source_account,
                                  "movement_date": movement.datetime})
            elif isinstance(movement, Transference):
                dict_list.append({"movement_type": "Transferencia", "amount": movement.amount,
                                  "source_account": movement.source_account,
                                  "receiving_account": movement.receiving_account,
                                  "this_account": movement.this_account,
                                  "this_accounts_final_balance": movement.this_accounts_final_balance,
                                  "movement_date": movement.datetime})
        return dict_list

    def save_in_json(self):
        account_dict = {"account_number": self.__account_number, "balance": self.__balance,
                        "movements_register": self.__movements_register_to_dict_list()}
        with open(f"{self.__account_number}.json", "wt", encoding="utf8") as json_save:
            json.dump(account_dict, json_save)

    def __str__(self):
        return f"Account {self.__account_number}. Balance: {self.__balance}€"

    def __del__(self):
        BankAccount.__EXISTING_ACCOUNT_NUMBERS.remove(self.__account_number)


class BankAccountLoader:

    @staticmethod
    def load_account(account_number):
        with open(f"{account_number}.json", "rt", encoding="utf8") as account_save:
            saved_content = json.load(account_save)
            return BankAccount(saved_content["balance"], saved_content["account_number"],
                               BankAccountLoader.rescue_movements(saved_content["movements_register"]))

    @staticmethod
    def rescue_movements(dict_list):
        rescued_movements = []
        allowed_internal_movements = list(InternalMovement.allowed_internal_movements())
        for movement in dict_list:
            if movement["movement_type"] == "Transferencia":
                rescued_movements.append(Transference(movement["amount"], movement["source_account"],
                                                      movement["receiving_account"], movement["this_account"],
                                                      movement["this_accounts_final_balance"],
                                                      movement["movement_date"]))
            elif movement["movement_type"] in allowed_internal_movements:
                rescued_movements.append(InternalMovement(movement["movement_type"], movement["amount"],
                                                          movement["final_balance"], movement["source_account"],
                                                          movement["movement_date"]))
        return rescued_movements


class InternalMovementError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Tipo de movimiento interno no válido.")


class NegativeBalanceError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Accounts are not allowed to have a negative balance.")


class ExcessiveWithdrawalError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Withdrawal exceeds this account's balance.")


class RegisterMovementError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Invalid operation code.")
