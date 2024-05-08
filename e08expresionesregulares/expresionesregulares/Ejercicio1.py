"""
Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va extraer del
mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

DNI: extrae los DNIs.
IP: extrae las direcciones IP.
MAT: extrae matrículas de coche con formato 0000XXX.
HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza con #.
FEC: extrae fechas con formato dd/mm/aaaa.
TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayusculas y minusculas, numeros,
guiones y guiones bajos.
El programa tiene que ser en relación a su complejidad y número de líneas lo más eficiente posible.

Author: Óscar Martín-Castaño Carrillo
"""

import re
import sys


def extract_information(archive, type):
    # Expresiones regulares para cada tipo de información
    regex = {
        'DNI': r'\b\d{8}[A-HJ-NP-TV-Z]\b',
        'IP': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        'MAT': r'\b\d{4}[A-Z]{3}\b',
        'HEX': r'\b#[0-9A-F]+\b',
        'FEC': r'\b\d{2}/\d{2}/\d{4}\b',
        'TWT': r'\B@[\w-]+\b'
    }

    if type in regex:
        # Leer el archivo
        with open(archive, 'r') as file:
            data = file.read()
        # Encontrar coincidencias utilizando la expresión regular
        matches = re.findall(regex[type], data)
        # Mostrar los datos extraídos
        for match in matches:
            print(match)
    else:
        print("Tipo de información no válido")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python programa.py archivo.txt tipo_de_informacion")
    else:
        archivo = sys.argv[1]
        tipo = sys.argv[2]
        extract_information(archivo, tipo)
