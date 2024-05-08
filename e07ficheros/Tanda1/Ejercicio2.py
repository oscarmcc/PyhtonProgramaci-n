"""
Escribe un programa que sea capaz de leer el fichero anterior y lo muestre por la pantalla.

Author: Óscar Martín-Castaño Carrillo
"""

try:
    with open("primos.txt", "r") as file:
        print("Números primos en el archivo primos.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo primos.txt")
except IOError:
    print("Error: No se pudo leer el archivo primos.txt")
