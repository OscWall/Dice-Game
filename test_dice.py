import unittest
from dice import Dice

class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice()
        result = dice.roll()
        self.assertTrue(1 <= result <= dice.get_sides())

    def test_set_sides(self):
        # Test setting valid number of sides
        dice = Dice()
        dice.set_sides(8)
        self.assertEqual(dice.get_sides(), 8)

        # Test setting invalid number of sides
        with self.assertRaises(ValueError):
            dice.set_sides(1)

    def test_get_current_value(self):
        # Test getting current value after rolling
        dice = Dice()
        result = dice.roll()
        self.assertEqual(dice.get_current_value(), result)

if __name__ == '__main__':
    unittest.main()
