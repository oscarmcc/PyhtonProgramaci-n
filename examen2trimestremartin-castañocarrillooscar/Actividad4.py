"""
Author: Óscar Martín-Castaño Carrillo
Date: 08/03/2024
"""
from typeguard import typechecked
from Actividad1 import Dice


@typechecked
class TrickedLudoDice(Dice):
    __MIN_NORMAL_DICE_ROLLS = 3
    __counter_roll = 0

    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 6)

    def roll(self):
        super().roll()
        self.__counter_roll += 1

    def put(self, side):
        if self.__counter_roll >= self.__MIN_NORMAL_DICE_ROLLS:
            self.side = side
            self.__counter_roll = 0
        else:
            raise ValueError(f"No ha tirado aún {self.__MIN_NORMAL_DICE_ROLLS} veces")
