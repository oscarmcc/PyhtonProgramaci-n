"""
Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la compra.
Crea la clase ShoppingCart. Al carrito se le pueden ir agregando elementos que se guardarán en una lista, por tanto,
deberás crear la clase Element. Cada elemento del carrito deberá contener el nombre del producto, su precio y la
cantidad (número de unidades de dicho producto). A continuación se muestra tanto el contenido del programa principal
como la salida que debe mostrar el programa. Los métodos a implementar se pueden deducir del programa principal.
"""


class Element:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, element):
        self.items.append(element)

    @property
    def size(self):
        return len(self.items)

    def total_prize(self):
        return sum(item.subtotal() for item in self.items)

    def __str__(self):
        output = "Contenido del carrito\n=====================\n"
        for item in self.items:
            output += f"{item.product_name} PVP: {item.price:.2f} Unidades: {item.quantity} Subtotal: {item.subtotal():.2f}\n"
        output += f"Hay {self.size} productos en la cesta.\n"
        output += f"El total asciende a {self.total_prize():.2f} euros"
        return output


mi_carrito = ShoppingCart()
mi_carrito.add(Element("Tarjeta SD 64Gb", 19.95, 2))
mi_carrito.add(Element("Canon EOS 2000D", 449, 1))
print(mi_carrito)
print(f"Hay {mi_carrito.size} productos en la cesta.")
print(f"El total asciende a {mi_carrito.total_prize():.2f} euros")

print("\nContinúa la compra...\n")
mi_carrito.add(Element("Samsung Galaxy Tab", 199, 3))
mi_carrito.add(Element("Tarjeta SD 64Gb", 19.95, 1))
print(mi_carrito)
print(f"Ahora hay {mi_carrito.size} productos en la cesta.")
print(f"El total asciende a {mi_carrito.total_prize():.2f} euros")
