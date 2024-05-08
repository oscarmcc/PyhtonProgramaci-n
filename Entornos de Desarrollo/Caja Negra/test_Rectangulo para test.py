from unittest import TestCase
from Rectanguloparatest import Rectangle
from POINTparaRectangulo import Point


class TestRectangle(TestCase):
    def setUp(self):
        self.p1 = Point(2, 2)
        self.p2 = Point(5, 5)
        self.rectangle = Rectangle(self.p1, self.p2)
        self.p3 = Point(-1, 0)
        self.p4 = Point(0, -1)
        self.rectangle2 = Rectangle(self.p3, self.p4)

    def test_area(self):
        self.assertEqual(self.rectangle.area, 9)
        self.assertEqual(self.rectangle2.area, 1)

    def test_perimeter(self):
        self.assertEqual(self.rectangle.perimeter, 12)
        self.assertEqual(self.rectangle2.perimeter, 4)

    def tearDown(self):
        del self.rectangle
