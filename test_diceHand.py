import unittest
from unittest.mock import MagicMock, patch
import random
from dice_Hand import DiceHand

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides

class Player:
    def __init__(self, difficulty_level=1):
        self.difficulty_level = difficulty_level
        self.score = 0

    def get_difficulty_level(self):
        return self.difficulty_level

    def add_score(self, score):
        self.score += score

    def reset_score(self):
        self.score = 0

class DiceHandTest(unittest.TestCase):
    def setUp(self):
        self.dice1 = Dice(6)
        self.dice2 = Dice(6)
        self.player = Player()
        self.dice_hand = DiceHand(self.dice1, self.dice2)

    def test_roll_pvi_easy(self):
        self.player.get_difficulty_level = MagicMock(return_value=1)
        with patch('random.randint', side_effect=[1, 6]):
            result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
            self.assertTrue(result)
            self.assertEqual(self.player.score, 7)

    def test_roll_pvi_easy_reset(self):
        self.player.get_difficulty_level = MagicMock(return_value=1)
        with patch('random.randint', side_effect=[1, 1]):
            result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
            self.assertFalse(result)
            self.assertEqual(self.player.score, 0)

    def test_roll_pvi_medium(self):
        self.player.get_difficulty_level = MagicMock(return_value=2)
        with patch('random.randint', side_effect=[3, 4]):
            result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
            self.assertTrue(result)
            self.assertEqual(self.player.score, 7)

    def test_roll_pvi_medium_reset(self):
        self.player.get_difficulty_level = MagicMock(return_value=2)
        with patch('random.randint', side_effect=[1, 1]):
            result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
            self.assertFalse(result)
            self.assertEqual(self.player.score, 0)

    def test_roll_pvi_hard(self):
        self.player.get_difficulty_level = MagicMock(return_value=3)
        with patch('random.randint', side_effect=[4, 5]):
            result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
            self.assertTrue(result)
            self.assertEqual(self.player.score, 9)

    def test_roll_pvi_hard_reset(self):
        self.player.get_difficulty_level = MagicMock(return_value=3)
        with patch('random.randint', side_effect=[1, 1]):
            result = self.dice_hand.roll_pvi(self.player, self.dice1, self.dice2)
            self.assertFalse(result)
            self.assertEqual(self.player.score, 0)

    def test_roll_pvp(self):
        with patch('random.randint', side_effect=[2, 3]):
            result = self.dice_hand.roll_pvp(self.player, self.dice1, self.dice2)
            self.assertTrue(result)
            self.assertEqual(self.player.score, 5)

    def test_roll_pvp_reset(self):
        with patch('random.randint', side_effect=[1, 1]):
            result = self.dice_hand.roll_pvp(self.player, self.dice1, self.dice2)
            self.assertFalse(result)
            self.assertEqual(self.player.score, 0)

if __name__ == '__main__':
    unittest.main()
