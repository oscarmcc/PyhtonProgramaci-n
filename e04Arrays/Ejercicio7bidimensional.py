"""
Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de PROGRAMACIÓN,
LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMATICOS.

El número de alumnos no lo sabemos de antemano por lo que se han de añadir conforme se vayan introduciendo los datos.

El programa pedirá el nombre y apellidos del alumno y a continuación las calificaciones en los módulos mencionados
anteriormente.

Cuando el usuario desee dejar de introducir información deberá de introducir una cadena vacía al introducir el nombre.

Asimismo el programa deberá de proporcionar las siguientes funcionalidades:

Impresión de las calificaciones del curso completo.
Impresión de las calificaciones de un alumno en concreto. El programa pedirá nombre y apellidos del alumno y de
encontrarlo mostrará las calificaciones de todos los módulos de este alumno.
Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota media.
Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota máxima
así como el alumno con la misma.
Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota más
baja así como el alumno con la misma.
Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá de ser
capaz de realizar una ordenación descendente por dicha nota.

Author: Óscar Martin-Castaño Carrillo
"""

print('Programa que pide el nombre y apellidos del alumno junto a sus notas y muestra en orden las notas junto a la '
      'máxima y la media de sus notas')

import random
from statistics import mean

MODULES = ["Programación", "Lenguaje de Marcas", "Bases de Datos", "Sistemas Informáticos"]
LEN_STUDENT_NAME = 30
LEN_MARK_NAME = 22
MARK_FORMAT = "5.2f"

def input_marks():
    def input_mark():
        while True:
            mark = float(input(f"Dame su nota en {module} (entre 0 y 10): "))
            if 0 <= mark <= 10:
                return mark
            print("El valor de la nota es erróneo, debe ser entre 0 y 10")

    while True:
        student_name = input("\nDame el nombre y apellidos del alumno/a a dar de alta (Intro para terminar): ")
        if student_name == "":
            break
        marks = []
        for module in MODULES:
            module_mark = input_mark()
            marks.append(module_mark)
        students.append([student_name] + marks)

def print_marks_course():
    print(f"\n{'Estudiante':{LEN_STUDENT_NAME}} PROGR L.MAR B.DAT S.INF\n")
    for student in students:
        print(f"{student[0]:{LEN_STUDENT_NAME}} ", end="")
        marks = student[1:]
        for mark in marks:
            print(f"{mark:{MARK_FORMAT}} ", end="")
        print()

def print_marks_student():
    def print_marks():
        marks = student[1:]
        for i in range(len(MODULES)):
            print(f"{MODULES[i]+':':{LEN_MARK_NAME}} {marks[i]:{MARK_FORMAT}}")

    student_name = input("Nombre del alumno/a: ")
    for student in students:
        if student[0] == student_name:
            print_marks()
            return
    print("Ese nombre de estudiante no existe.")

def print_marks_module_sorted():
    module = input_module()
    if module == -1:
        return
    marks = [[student[module], student[0]] for student in students]
    marks.sort(reverse=True)
    for mark in marks:
        print(f"{mark[1]:{LEN_STUDENT_NAME}} {mark[0]:{MARK_FORMAT}}")

def input_module():
    module = int(input("Número de módulo (1-PROGR 2-L.MAR 3-B.DAT 4-S.INF): "))
    if module < 0 or module > len(MODULES):
        print("ERROR. El número de módulo es erróneo.")
        return -1
    return module

def print_min_mark_module():
    module = input_module()
    if module != -1:
        marks = [student[module] for student in students]
        print(f"La nota más baja de {MODULES[module-1]} es {min(marks)}")

def print_max_mark_module():
    module = input_module()
    if module != -1:
        marks = [student[module] for student in students]
        print(f"La nota más alta de {MODULES[module-1]} es {max(marks)}")

def print_mean_module():
    module = input_module()
    if module != -1:
        marks = [student[module] for student in students]
        print(f"La nota media de {MODULES[module-1]} es {mean(marks)}")

def fill_students_randomly(n):
    for i in range(n):
        marks = [random.randint(0,1000)/100 for _ in range(4)]
        students.append([f"Estudiante {i+1}"] + marks)


# Programa principal
print("Gestión de calificaciones")
print("-------------------------")

students = []

input_marks()

while True:
    print("\nMenú de opciones para gestionar notas\n"
          "_____________________________________\n"
          "1. Impresión de las calificaciones del curso completo.\n"
          "2. Impresión de las calificaciones de un/a estudiante.\n"
          "3. Nota media de un módulo.\n"
          "4. Nota más alta en un módulo.\n"
          "5. Nota más baja en un módulo.\n"
          "6. Listado ordenado de los estudiantes respecto a su nota en un módulo (de mayor a menor).\n"
          "7. Finalizar.\n")

    option = int(input("Introduzca una opción: "))
    if option == 1:
        print_marks_course()
    elif option == 2:
        print_marks_student()
    elif option == 3:
        print_mean_module()
    elif option == 4:
        print_max_mark_module()
    elif option == 5:
        print_min_mark_module()
    elif option == 6:
        print_marks_module_sorted()
    elif option == 7:
        break
    else:
        print("\nLa opción introducida es errónea")

print("\n¡Hasta la próxima! :-)")