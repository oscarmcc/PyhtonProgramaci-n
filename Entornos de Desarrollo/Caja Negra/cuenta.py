import random


class Cuenta:
    codigo = 0
    saldo = 0

    def __init__(self, saldoinicial):
        self.codigo = random.randint(1, 1000000000)
        self.saldo = saldoinicial

    def reintegro(self, cantidad):
        if cantidad > self.saldo:
            print("ERROR. No se ha podido realizar el reintegro")
            return False
        self.saldo -= cantidad

    def ingreso(self, cantidad):
        self.saldo += cantidad

    def transferencia(self, dinero, cuenta):
        if self.saldo < dinero:
            print("ERROR. No se ha podido realizar el reintegro")
            return False
        self.setSaldo(self.saldo - dinero)
        cuenta.setSaldo(cuenta.getSaldo() + dinero)

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

    def mostrar(self):
        return f'Cuenta: {self.codigo}, saldo: {self.saldo}'
