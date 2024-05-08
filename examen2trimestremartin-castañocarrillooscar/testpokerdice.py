from Actividad2 import PokerDice

dice = PokerDice()
print(f"Tiro cinco veces el dado {repr(dice)}:")
for i in range(5):
    dice.roll()
    print(f"Tirada {i+1}: {dice} con puntuación {dice.score}")
