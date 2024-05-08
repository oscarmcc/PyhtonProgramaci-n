"""
Author: Óscar Martín-Castaño Carrillo
Date: 08/03/2024
"""
import random
from typeguard import typechecked
from Actividad1 import Dice


@typechecked
class PokerDice(Dice):
    __SCORE = (6, 5, 4, 3, 2, 1)

    def __init__(self):
        super().__init__('A', 'K', 'Q', 'J', 'R', 'N')
        self.__score = 0


    @property
    def score(self):
        return self.__score

    def roll(self):
        super().roll()
        self.__score_mark()

    def __score_mark(self):
        if self.side == 'A':
            self.__score = 6
        elif self.side == 'K':
            self.__score = 5
        elif self.side == 'Q':
            self.__score = 4
        elif self.side == 'J':
            self.__score = 3
        elif self.side == 'R':
            self.__score = 2
        else:
            self.__score = 1

