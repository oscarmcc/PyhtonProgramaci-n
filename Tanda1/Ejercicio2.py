"""
 Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y
 setters (propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto. Además la clase debe
 tener un __str__() para poder imprimir los puntos en formato “(x,y)”. Implementa un test donde crees un punto, lo
 imprimas utilizando de manera implícita el método __str__(), imprimas su coordenada x, asignes 0 a su coordenada x, y
 vuelvas a imprimir el punto.

 Author: Óscar Martín-Castaño Carrillo
 Date: 14/01/2024
"""


class Point:
    def __init__(self, x, y):
        self.x = x  # Llamamos al setter, si lo ponemos privado directamente es
        self.y = y  # dependiendo de si queremos controlar o no lo que estamos añadiendo al atributo del objeto

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = float(value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = float(value)

    def invert_coordinates(self):
        self.__x, self.__y = self.__y, self.__x

    def __str__(self):
        return f"Point({self.x},{self.y})"
