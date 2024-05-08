from unittest import TestCase
from cuenta import Cuenta


class TestCuenta(TestCase):

    def setUp(self):
        self.cuenta = Cuenta(1000)

    def test_reintegro(self):
        self.cuenta.reintegro(323)
        self.assertEqual(self.cuenta.getSaldo(), 677)
        self.cuenta.reintegro(177)
        self.assertEqual(self.cuenta.getSaldo(), 500)
        self.cuenta.reintegro(500)
        self.assertEqual(self.cuenta.getSaldo(), 0)
        self.assertFalse(self.cuenta.reintegro(1))
        self.assertEqual(self.cuenta.getSaldo(), 0)

    def test_ingreso(self):
        self.cuenta.ingreso(3000)
        self.assertEqual(self.cuenta.getSaldo(), 4000)

    def test_transferencia(self):
        self.cuenta2 = Cuenta(3333)
        self.cuenta2.transferencia(333, self.cuenta)
        self.assertEqual(self.cuenta2.getSaldo(), 3000)
        self.assertEqual(self.cuenta.getSaldo(), 1333)

        self.cuenta2.transferencia(3001, self.cuenta)
        self.assertEqual(self.cuenta2.getSaldo(), 3000)
        self.assertEqual(self.cuenta.getSaldo(), 1333)
        self.assertFalse(self.cuenta2.transferencia(3001, self.cuenta))

    # def test_get_saldo(self):
    #   self.fail()

    # def test_set_saldo(self):
    #    self.fail()

    # def test_mostrar(self):
    #   self.fail()

    def tearDown(self):
        del self.cuenta
