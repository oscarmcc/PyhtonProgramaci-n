from Actividad5 import DiceCup
from Actividad1 import Dice
from Actividad3 import LudoDice
from Actividad2 import PokerDice

cup = DiceCup(LudoDice(), PokerDice(), Dice('X', 'Y', 'Z'))
print(f"Creado cubilete de dados: {cup} con {cup.size} dados")

d = Dice(100, 200, 300)
cup.add(d)
print(f"Cubilete después de haber añadido el dado {d}: {cup}. Tamaño {cup.size}")

cup.remove(d)
print(f"Cubilete después de haber borrado el dado {d}: {cup}. Tamaño {cup.size}")

input(f"Y si volvemos a borrar {d} del cubilete saltará una excepción. Pulsa Intro para seguir...")
cup.remove(d)
