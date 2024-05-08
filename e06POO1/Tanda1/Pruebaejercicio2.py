from e06POO1.Tanda1.Ejercicio2 import Point

point1 = Point(10, 5)
print(point1)

point2 = Point(8, 9)
print(point2)
point2.invert_coordinates()
print(point2)

point3 = Point(9, 5)
print(point3)
point3.x = 0    # Llama al setter
print(point3)
point3.invert_coordinates()
print(point3)
