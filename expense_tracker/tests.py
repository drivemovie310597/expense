# from django.test import TestCase
from unittest import TestCase

# Create your tests here.
def two_integer(a, b):
    return a + b  # TDD Practice


class Test(TestCase):
    def test_sum(self):
        self.assertEqual(two_integer(1, 2), 3)  # 3 is the expected result
