from e06POO1.Tanda1.Ejercicio4 import Dice


def dice_roll(value):
    for i in range(4):
        value.roll()
        print(value)


def show_face(dice):
    print(f"La cara con la que se inicializa el dado es {dice.show}")


dado1 = Dice()
show_face(dado1)
dice_roll(dado1)

dado2 = Dice(3)
show_face(dado2)
dice_roll(dado2)

dado3 = Dice(1, 10)
show_face(dado3)
dice_roll(dado3)

# dado4 = Dice(-1, 10)
# show_face(dado4)
# dice_roll(dado4)

dado5 = Dice(8)
show_face(dado5)
dice_roll(dado5)
