"""
Utilidad: conversor de JSON a CSV

Recibe como parámetro un JSON (un argumento con extensión .json)
Si no recibe esto, error

Resultado es un fichero CSV con el mismo nombre pero con extensión csv

--> json2csv
"""
import sys
import json
import csv


def json_to_csv(json_file):
    if not json_file.endswith('.json'):
        print("Error: El archivo de entrada debe tener extensión .json")
        return

    csv_file = json_file.replace('.json', '.csv')

    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"Se ha convertido '{json_file}' a '{csv_file}' exitosamente.")

    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except IOError:
        print("Error: No se pudo leer el archivo JSON")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python json2csv.py <archivo_json>")
        sys.exit(1)

    json_file = sys.argv[1]
    json_to_csv(json_file)
