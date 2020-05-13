import unittest
from unittest import TestCase

from Part1 import Assignments


class Test(TestCase):
    def test_assign(self):
        num = 10
        result = Assignments.checkDriverAge(num)
        self.assertEqual(result, 'Sorry, you are too young to drive this car. Powering off')

    def test_assign1(self):
        num = 'asdasdasd'
        result = Assignments.checkDriverAge(num)
        self.assertTrue(isinstance(result, ValueError))


if __name__ == '__main__':
    unittest.main()
