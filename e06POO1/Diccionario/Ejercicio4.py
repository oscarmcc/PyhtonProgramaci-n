"""
Realiza un programa que escoja al azar 5 palabras en español del mini-diccionario del ejercicio anterior.
El programa irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y comprobará si
son correctas. Al final, el programa deberá mostrar cuántas respuestas son válidas y cuántas erróneas.
"""
from Ejercicio3 import dictionary
import random

NUM_QUESTIONS = 5

correct_answer = 0
spanish_words = tuple(dictionary.keys())
test_word = set()

while len(test_word) < NUM_QUESTIONS:
    word = random.choice(spanish_words)
    test_word.add(word)

for word in test_word:
    translation = input(f"Ingrese la traducción que creas que es la correcta para la palabra {word}: ").lower()
    if dictionary[word].lower() == translation:
        correct_answer += 1
        print(f"Correcto")
    else:
        print(f"Incorrecto")
print(f"De las {NUM_QUESTIONS} palabras has acertado {correct_answer}, "
      f"pero has fallado {NUM_QUESTIONS - correct_answer}")
