"""Module used for testing"""
import unittest
from intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """Class used to test the function inside the Intelligence class"""
    def setUp(self):
        name = "Alex"
        score = 0
        difficulty_level = 1
        self.cpu = Intelligence(name, score, difficulty_level)

    def test_get_name(self):
        """Test for the get_name function"""
        self.cpu.set_name("John")
        self.assertEqual("John", self.cpu.get_name())

    def test_get_score(self):
        """Test for the get_score function"""
        self.cpu.set_score(20)
        self.assertEqual(20, self.cpu.get_score())

    def test_get_difficulty_level(self):
        """Test for the get_difficulty_level function"""
        self.cpu.set_difficulty_level(2)
        self.assertEqual(2, self.cpu.get_difficulty_level())

    def test_set_name(self):
        """Test for the set_name function"""
        name = self.cpu.get_name()
        self.cpu.set_name("Oscar")
        new_name = self.cpu.get_name()
        self.assertNotEqual(name, new_name)

    def test_set_score(self):
        """Test for the get_score function"""
        score = self.cpu.get_score()
        self.cpu.set_score(1)
        new_score = self.cpu.get_score()
        self.assertNotEqual(score, new_score)

    def test_set_difficulty_level(self):
        """Test for the set_difficulty_level function"""
        score = self.cpu.get_difficulty_level()
        self.cpu.set_difficulty_level(2)
        difficulty_level = self.cpu.get_difficulty_level()
        self.assertNotEqual(score, difficulty_level)

    def test_reset_score(self):
        """Test for the reset_score function"""
        score = self.cpu.reset_score()
        self.assertEqual(score, 0, "The score hasn't been reset")

    def test_add_score(self):
        """Test for the add_score function"""
        score = 5
        self.cpu.add_score(score)
        self.assertEqual(score, self.cpu.get_score())


if __name__ == "__main__":
    unittest.main()
