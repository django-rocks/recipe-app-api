from django.test import TestCase

from app.calc import add

class CalcTests(TestCase):

    def tests_add_numbers(self):
        """Test where two numbers are added together"""
        self.assertEqual(add(3, 8), 11)
