"""

Author: Óscar Martín-Castaño Carrillo
Date: 08/03/2024
"""
from __future__ import annotations
import random
from typeguard import typechecked


@typechecked
class Dice:
    def __init__(self, *dices):
        if len(dices) == 1 and isinstance(dices[0], Dice):
            self.__dices = dices[0].__dices.copy()
        else:
            self.__dices = list(dices)
        self.__side = ''

    @property
    def dice(self):
        return self.__dices

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value

    def roll(self):
        self.__side = random.choice(self.__dices)

    def __str__(self):
        return f'|{self.__side}|'

    def __repr__(self):
        return f'{self.__dices}'

    def __eq__(self, other: Dice):
        return self.__side == other.__side

    def __ne__(self, other: Dice):
        return self.__side != other.__side
