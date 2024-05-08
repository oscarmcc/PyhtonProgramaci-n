"""
Realiza un programa que sea capaz de ordenar alfabéticamente las palabras contenidas en un fichero de texto.
El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos. El nombre
del fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo palabras_sort.txt .
Suponemos que cada palabra ocupa una línea.

Author: Óscar Martín-Castaño Carrillo
"""
import sys


def sort_words(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            words = f.readlines()
            words.sort()

        with open(output_file, 'w') as f:
            f.writelines(words)

        print(f"Palabras ordenadas correctamente en '{output_file}'")

    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except IOError:
        print("Error: No se pudo leer o escribir en el archivo")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ordenar_palabras.py <archivo_entrada>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '_sort.txt'

    sort_words(input_file, output_file)
