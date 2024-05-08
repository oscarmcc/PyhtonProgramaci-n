"""
Nos hemos enterado que la clase datetime.date ha sido comprometida y tenemos que crear una clase nueva para almacenar
fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o año). Los objetos
de la clase Fecha son fechas de tiempo y se crean de la forma:

f1 = Date(1, 10, 2020)  # almacena el 1 de Octubre de 2020
f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Crea métodos para:

Sumar y restar días a la fecha.
Restar fechas. Devuelve el número de días comprendidos entre ambas.
Comparar la fecha almacenada con otra.
Saber si el año de la fecha almacenada es bisiesto.
Obtener el día de la semana de una fecha concreta.
El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

Author: Óscar Martín-Castaño Carrillo
Date: 11/02/2024
"""
from typeguard import typechecked


@typechecked
class Date:
    MONTHS = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    DAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    def __init__(self, day, month, year):
        if not self.is_valid_date(day, month, year):
            raise ValueError("Fecha no válida")
        self.__day = day
        self.__month = month
        self.__year = year

    @classmethod
    def from_date(cls, other):
        return cls(other.__day, other.__month, other.__year)

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):
        if month == 2:
            return 29 if Date.is_leap_year(year) else 28
        elif month in {4, 6, 9, 11}:
            return 30
        else:
            return 31

    @staticmethod
    def is_valid_date(day, month, year):
        if year < 1 or month < 1 or month > 12 or day < 1 or day > Date.days_in_month(month, year):
            return False
        return True

    def add_days(self, days):
        new_day = self.__day + days
        while new_day > Date.days_in_month(self.__month, self.__year):
            new_day -= Date.days_in_month(self.__month, self.__year)
            self.__month += 1
            if self.__month > 12:
                self.__month = 1
                self.__year += 1
        self.__day = new_day

    def substract_days(self, days):
        new_day = self.__day - days
        while new_day < 1:
            self.__month -= 1
            if self.__month < 1:
                self.__month = 12
                self.__year -= 1
            new_day += Date.days_in_month(self.__month, self.__year)
        self.__day = new_day

    def days_difference(self, other_date):
        return abs((self.to_days() - other_date.to_days()))

    def compare_date(self, other_date):
        if self.__year < other_date.__year:
            print(f"La fecha introducida {other_date.__day}/{other_date.__month}/{other_date.__year} "
                  f"es posterior a la fecha almacenada {self.__day}/{self.__month}/{self.__year}.")
        elif self.__year > other_date.__year:
            print(f"La fecha introducida {other_date.__day}/{other_date.__month}/{other_date.__year} "
                  f"es anterior a la fecha almacenada {self.__day}/{self.__month}/{self.__year}.")
        elif self.__month < other_date.__month:
            print(f"La fecha introducida {other_date.__day}/{other_date.__month}/{other_date.__year} "
                  f"es posterior a la fecha almacenada {self.__day}/{self.__month}/{self.__year}.")
        elif self.__month > other_date.__month:
            print(f"La fecha introducida {other_date.__day}/{other_date.__month}/{other_date.__year} "
                  f"es anterior a la fecha almacenada {self.__day}/{self.__month}/{self.__year}.")
        elif self.__day < other_date.__day:
            print(f"La fecha introducida {other_date.__day}/{other_date.__month}/{other_date.__year} "
                  f"es posterior a la fecha almacenada {self.__day}/{self.__month}/{self.__year}.")
        elif self.__day > other_date.__day:
            print(f"La fecha introducida {other_date.__day}/{other_date.__month}/{other_date.__year} "
                  f"es anterior a la fecha almacenada {self.__day}/{self.__month}/{self.__year}.")
        else:
            print("Las fechas son iguales.")

    def day_of_week(self):
        days_since_epoch = self.to_days()
        return Date.DAYS[days_since_epoch % 7]

    def is_bisiesto(self):
        return Date.is_leap_year(self.__year)

    def __str__(self):
        return f"{self.__day} de {Date.MONTHS[self.__month - 1]} de {self.__year}"

    def to_days(self):
        days = self.__day - 1
        for y in range(1, self.__year):
            days += 366 if Date.is_leap_year(y) else 365
        for m in range(1, self.__month):
            days += Date.days_in_month(m, self.__year)
        return days


if __name__ == "__main__":
    f1 = Date(1, 10, 2020)
    f2 = Date.from_date(f1)
    print(f2)
    f2.add_days(10)
    print(f2)
    f2.substract_days(5)
    print(f2)
    print(f1.days_difference(f2))
    print(f1.compare_date(f2))
    print(f1.day_of_week())
    print(f1.is_bisiesto())
