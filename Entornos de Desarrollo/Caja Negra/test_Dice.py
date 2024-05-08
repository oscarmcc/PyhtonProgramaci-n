from unittest import TestCase
from Dice import Dice


class TestDice(TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_show_(self):
        self.dice3 = Dice(-1)
        self.dice4 = Dice(7)
        self.assertFalse(self.dice3.show_(-1))
        self.assertFalse(self.dice4.show_(7))

    def test_faces_(self):
        self.assertEqual(self.dice.faces, 6)
        self.dice2 = Dice(0, -1)
        self.assertFalse(self.dice2.faces_(-1))

    def test_roll(self):
        self.assertIn(self.dice.roll(), (None, 1, 2, 3, 4, 5, 6))
        self.dice5 = Dice(0, 4)
        self.assertIn(self.dice5.roll(), (None, 1, 2, 3, 4, 5))
        self.dice6 = Dice(0, 10)
        self.assertIn(self.dice6.roll(), (None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def tearDown(self):
        del self.dice
