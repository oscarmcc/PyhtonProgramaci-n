"""
 Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero.
 Tanto el nombre del fichero como la palabra se deben pasar como argumentos en la línea de comandos.

 Author: Óscar Martín-Castaño Carrillo
"""
import sys


def count_word_occurrences(file_name, word):
    try:
        with open(file_name, 'r') as f:
            text = f.read()
            occurrences = text.count(word)
            print(f"La palabra '{word}' aparece {occurrences} veces en '{file_name}'")

    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except IOError:
        print("Error: No se pudo leer el archivo")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python contar_ocurrencias.py <archivo> <palabra>")
        sys.exit(1)

    file_name = sys.argv[1]
    word = sys.argv[2]

    count_word_occurrences(file_name, word)
