from random import randint


class Dice:
    def __init__(self, show=0, faces=6):
        self.__show = show
        self.__faces = faces
        self.show_(show)
        self.faces_(faces)

    @property
    def show(self):
        return self.__show

    def show_(self, value):
        if self.show < 0:
            return False
        elif self.show > self.faces:
            return False
        elif self.show == 0:
            self.__show = randint(1, self.faces)
        else:
            self.__show = value

    @property
    def faces(self):
        return self.__faces

    def faces_(self, value):
        if value < 1:
            return False
        else:
            self.__faces = value

    def roll(self):
        self.__show = randint(1, self.__faces)

    def __str__(self):
        return f"El dado muestra el número {self.__show}"
