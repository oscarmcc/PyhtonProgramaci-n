"""
Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor (de un conjunto
de valores).
CardPlayer que simule un jugador de naipes. Un jugador tiene un nombre y un conjunto de naipes.
Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
Puede deshacerse de una carta.
Puede recibir cartas.
Deck que simula un conjunto de cartas de naipes.
Inicialmente tiene las cartas que le llegan con el constructor.
Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
Le pueden quitar la primera carta (robar).
Puede barajarse.
Podemos saber cuantas cartas hay en la baraja.
Baraja Española e Inglesa (SpanishDeck e EnglishDeck) que heredan de Deck.

Author: Óscar Martín-Castaño Carrillo
Date: 04/03/2024
"""

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} de {self.suit}"


class CardPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def discard_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        else:
            return None

    def draw_card(self, deck):
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        return card

    def __str__(self):
        return f"{self.name}: {', '.join(str(card) for card in self.hand)}"


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            return None

    def shuffle(self):
        random.shuffle(self.cards)

    def cards_left(self):
        return len(self.cards)


class SpanishDeck(Deck):
    def __init__(self):
        suits = ['Oros', 'Copas', 'Espadas', 'Bastos']
        values = ['As', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']
        cards = [Card(suit, value) for suit in suits for value in values]
        super().__init__(cards)


class EnglishDeck(Deck):
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        cards = [Card(suit, value) for suit in suits for value in values]
        super().__init__(cards)
