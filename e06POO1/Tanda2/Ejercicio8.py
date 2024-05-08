"""
Muestra un menú con las siguientes opciones:

Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce
correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor. Si
el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida (se ha ejecutado
la opción anterior), si no la hay mostrará un mensaje de error.
Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
Añadir años a la fecha. El mismo procedimiento que la opción 2.
Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error)
y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la
que tenemos almacenada y el número de días comprendido entre las dos fechas.
Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
Terminar.

Author: Óscar Martín-Castaño Carrillo
Date: 09/02/2024
"""
import datetime
from typeguard import typechecked


class Date:
    def __init__(self):
        self.date = None

    def introduce_date(self):
        while True:
            try:
                day = int(input("Introduce el día "))
                month = int(input("Introduce el mes "))
                year = int(input("Introduce el año "))
                self.date = datetime.date(year, month, day)
                print("La fecha introducida es:", self.date.strftime("%d/%m/%Y"))
                return self.date
            except ValueError:
                print("Introduce una Fecha válida")

    def add_days(self):
        try:
            days = int(input("Introduce el número de días para añadir "))
            self.date += datetime.timedelta(days=days)
        except ValueError:
            print("Introduce una fecha válida")

    def add_months(self):
        try:
            months = int(input("Introduce el número de meses para añadir "))
            self.date = self.date.replace(year=self.date.year + (self.date.month + months - 1) // 12,
                                          month=(self.date.month + months - 1) % 12 + 1)
        except ValueError:
            print("Introduce una fecha valida")

    def add_years(self):
        try:
            years = int(input("Introduce el número de años para añadir "))
            self.date = self.date.replace(year=self.date.year + years)
        except ValueError:
            print("Introduce una fecha valida ")

    def compare_date(self, other_date):
        if self.date.year < other_date.year:
            print("La fecha introducida es posterior a la fecha almacenada.")
        elif self.date.year > other_date.year:
            print("La fecha introducida es anterior a la fecha almacenada.")
        elif self.date.month < other_date.month:
            print("La fecha introducida es posterior a la fecha almacenada.")
        elif self.date.month > other_date.month:
            print("La fecha introducida es anterior a la fecha almacenada.")
        elif self.date.day < other_date.day:
            print("La fecha introducida es posterior a la fecha almacenada.")
        elif self.date.day > other_date.day:
            print("La fecha introducida es anterior a la fecha almacenada.")
        else:
            print("Las fechas son iguales.")

    def show_long_date(self):
        days_week = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        months_year = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
                       "octubre", "noviembre", "diciembre"]
        day_of_week = days_week[self.date.weekday()]
        month = months_year[self.date.month - 1]
        print(f"{day_of_week}, {self.date.day} de {month} de {self.date.year}")


@typechecked
class Menu:
    def __init__(self, *options):
        if len(options) == 1 and isinstance(options[0], (list, tuple)):
            self.options = list(options[0])
        self.__option = None
        self.dates = Date()
        self.select_option()

    @property
    def option(self):
        return self.__option

    def show_options(self):
        for i in range(len(self.options)):
            print(f"{i + 1}.{self.options[i]}")

    def select_option(self):
        while True:
            self.show_options()
            self.__option = int(input("Ingrese la opción deseada "))
            match self.__option:
                case 1:
                    self.dates.introduce_date()
                case 2:
                    self.dates.add_days()
                case 3:
                    self.dates.add_months()
                case 4:
                    self.dates.add_years()
                case 5:
                    self.compare_dates_in_menu()
                case 6:
                    self.dates.show_long_date()
                case 7:
                    new_option = input("Ingrese la nueva opción deseada: ")
                    self.options.append(new_option)
                case 8:
                    exit(0)

    def compare_dates_in_menu(self):
        try:
            day = int(input("Introduce el día: "))
            month = int(input("Introduce el mes: "))
            year = int(input("Introduce el año: "))
            other_date = datetime.date(year, month, day)
            self.dates.compare_date(other_date)
        except ValueError:
            print("La fecha introducida no es válida.")


if __name__ == "__main__":
    opciones = ("Introduce una fecha", "Agregar dias", "Agregar meses", "Agregar años",
                "Comparar fechas", "Mostrar la fecha en formato largo", "Agregar una opción nueva", "Terminar")
    menu = Menu(opciones)
