"""
Author: Óscar Martín-Castaño Carrillo
Date: 08/03/2024
"""
from typeguard import typechecked
from Actividad1 import Dice
from Actividad2 import PokerDice
from Actividad3 import LudoDice


@typechecked
class DiceCup:

    def __init__(self, *dices):
        if len(dices) == 1 and isinstance(dices[0], DiceCup):
            self.__dices = dices[0].__dices.copy()
        else:
            self.__dices = list(dices)

    @property
    def dices(self):
        return self.__dices

    @property
    def size(self):
        return len(self.__dices)

    def add(self, other: (Dice, PokerDice, LudoDice)):
        self.__dices.append(other)

    def remove(self, dice):
        if dice not in self.__dices:
            raise ValueError(f"El dado {dice} no se encuentra en el cubilete")
        self.__dices.remove(dice)

    def __str__(self):
        return f"|{self.__dices}|"
