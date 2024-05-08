from unittest import TestCase
from Durationtest import Duration


class TestDuration(TestCase):
    def setUp(self):
        self.d1 = Duration(1, 0, 0)

    def test_add_seconds(self):
        self.d1.add_seconds(1)
        self.assertEqual(self.d1.seconds,  1)
        self.d1.add_seconds(60)
        self.assertEqual(self.d1.seconds and self.d1.minutes, 1)

    def test_sub_seconds(self):
        self.d2 = Duration(0, 0, 20)
        self.d2.sub_seconds(10)
        self.assertEqual(self.d2.seconds, 10)
        self.d2.sub_seconds(10)
        self.assertEqual(self.d2.seconds, 0)

    def test_add_minutes(self):
        self.d1.add_minutes(60)
        self.assertEqual(self.d1.minutes, 0)
        self.d1.add_minutes(120)
        self.assertEqual(self.d1.hours, 4)

    def test_sub_minutes(self):
        self.d2 = Duration(0, 10, 0)
        self.d2.sub_minutes(5)
        self.assertEqual(self.d2.minutes, 5)
        self.d2.sub_minutes(5)
        self.assertEqual(self.d2.minutes, 0)

    def test_add_hours(self):
        self.d1.add_hours(4)
        self.assertEqual(self.d1.hours, 5)

    def test_sub_hours(self):
        self.d1.sub_hours(1)
        self.assertEqual(self.d1.hours, 0)

    def tearDown(self):
        del self.d1
