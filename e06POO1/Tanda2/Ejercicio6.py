"""
Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y se
crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s

Author: Óscar Martín-Castaño Carrillo
Date: 08/02/2024
"""
from __future__ import annotations

from typeguard import typechecked


@typechecked
class Duration:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

        self.normalize_seconds(self.__seconds)
        self.normalize_minutes(self.__minutes)

    @classmethod
    def new_time(cls, other: Duration):
        new_time = cls(other.__hours, other.__minutes, other.__seconds)
        new_time.__hours = other.__hours
        new_time.__minutes = other.__minutes
        new_time.__seconds = other.__seconds
        return new_time

    def normalize_seconds(self, seconds: int):
        count_seconds = 0
        if self.__seconds < 0:
            self.__seconds = 60 + seconds
            self.__minutes = self.__minutes - 1
        while self.__seconds >= 60:
            self.__seconds = self.__seconds - 60
            count_seconds += 1
        self.__minutes = self.__minutes + count_seconds

    def normalize_minutes(self, minutes):
        count_minutes = 0
        if self.__minutes < 0:
            self.__minutes = 60 + minutes
            self.__seconds = 59
            self.__hours = self.__hours - 1
        while self.__minutes >= 60:
            self.__minutes = self.__minutes - 60
            count_minutes += 1
        self.__hours = self.__hours + count_minutes

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def __add__(self, other):
        self.__seconds += other.seconds
        self.__minutes += other.minutes
        self.__hours += other.hours
        self.normalize_seconds(self.__seconds)
        self.normalize_minutes(self.__minutes)
        return f"Time: {self.__hours}h {self.__minutes}m {self.__seconds}s"

    def add_hours(self, hours: int):
        return self.__hours + hours

    def add_minutes(self, minutes: int):
        self.__minutes += minutes
        self.normalize_minutes(self.__minutes)

    def add_seconds(self, seconds: int):
        self.__seconds += seconds
        self.normalize_seconds(self.__seconds)
        self.normalize_minutes(self.__minutes)

    def __sub__(self, other):
        self.subtract_hours(other.hours)
        self.subtract_minutes(other.minutes)
        self.subtract_seconds(other.seconds)
        return f"Time: {self.__hours}h {self.__minutes}m {self.__seconds}s"

    def subtract_seconds(self, seconds: int):
        self.__seconds -= seconds
        self.normalize_seconds(self.__seconds)
        self.normalize_minutes(self.__minutes)

    def subtract_minutes(self, minutes: int):
        self.__minutes -= minutes
        self.normalize_minutes(self.__minutes)

    def subtract_hours(self, hours: int):
        if self.__hours == 0 or hours >= self.__hours:
            self.__hours = 0
            if self.__minutes == 0:
                self.__minutes = 0
                self.__seconds = 59
            else:
                self.__minutes = 59
        else:
            self.__hours -= hours

    def __str__(self):
        return f"Time: {self.__hours}h {self.__minutes}m {self.__seconds}s"


if __name__ == '__main__':
    t1 = Duration(1, 20, 30)
    print(t1)
    t2 = Duration(2, 75, -10)
    print(t2)
    t3 = Duration.new_time(t2)
    print(t3)
    t4 = t2 + t1
    print(t4)
    t5 = Duration(1, 14, 20)
    t6 = t1 - t5
    print(t6)
