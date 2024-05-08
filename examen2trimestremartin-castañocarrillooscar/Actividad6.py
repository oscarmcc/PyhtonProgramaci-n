"""
Author: Óscar Martín-castaño Carrillo
Date: 08/03/2024
"""
from typeguard import typechecked
from Actividad5 import DiceCup
import random


@typechecked
class PokerDiceCup(DiceCup):
    __SCORE = (6, 5, 4, 3, 2, 1)

    def __init__(self, *dices):
        super().__init__(*dices)
        self.__side = ''
        self.__score = 0
        self.__roll()

    @property
    def score(self):
        return self.__score

    def __roll(self):
        self.__side = random.choice(self.dices)
        self.__score_mark()

    def __score_mark(self):
        if self.__side == 'A':
            self.__score += 6
        elif self.__side == 'K':
            self.__score += 5
        elif self.__side == 'Q':
            self.__score += 4
        elif self.__side == 'J':
            self.__score += 3
        elif self.__side == 'R':
            self.__score += 2
        else:
            self.__score += 1

    def __str__(self):
        return f"|{self.__side}|"
