"""
Tenemos guardados en un fichero CSV los nombres, dorsales y tiempos (en segundos) de las cinco
etapas para los ciclistas participantes en la última vuelta ciclista local.
Haz un programa en Python que muestre y ejecute el siguiente menú:
1. Cargar en memoria (list) los datos de un fichero CSV y ordenarlos por el tiempo total
(primero el ciclista con menor tiempo).
2. Mostrar ganador de la vuelta (dorsal, nombre del ciclista y tiempo total en HH:MM:SS).
3. Mostrar ganador de una etapa (dorsal, nombre del ciclista y tiempo en HH:MM:SS).
4. Mostrar ganador de cada una de las etapas (etapa, dorsal, nombre del ciclista y tiempo en
HH:MM:SS).
5. Guardar en un fichero CSV los datos de la opción anterior.
6. Mostrar la tabla de tiempos (dorsal, nombre del ciclista, tiempos por etapa y tiempo total en
HH:MM:SS).
7. Finalizar.

Author: Óscar Martín-Castaño Carrillo
Date: 03/05/2024
"""
import csv


class Filecsvnotfound(FileNotFoundError):
    def __init__(self):
        super().__init__('El fichero CSV no existe')


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


class Ciclist:
    def __init__(self, file):
        self.file = file
        self.ciclist = []
        self.__total_time = 0

    @property
    def total_time(self):
        return self.__total_time

    def load_into(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.ciclist.append(row)
            self.__order_fiel_ciclist()

    def __order_fiel_ciclist(self):
        for row in range(1, len(self.ciclist)):
            self.__total_time = 0
            for column in range(2, len(self.ciclist[row])):
                self.__total_time += int(self.ciclist[row][column])
            self.ciclist[row].append(self.__total_time)
        self.ciclist[1:] = sorted(self.ciclist[1:], key=lambda x: int(x[-1]))

    def winner_lap(self):
        name_winner = self.ciclist[1][0]
        dorsal = self.ciclist[1][1]
        time = self.ciclist[1][-1]
        time_horus, time_minutes, time_seconds = self.__refactor_time(time)
        return dorsal, name_winner, time_horus, time_minutes, time_seconds

    def __refactor_time(self, time):
        time_minutes = (time % 3600) / 60
        time_seconds = time % 60
        time_hours = time / 3600
        return time_hours, time_minutes, time_seconds

    def winner_stage(self, stage_option):
        time_winner_stage = self.ciclist[1][stage_option + 1]
        name = self.ciclist[1][0]
        dorsal = self.ciclist[1][1]
        for row in range(2, len(self.ciclist)):
            if int(time_winner_stage) > int(self.ciclist[row][stage_option + 1]):
                time_winner_stage = self.ciclist[row][stage_option + 1]
                name = self.ciclist[row][0]
                dorsal = self.ciclist[row][1]
        time_hours, time_minutes, time_seconds = self.__refactor_time(int(time_winner_stage))
        return dorsal, name, time_hours, time_minutes, time_seconds

    @classmethod
    def save_winners_stages_csv(cls, new_file):
        with open(new_file, 'wt', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Etapa', 'Dorsal', 'Nombre', 'Tiempo'])
            writer.writeheader()
            for n in range(1, 6):
                dorsal, name, time_hours, time_minutes, time_secods = file.winner_stage(n)
                time = str(int(time_hours)) + ':' + str(int(time_minutes)) + ':' + str(int(time_secods))
                writer.writerow({'Etapa': n, 'Dorsal': dorsal, 'Nombre': name, 'Tiempo': time})

    def see_all(self, person):
        dorsal = self.ciclist[person][1]
        name = self.ciclist[person][0]
        total_time = self.ciclist[person][-1]
        time_horus, time_minutes, time_seconds = self.__refactor_time(total_time)
        stage1 = self.ciclist[person][2]
        stage2 = self.ciclist[person][3]
        stage3 = self.ciclist[person][4]
        stage4 = self.ciclist[person][5]
        stage5 = self.ciclist[person][6]
        return dorsal, name, stage1, stage2, stage3, stage4, stage5, time_horus, time_minutes, time_seconds

    def __str__(self):
        return f'{self.ciclist}'


if __name__ == '__main__':
    options = ['Cargar en memoria (list) los datos de un fichero CSV y ordenarlos por el tiempo total '
               '(primero el ciclista con menor tiempo)',
               'Mostrar ganador de la vuelta (dorsal, nombre del ciclista y tiempo en total en HH:MM:SS)',
               'Mostrar ganador de una etapa (dorsal, nombre del ciclista y tiempo en HH:MM:SS)',
               'Mostrar ganador de cada una de las etapas (etapa, dorsal, nombre del ciclista y tiempo en HH:MM:SS)',
               'Guardar en un fichero CSV los datos de la opción anterior',
               'Mostrar la tabla de tiempos '
               '(dorsal, nombre del ciclista, tiempos por etapa y tiempo total en HH:MM:SS)',
               'Finalizar']
    menu = Menu(options)
    menu.show_options()
    option = int(input('Introduce una opción deseada: '))
    if option == 1:
        try:
            name = input('Introduce el nombre del fichero CSV te recuerdo que debe ser con la extension .csv: ')
        except FileNotFoundError:
            print('El fichero CSV tiene que ser con la extension .csv')
        file = Ciclist(name)
        file.load_into()
    else:
        raise Filecsvnotfound
    while True:
        menu.show_options()
        option = int(input('Introduce una opción deseada: '))
        if option == 1:
            try:
                name = input('Introduce el nombre del fichero CSV te recuerdo que debe ser con la extension .csv: ')
            except name.endswith('.csv'):
                print('El fichero CSV tiene que ser con la extension .csv')
                continue
            file = Ciclist(name)
            file.load_into()
        if option == 2:
            dorsal, name, time_hours, time_minutes, time_secods = file.winner_lap()
            print(f"Ganador de la vuelta: dorsal {dorsal} - {name} "
                  f"con tiempo {int(time_hours)}:{int(time_minutes)}:{int(time_secods)}")
        elif option == 3:
            choose_stage = int(input('Introduce el número de la etapa: '))
            dorsal, name, time_hours, time_minutes, time_secods = file.winner_stage(choose_stage)
            print(f"Ganador de la etapa: {choose_stage} dorsal {dorsal} - {name} "
                  f"con tiempo {int(time_hours)}:{int(time_minutes)}:{int(time_secods)}")
        elif option == 4:
            for n in range(1, 6):
                dorsal, name, time_hours, time_minutes, time_secods = file.winner_stage(n)
                print(f"Ganador de la etapa: {n} dorsal {dorsal} - {name} "
                      f"con tiempo {int(time_hours)}:{int(time_minutes)}:{int(time_secods)}")
        elif option == 5:
            other_file = input('Introduce el nombre del fichero: ')
            Ciclist.save_winners_stages_csv(other_file)
        elif option == 6:
            print('                          1      2      3      4      5      TOTAL')
            print('                        -------------------------------------------')
            for n in range(1, 7):
                (dorsal, name, stage1, stage2, stage3,
                 stage4, stage5, time_hours, time_minutes, time_secods) = file.see_all(n)
                print(f"{dorsal}. {name} {stage1:5s}{stage2:6s}{stage3:6s}{stage4:6s}{stage5:6s} "
                      f"| {int(time_hours)}:{int(time_minutes)}:{int(time_secods)} ")
        elif option == 7:
            print('Gracias por usar el programa')
            exit(0)
