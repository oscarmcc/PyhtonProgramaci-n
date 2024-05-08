"""
Realiza un programa que escoja al azar 10 cartas de la baraja española (10 objetos de la clase Card).
Emplea una lista para almacenarlas y asegúrate de que no se repite ninguna. Las cartas se deben mostrar ordenadas.
Primero se ordenarán por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se ordenará por
número: as, 2, 3, 4, 5, 6, 7, sota, caballo, rey.
"""
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} de {self.suit}"


def create_spanish_deck():
    suits = ['Oros', 'Copas', 'Espadas', 'Bastos']
    values = ['As', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']
    deck = [Card(suit, value) for suit in suits for value in values]
    return deck


def select_random_cards(deck, num_cards):
    selected_cards = []
    while len(selected_cards) < num_cards:
        card = random.choice(deck)
        if card not in selected_cards:
            selected_cards.append(card)
    return selected_cards


def sort_cards(cards):
    suits_order = {'Bastos': 0, 'Copas': 1, 'Espadas': 2, 'Oros': 3}
    values_order = {'As': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 'Sota': 8, 'Caballo': 9, 'Rey': 10}
    cards.sort(key=lambda card: (suits_order[card.suit], values_order[card.value]))
    return cards


spanish_deck = create_spanish_deck()

selected_cards = select_random_cards(spanish_deck, 10)

sorted_cards = sort_cards(selected_cards)

print("Las 10 cartas seleccionadas de la baraja española son:")
for card in sorted_cards:
    print(card)
