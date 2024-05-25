import unittest
from unittest.mock import MagicMock, patch
import random
from diceHand import DiceHand

class TestDiceHand(unittest.TestCase):
    def setUp(self):
        self.dice1 = MagicMock()
        self.dice2 = MagicMock()
        self.dice_hand = DiceHand(self.dice1, self.dice2)
        self.player = MagicMock()

    @patch('random.randint')
    def test_roll_pvi_easy(self, mock_randint):
        self.player.get_difficulty_level = MagicMock(return_value=1)
        self.dice1.get_sides = MagicMock(return_value=6)
        self.dice2.get_sides = MagicMock(return_value=6)

        # Mock random.randint to return 1 for both dice
        mock_randint.side_effect = [1, 1]

        result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
        print("test_roll_pvi_easy: result =", result)  # Debugging line
        self.assertFalse(result)  # With mocked values, it should return False

    @patch('random.randint')
    def test_roll_pvi_medium(self, mock_randint):
        self.player.get_difficulty_level = MagicMock(return_value=2)
        self.dice1.get_sides = MagicMock(return_value=6)
        self.dice2.get_sides = MagicMock(return_value=6)

        # Mock random.randint to return 4 and 5 for dice
        mock_randint.side_effect = [4, 5]

        result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
        self.assertTrue(result)  # With mocked values, it should return True

    @patch('random.randint')
    def test_roll_pvi_hard(self, mock_randint):
        self.player.get_difficulty_level = MagicMock(return_value=3)
        self.dice1.get_sides = MagicMock(return_value=6)
        self.dice2.get_sides = MagicMock(return_value=6)

        # Mock random.randint to return 5 and 6 for dice
        mock_randint.side_effect = [5, 6]

        result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
        self.assertTrue(result)  # With mocked values, it should return True

    @patch('random.randint')
    def test_roll_pvp(self, mock_randint):
        self.dice1.get_sides = MagicMock(return_value=6)
        self.dice2.get_sides = MagicMock(return_value=6)

        # Mock random.randint to return 2 and 3 for dice
        mock_randint.side_effect = [2, 3]

        result = self.dice_hand.roll_pvp(self.player, self.dice1, self.dice2)
        self.assertTrue(result)  # With mocked values, it should return True

    @patch('random.randint')
    def test_roll_or_not(self, mock_randint):
        # Mock random.randint to return 1
        mock_randint.side_effect = [1]

        result = self.dice_hand.roll_or_not()
        self.assertIn(result, [1, 2])  # Should return either 1 or 2

if __name__ == '__main__':
    unittest.main()
