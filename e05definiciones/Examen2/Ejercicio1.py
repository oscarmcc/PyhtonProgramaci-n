"""
A.- Realiza la siguiente colección de funciones para manejar fechas como cadenas de caracteres,
siendo el formato de la cadena: AAAAMMDD. Ejemplo: El 15 de diciembre de 2019 sería:
"20191215".
1. ok_date: dice si la fecha que se pasa como parámetro es correcta.
2. tomorrow: suma un día a la fecha que se pasa como parámetro y lo devuelve.
3. next_n_days: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
4. yesterday: resta un día a la fecha que se pasa como parámetro y lo devuelve.
5. past_n_days: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.
6. leap_year: dice si el año de la fecha que se pasa como parámetro es bisiesto.
7. compare_dates: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
 segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
8. date_to_str: recibe una fecha y devuelve una cadena con el formato:
 DD de {MES} de AAAA (Ejemplo: "15 de Diciembre de 2019")

9. year, month, day, month_name: recibe una fecha y devuelve esos valores

Author: Óscar Martín-Castaño Carrillo
Date: 18/12/2023
"""


def month_name():
    month_name = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'juno', 'julio', 'agosto', 'septiembre',
                  'octubre', 'noviembre', 'diciembre']
    return month_name


def year_month_days():
    year_month_days = input("Introduce una fecha en formato AAAAMMDD ")
    if len(year_month_days) == 8:
        return year_month_days


def year(year_date):
    year = int(year_date[:4])
    return year


def month(month_date):
    month = int(month_date[4:6])
    return month


def day(day_date):
    day = int(day_date[6:])
    return day


def leap_year(year):
    if year >= 1 or year <= 9999:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False


def ok_date(year, month, day, date):
    if len(date) == 8:
        if leap_year(year):
            match month:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                    if 1 <= day <= 31:
                        return True
                    else:
                        return False
                case 2:
                    if 1 <= day <= 29:
                        return True
                    else:
                        return False
                case 4 | 6 | 9 | 11:
                    if 1 <= day <= 31:
                        return True
                    else:
                        return False
        else:
            match month:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                    if 1 <= day <= 31:
                        return True
                    else:
                        return False
                case 2:
                    if 1 <= day <= 28:
                        return True
                    else:
                        return False
                case 4 | 6 | 9 | 11:
                    if 1 <= day <= 31:
                        return True
                    else:
                        return False
    else:
        return False


def tomorrow(year, month, day):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if day == 31:
                day = 1
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
            else:
                day += 1
        case 2:
            if leap_year(year):
                if day == 29:
                    day = 1
                    month +=1
                else:
                    day += 1
            else:
                if day == 28:
                    day = 1
                    month += 1
                else:
                    day += 1
        case 4 | 6 | 9 | 11:
            if day == 30:
                day = 1
                month += 1
            else:
                day += 1
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    date = str(year) + str(month) + str(day)
    date = int(date)
    return date


def yesterday(year, month, day):
    match month:
        case 1 | 5 | 7 | 8 | 10 | 12:
            if day == 1:
                day = 30
                if month == 1:
                    month = 12
                    year -= 1
                else:
                    month -= 1
            else:
                day -= 1
        case 3:
            if leap_year(year):
                if day == 1:
                    day = 29
                    month -= 1
                else:
                    day -= 1
        case 2:
            if day == 1:
                day = 31
                month -=1
            else:
                day -= 1
        case 4 | 6 | 9 | 11:
            if day == 1:
                day = 31
                month -= 1
            else:
                day -= 1
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    date = str(year) + str(month) + str(day)
    date = int(date)
    return date


def next_n_days(repetitions):
    return (tomorrow(year, month, day) for _ in range(0, repetitions))


def compare_dates(date1, date2):
    if year(date1) == year(date2):
        if month(date1) == month(date2):
            if day(date1) == day(date2):
                return 0
            elif day(date1) > day(date2):
                return 1
            else:
                return -1
        elif month(date1) > month(date2):
            return 1
        else:
            return -1
    elif year(date1) > year(date2):
        return 1
    else:
        return -1

if __name__ == '__main__':
    date = year_month_days()
    date2 = year_month_days()
    year2 = year(date2)
    month2 = month(date2)
    day2 = day(date2)
    year = year(date)
    month = month(date)
    day = day(date)
    leap = leap_year(year)
    name_month = month_name()
    okdate = ok_date(year, month, day, date)
    tomorrow = tomorrow(year, month, day)
    yesterday = yesterday(year, month, day)
    #nextday = next_n_days(2)
    print(compare_dates(date, date2))
    print(date)
    print(year)
    print(month)
    print(day)
    print(leap)
    print(okdate)
    print(tomorrow)
    print(yesterday)
    #print(nextday)