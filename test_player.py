"""Usertest"""
import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    """Unit tests for all functions in the Player class"""
    def setUp(self):
        self.name = "Alex"
        self.score = 0
        self.difficulity_level = 1
        self.player = Player(self.name, self.score, self.difficulity_level)

    def test_get_name(self):
        """Test for the get_name function"""
        self.player.set_name("John")
        self.assertEqual("John", self.player.get_name())

    def test_get_score(self):
        """Test for the get_score function"""
        self.player.set_score(20)
        self.assertEqual(20, self.player.get_score())

    def test_get_difficulty_level(self):
        """Test for the get_difficulty_level function"""
        self.player.set_difficulty_level(2)
        self.assertEqual(2, self.player.get_difficulty_level())

    def test_set_name(self):
        """Test for the set_name function"""
        name = self.player.get_name()
        self.player.set_name("Oscar")
        new_name = self.player.get_name()
        self.assertNotEqual(name, new_name)

    def test_set_score(self):
        """Test for the get_score function"""
        score = self.player.get_score()
        self.player.set_score(1)
        new_score = self.player.get_score()
        self.assertNotEqual(score, new_score)

    def test_set_difficulty_level(self):
        """Test for the set_difficulty_level function"""
        score = self.player.get_difficulty_level()
        self.player.set_difficulty_level(2)
        difficulty_level = self.player.get_difficulty_level()
        self.assertNotEqual(score, difficulty_level)

    def test_reset_score(self):
        """Test for the reset_score function"""
        score = self.player.reset_score()
        self.assertEqual(score, 0, "The score hasn't been reset")


if __name__ == "__main__":
    unittest.main()
