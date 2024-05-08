"""
 Escribe un programa capaz de quitar los comentarios de un programa de Java.

Se utilizaría de la siguiente manera:

python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>

Por ejemplo:

python quita-comentarios.py Holav1.java Holav2.java

crea un fichero con nombre Holav2.java que contiene el código de Holav1.java pero sin los comentarios.
"""

import sys


def remove_comments(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        cleaned_lines = [line.split('//')[0].rstrip() + '\n' for line in lines if '//' in line]

        with open(output_file, 'w') as f:
            f.writelines(cleaned_lines)

        print(f"Comentarios eliminados correctamente en '{output_file}'")

    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except IOError:
        print("Error: No se pudo leer o escribir en el archivo")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python quita_comentarios.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    remove_comments(input_file, output_file)
