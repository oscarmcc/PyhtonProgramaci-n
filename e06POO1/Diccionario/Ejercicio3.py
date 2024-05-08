"""
Crea un mini-diccionario español-inglés que contenga, al menos, 20 palabras (con su correspondiente traducción).
Utiliza un diccionario para almacenar las parejas de palabras. El programa pedirá una palabra en español y dará
la correspondiente traducción en inglés.
"""
dictionary = {"puerta": "door", "ventana": "window", "ordenador": "computer", "pelo": "hair", "luna": "moon",
              "mascota": "pet", "perro": "dog", "gato": "cat", "vaca": "cow", "caballo": "horse", "coche": "car",
              "árbol": "tree", "océano": "ocean", "camiseta": "T-Shirt", "silla": "chair", "lunes": "Monday",
              "martes": "Tuesday", "jueves": "thursday", "viernes": "friday", "domingo": "Sunday", "leche": "milk"}
while True:
    word = input("Ingrese una palabra para ver su traducción: ").lower()
    if word in dictionary:
        print(dictionary[word])
    else:
        translation = input("No existe la palabra por favor introduce la traducción en inglés: ")
        dictionary[word] = translation
