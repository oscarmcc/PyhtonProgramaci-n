"""
1. Escribe un programa que guarde en un fichero con nombre primos.txt los números primos que hay entre 1 y 500.

Author: Óscar Martín-Castaño Carrillo
"""


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


try:
    with open("primos.txt", "w") as file:
        for num in range(1, 501):
            if es_primo(num):
                file.write(f"{num}\n")
    print("Los números primos se han guardado correctamente en primos.txt")
except IOError:
    print("Error: No se pudo escribir en el archivo primos.txt")
