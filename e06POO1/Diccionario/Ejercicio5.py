"""
Escribe un programa que genere una secuencia de 5 cartas de la baraja española y que sume los puntos según
el juego de la brisca. El valor de las cartas se debe guardar en un diccionario que debe contener
parejas (figura, valor), por ejemplo (“caballo”, 3). La secuencia de cartas debe ser una lista que contiene objetos
de la clase Carta. El valor de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el
resto de cartas no vale nada.
"""
import random


class Carta:
    def __init__(self, figure):
        self.figure = figure


def generate_card():
    figuras = ["as", "dos", "tres", "cuatro", "cinco", "seis", "siete", "sota", "caballo", "rey"]
    figura = random.choice(figuras)
    return Carta(figura)


def calculate_points(card):
    valores = {
        "as": 11,
        "tres": 10,
        "sota": 2,
        "caballo": 3,
        "rey": 4
    }
    points = 0
    for card_points in card:
        if card_points.figure in valores:
            points += valores[card_points.figure]
    return points


secuencia_cartas = [generate_card() for _ in range(5)]
print("Secuencia de cartas generada:")
for i, carta in enumerate(secuencia_cartas, start=1):
    print(f"Carta {i}: {carta.figure}")
puntos = calculate_points(secuencia_cartas)
print(f"Puntos totales: {puntos}")
