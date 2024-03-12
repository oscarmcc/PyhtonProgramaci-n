"""
 Crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera. Para la clase Vehicle,
 crea los atributos de clase vehicles_created y total_kilometers, así como el atributo de instancia kilometers_traveled.

En la clase Vehicle crea un método para viajar (travel) que incremente los kilómetros recorridos. En la clase Bike haz
un método para hacer el caballito y en la clase Car otro para quemar rueda.

Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como el que se
muestra a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Ver kilometraje de la bicicleta
6. Ver kilometraje del coche
7. Ver kilometraje total
8. Salir

Elige una opción (1-8):

Author: Óscar Martín-Castaño Carrillo
Date: 12/02/2024
"""

from typeguard import typechecked
from abc import ABC


class Menu:
    def __init__(self, *options):
        if len(options) == 1 and isinstance(options[0], (list, tuple)):
            self.options = list(options[0])

    def show_options(self, ):
        max_len_word = self.options[0]
        for n in range(1, len(self.options)):
            if len(max_len_word) < len(self.options[n]):
                max_len_word = self.options[n]
        for i in range(len(self.options)):
            print(f"{i + 1}.{self.options[i]}")
        print('-' * (len(max_len_word) + 3))


@typechecked
class Vehicle(ABC):
    __vehicles_created = 0
    __total_kilometers = 0.0

    def __init__(self):
        self.__kilometers_travelled = 0.0
        Vehicle.__vehicles_created += 1

    @classmethod
    def total_kilometers(cls):
        return cls.__total_kilometers

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created

    @property
    def kilometers_travelled(self):
        return self.__kilometers_travelled

    def travel(self, distance: float):
        if distance < 0:
            raise ValueError("No puedo recorrer una distancia negativa de kilómetros")
        self.__kilometers_travelled += distance
        Vehicle.__total_kilometers += distance

    def __del__(self):
        Vehicle.__total_kilometers -= self.__kilometers_travelled
        Vehicle.__vehicles_created -= 1


class Bike(Vehicle):

    def __init__(self):
        super().__init__()

    @property
    def bike_kilometers(self):
        return self.kilometers_travelled

    @staticmethod
    def do_horsepower():
        print(f'Bike doing horsepower')

    def __str__(self):
        return f'Bike travel: {self.bike_kilometers}'


@typechecked()
class Car(Vehicle, ABC):
    FUEL_CONSUMED_PER_KILOMETER = 0.1
    FUEL_CONSUMED_BURNING_WHEEL = 1
    TANK_CAPACITY = 50

    def __init__(self):
        super().__init__()
        self.__fuel = 0.0

    @property
    def car_kilometers(self):
        return self.kilometers_travelled

    @property
    def fuel_consume(self):
        return self.__fuel

    def fill_the_tank(self):
        self.__fuel += self.TANK_CAPACITY

    def burn_wheel(self):
        print(f'Car burning wheel')
        self.__fuel -= self.FUEL_CONSUMED_BURNING_WHEEL

    def travel(self, distance: int):
        if distance * self.FUEL_CONSUMED_PER_KILOMETER > self.__fuel:
            super().travel(self.__fuel / self.FUEL_CONSUMED_PER_KILOMETER)
            self.__fuel = 0.0
        elif self.__fuel == 0.0:
            raise ValueError('No fuel in the tank')
        else:
            super().travel(distance)
            self.__fuel -= distance * self.FUEL_CONSUMED_PER_KILOMETER

    def __str__(self):
        return f'Car travel: {self.car_kilometers}'


if __name__ == '__main__':
    opciones = ['Crear una bicicleta', 'Crea un coche', 'Anda con la bicicleta', 'Haz el caballito con la bici',
                'Anda con el coche', 'Quema rueda con el coche', 'Ver kilometraje del coche',
                'Ver kilometraje de la bicicleta', 'Llenar el tanque de combustible del coche',
                'Ver el combustible que queda en el coche', 'Ver kilometraje total', 'Ver objetos creados',
                'Eliminar objeto bicicleta', 'Eliminar objeto coche', 'Salir']


    def select_option():
        while True:
            menu.show_options()
            options = int(input("Ingrese la opción deseada "))
            match options:
                case 1:
                    bike = Bike()
                case 2:
                    car = Car()
                case 3:
                    distance = int(input("Ingrese la distancia recorrida "))
                    bike.travel(distance)
                    print(f"La distancia recorrida es {bike.kilometers_travelled}")
                case 4:
                    bike.do_horsepower()
                case 5:
                    distance = int(input("Ingrese la distancia recorrida "))
                    car.travel(distance)
                    print(f"La distancia recorrida es {car.kilometers_travelled}")
                case 6:
                    car.burn_wheel()
                case 7:
                    print(car)
                case 8:
                    print(bike)
                case 9:
                    car.fill_the_tank()
                case 10:
                    print(f"El combustible que le queda al coche es {car.fuel_consume}")
                case 11:
                    print(f" La distancia recorrida por los dos vehículos es {Vehicle.total_kilometers()}")
                case 12:
                    print(f"Los objetos creados son {Vehicle.vehicles_created()}")
                case 13:
                    del bike
                case 14:
                    del car
                case 15:
                    exit(0)


    menu = Menu(opciones)
    select_option()
