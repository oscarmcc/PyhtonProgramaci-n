from unittest import TestCase
import unittest

from Numeros import Numeros


class TestNumeros(TestCase):

    def setUp(self):
        self.numeros = Numeros()

    def test_primo(self):
        assert self.numeros.primo(13)
        assert not self.numeros.primo(4)

    def test_potencia(self):
        self.assertEqual(self.numeros.potencia(5, 10), 9765625)
        self.assertEqual(self.numeros.potencia(3, 0), 1)
        self.assertEqual(self.numeros.potencia(0, 0), "Indeterminacion")
        self.assertEqual(self.numeros.potencia(0, 77), 0)

    def test_fibonacci(self):
        self.assertEqual(self.numeros.fibonnacci(1), 1)
        self.assertEqual(self.numeros.fibonnacci(0), 0)
        self.assertEqual(self.numeros.fibonnacci(-69), 0)
        self.assertEqual(self.numeros.fibonnacci(100), 354224848179261915075)

    def test_perfecto(self):
        assert self.numeros.perfecto(28)
        assert self.numeros.perfecto(6)
        assert not self.numeros.perfecto(27)
        assert self.numeros.perfecto(8128)
        assert not self.numeros.perfecto(73)
        assert not self.numeros.perfecto(1)
        assert not self.numeros.perfecto(0)
        # 0 is not considered a perfect number.
        # So 1 failure is going to be expected and assumed. The test has done its job detecting it.

    def mytest(self):
        self.test_primo()
        self.test_potencia()
        self.test_fibonacci()
        self.test_perfecto()

    def tearDown(self):
        del self.numeros


if __name__ == '__main__':
    unittest.main()
