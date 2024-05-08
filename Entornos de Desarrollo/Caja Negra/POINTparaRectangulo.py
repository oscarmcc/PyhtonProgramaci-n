from typeguard import typechecked

@typechecked
class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: int):
        self.__y = value

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Point({self.__x}, {self.__y})"

    def invert_coordinates(self):
        self.__x, self.__y = self.__y, self.__x