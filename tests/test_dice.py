import unittest
from unittest.mock import patch
from MyPackages.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        # Test that roll returns a value within the valid range
        with patch('random.randint', return_value=3):
            result = self.dice.roll()
            self.assertEqual(result, 3)

    def test_set_sides(self):
        # Test setting valid number of sides
        self.dice.set_sides(8)
        self.assertEqual(self.dice.get_sides(), 8)

        # Test setting invalid number of sides
        with self.assertRaises(ValueError):
            self.dice.set_sides(1)

    def test_get_current_value(self):
        # Test getting current value after rolling
        with patch('random.randint', return_value=4):
            self.dice.roll()
            self.assertEqual(self.dice.get_current_value(), 4)

    def test_get_sides(self):
        # Test getting number of sides
        self.assertEqual(self.dice.get_sides(), 6)

if __name__ == '__main__':
    unittest.main()
