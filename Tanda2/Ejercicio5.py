"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
Obtener el número de elementos almacenados (tamaño).
Saber si la pila o la cola está vacía.
Vaciar completamente la pila o la cola.
Para el caso de la pila:
Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
Leer el elemento superior de la pila sin retirarlo (top).
Para el caso de la cola:
Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer
elemento que entró.
Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

Author: Óscar Martín-Castaño Carrillo
"""
from __future__ import annotations


class Data:
    def __init__(self, *items):
        self.__items = list(items)

    @classmethod
    def from_data(cls, other: Data):
        new_data = cls()
        new_data.__items = other.__items.copy()
        return new_data

    @property
    def items(self):
        return self.__items

    def get_size(self):
        return len(self.__items)

    def is_empty(self):
        return len(self.__items) == 0

    def empty(self):
        return self.__items == []


class Stack(Data):
    def __init__(self, stack):
        super().__init__(*stack)

    @property
    def stack(self):
        return self.items

    def push(self, item):
        return self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def read_top(self):
        return self.items[-1]

    def __str__(self):
        return f"Stack: {self.stack}"


class Queue(Data):
    def __init__(self, queue):
        super().__init__(*queue)

    @property
    def queue(self):
        return self.items

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    def read(self):
        return self.items[0]

    def __str__(self):
        return f"Queue: {self.queue}"


if __name__ == '__main__':
    stack1 = Stack((1, 2, 3, 4))
    stack1.push(3)
    print(stack1)
    print(stack1.pop())
    print(stack1.read_top())

    queue1 = Queue((1, 2, 3, 4))
    queue1.enqueue(4)
    print(queue1)
    print(queue1.dequeue())
    print(queue1.read())

    stack2 = Data.from_data(stack1)
    queue2 = Data.from_data(queue1)
    print(f"Creadas {stack2}, {queue2}")
