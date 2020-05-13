import unittest
from Part2 import randomgame


class testgame(unittest.TestCase):
    def test_input(self):
        self.assertTrue(randomgame.run_guess(5, 5))

    def test_input1(self):
        self.assertFalse(randomgame.run_guess(5, 4))


if __name__ == '__main__':
    unittest.main()

