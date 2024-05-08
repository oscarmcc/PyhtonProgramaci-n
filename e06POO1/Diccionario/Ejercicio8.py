"""
Mejora el programa anterior (en otro diferente) de tal forma que al intentar agregar un elemento al carrito,
se compruebe si ya existe el producto y, en tal caso, se incremente el número de unidades sin añadir un nuevo
elemento. Observa que en el programa anterior, se repetía el producto “Tarjeta SD 64Gb” dos veces en el carrito.
En esta nueva versión ya no sucede esto, sino que se incrementa el número de unidades del producto que se agrega.
El contenido del programa principal es idéntico al ejercicio anterior.
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

    def add_item(self, product_name, price, quantity):
        for item in self.items:
            if item.product_name == product_name:
                item.quantity += quantity
                return
        item = Element(product_name, price, quantity)
        self.items.append(item)

    def total(self):
        return sum(item.subtotal() for item in self.items)

    def size(self):
        return len(self.items)

    def __str__(self):
        output = "Contenido del carrito\n=====================\n"
        for item in self.items:
            output += (f"{item.product_name} PVP: {item.price:.2f} Unidades: {item.quantity} "
                       f"Subtotal: {item.subtotal():.2f}\n")
        output += f"Hay {self.size()} productos en la cesta.\n"
        output += f"El total asciende a {self.total():.2f} euros"
        return output


# Programa principal
mi_carrito = ShoppingCart()
mi_carrito.add_item("Tarjeta SD 64Gb", 19.95, 2)
mi_carrito.add_item("Canon EOS 2000D", 449, 1)
print(mi_carrito)
print("\nContinúa la compra...\n")
mi_carrito.add_item("Samsung Galaxy Tab", 199, 3)
mi_carrito.add_item("Tarjeta SD 64Gb", 19.95, 1)
print(mi_carrito)
