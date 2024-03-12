"""
Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos
para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree
dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

Author: Óscar Martín-Castaño Carrillo
Date: 18/01/2024
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def get_area(self):
        base = abs(self.__point1.x - self.__point2.x)
        height = self.__point1.y - self.__point2.y
        return base * height

    def get_perimeter(self):
        base = abs(self.__point1.x - self.__point2.x)
        height = self.__point1.y - self.__point2.y
        return 2 * (base + height)
