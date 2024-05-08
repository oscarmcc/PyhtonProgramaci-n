"""
Escribe un programa que guarde en un fichero el contenido de otros dos ficheros,
de tal forma que en el fichero resultante aparezcan las líneas de los primeros dos ficheros mezcladas, es decir,
la primera línea será del primer fichero, la segunda será del segundo fichero, la tercera será la siguiente del primer
fichero, etc.

Author: Óscar Martín-Castaño Carrillo
"""
import sys


def merge_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        merged_lines = [line1.strip() + '\n' + line2.strip() for line1, line2 in zip(lines1, lines2)]

        with open(output_file, 'w') as f:
            f.writelines(merged_lines)

        print(f"Líneas mezcladas y guardadas correctamente en '{output_file}'")

    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except IOError:
        print("Error: No se pudo leer o escribir en el archivo")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python mezclar_archivos.py <archivo_1> <archivo_2> <archivo_salida>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]

    merge_files(file1, file2, output_file)
