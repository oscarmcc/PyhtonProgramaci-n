"""
 Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al
 que no se le pasa nada e inicializa el dado al azar, otro al que sólo se le pasa que número tiene el dado en la cara
 superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters, el
 método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los
 lance una serie de veces.

 Author: Óscar Martín-Castaño Carrillo
 Date: 18/01/2024
"""
from random import randint


class Dice:
    def __init__(self, show=0, faces=6):
        if show > faces or show < 0:
            raise ValueError("El número en la cara superior no se encuentra en el número de caras del dado")
        if show == 0:
            self.__show = randint(1, faces)
        else:
            self.__show = show
        if faces <= 0:
            raise ValueError("El número de caras del dado debe ser positivo")
        self.__faces = faces

    @property
    def show(self):
        return self.__show

    @property
    def faces(self):
        return self.__faces

    def roll(self):
        self.__show = randint(1, self.__faces)

    def __str__(self):
        return f"El dado muestra el número {self.__show}"
