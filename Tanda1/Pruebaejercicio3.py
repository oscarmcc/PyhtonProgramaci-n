from e06POO1.Tanda1 import Ejercicio3 as e3

point1 = e3.Point(20, 8)
point2 = e3.Point(6, 2)

rectangle1 = e3.Rectangle(point1, point2)
print(f"El area del rectángulo es {rectangle1.get_area()}\n"
      f"El perimetro del rectángulo es {rectangle1.get_perimeter()}")

point3 = e3.Point(2, 7)
rectangle2 = e3.Rectangle(point3, point1)
print(f"El area del rectángulo es {rectangle2.get_area()}\n"
      f"El perimetro del rectángulo es {rectangle2.get_perimeter()}")
