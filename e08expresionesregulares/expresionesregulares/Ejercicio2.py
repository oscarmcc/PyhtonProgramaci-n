"""
Programa que reciba una url y el nombre de una etiqueta html. Si la url es válida debe mostrar por la pantalla el
contenido de cada etiqueta.

Ejemplo:

si ejecuto python miprograma https://www.iesgrancapitan.org/ title

La salida sería:

Centro Educativo IES Gran Capitán

Número de etiquetas encontradas: 1

ó si ejecuto python miprograma https://example.com/ p

La salida sería:

This domain is for use in illustrative examples in documents. You may use this domain in literature without
prior coordination or asking for permission.


<a href="https://www.iana.org/domains/example">More information...</a>

Número de etiquetas encontradas: 2

Author: Óscar Martín-Castaño Carrillo
"""
import requests
import sys
import xml.etree.ElementTree as ET


def encontrar_etiquetas(url, tag):
    try:
        response = requests.get(url)
        tree = ET.ElementTree(ET.fromstring(response.content))
        etiquetas = tree.findall(f'.//{tag}')
        for tag in etiquetas:
            print(tag.text.strip())
        print(f"Número de etiquetas encontradas: {len(etiquetas)}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python programa.py url etiqueta")
    else:
        url = sys.argv[1]
        etiqueta = sys.argv[2]
        encontrar_etiquetas(url, etiqueta)
