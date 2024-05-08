class Euclides:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mcd(self):
        if self.a < self.b:
            aux = self.a
            self.a = self.b
            self.b = aux
        num1 = self.a
        num2 = self.b
        resto = self.a % self.b
        while resto != 0:
            num1 = num2
            num2 = resto
            resto = num1 % num2
        return f'El MCD de {self.a} y {self.b} es {num2}'


salir = 's'
while salir == 's':
    n1 = int(input('Introduce el primer número para el algoritmo de Euclides: '))
    n2 = int(input('Introduce el segundo número para el algoritmo de Euclides: '))
    euclides = Euclides(n1, n2)
    print(euclides.mcd())
    salir = input('¿Desea volver a calcular el MCD de otros dos números? (s/n) ')
