"""
Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de
salir y un programa de prueba.

Author: Óscar Martín-Castaño Carrillo
Date: 13/01/2024
"""
import random


class Dice:
    def __init__(self):
        self.side = random.randint(1, 6)

    def roll(self):
        self.side = random.randint(1, 6)
        return self.side

    
