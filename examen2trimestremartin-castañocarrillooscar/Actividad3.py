"""
Author: Óscar Martín-Castaño Carrillo
Date: 08/03/2024
"""
from Actividad1 import Dice
from typeguard import typechecked


@typechecked
class LudoDice(Dice):

    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 6)
        super().roll()

    def __gt__(self, other: Dice):
        return self.side > other.side

    def __lt__(self, other: Dice):
        return self.side <= other.side

    def __le__(self, other: Dice):
        return self.side < other.side

    def __ge__(self, other: Dice):
        return self.side >= other.side
