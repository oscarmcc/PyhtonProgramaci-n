x = int(input("Introduzca un número: "))
y = int(input("Introduzca un segundo número: "))
z = int(input("Introduzca un tercer número: "))
if x < y:
    if x < z:
        menor = x
    else:
        menor = z
elif z < y:
    menor = z
else:
    menor = y
print("El menor es", menor)
