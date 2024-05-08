from unittest import TestCase
from Calculadoratest import Calculator


class TestCalculator1(TestCase):
    # Este método se ejecuta antes de cada prueba
    def setUp(self):
        self.calc = Calculator()

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(13, 3), 11)

    # Liberamos memoria física de la instancia
    def tearDown(self):
        del self.calc
