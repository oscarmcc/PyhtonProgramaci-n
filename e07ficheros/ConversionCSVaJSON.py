"""
Utilidad: conversor de CSV a JSON

Recibe como parámetro un CSV (un argumento con extensión .csv)
Si no recibe esto, error

Resultado es un fichero JSON con el mismo nombre pero con extensión JSON

--> csv2json
"""

import sys
import csv
import json


def csv_to_json(csv_file):
    if not csv_file.endswith('.csv'):
        print("Error: El archivo de entrada debe tener extensión .csv")
        return

    json_file = csv_file.replace('.csv', '.json')

    try:
        with open(csv_file, 'rt') as f:
            csv_data = csv.DictReader(f)
            data = list(csv_data)

        with open(json_file, 'wt') as f:
            json.dump(data, f, indent=4)

        print(f"Se ha convertido '{csv_file}' a '{json_file}' exitosamente.")

    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except IOError:
        print("Error: No se pudo leer el archivo CSV")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python csv2json.py <archivo_csv>")
        sys.exit(1)

    csv_file = sys.argv[1]
    csv_to_json(csv_file)
