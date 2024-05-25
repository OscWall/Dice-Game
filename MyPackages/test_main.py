"""Usertest"""
import unittest
from main import Main


class TestIntelligence(unittest.TestCase):
    """Class used to test functions inside main"""
    def test_input_choice_letter(self):
        self.assertFalse(Main.input_choice("f"))

    def test_input_choice_wrong_number(self):
        self.assertFalse(Main.input_choice(4))

    def test_input_choice_correct_number(self):
        self.assertTrue(Main.input_choice(1))
    
    def test_difficulty_level_letter(self):
        self.assertFalse(Main.input_difficulty_level("f"))

    def test_input_difficulty_level_wrong_number(self):
        self.assertFalse(Main.input_choice(4))

    def test_input_difficulty_level_correct_number(self):
        self.assertTrue(Main.input_choice(1))

if __name__ == "__main__":
    unittest.main()
