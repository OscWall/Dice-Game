"""No module"""


class Player:
    """Class representing a player"""
    def __init__(self, name, score, difficulty_level):
        self.name = name
        self.score = score
        self.difficulty_level = difficulty_level

    def get_name(self):
        """Function returns the name of the player"""
        return f"{self.name}"

    def set_name(self, name):
        """Function changes the name of the player"""
        self.name = name

    def get_score(self):
        """Function returns the score of the player"""
        return self.score

    def set_score(self, score):
        """Function changes the score of the player"""
        self.score = score

    def get_difficulty_level(self):
        """Function returns the difficulty level"""
        return self.difficulty_level

    def set_difficulty_level(self, difficulty_level):
        """Function changes the difficulty level"""
        self.difficulty_level = difficulty_level

    def reset_score(self):
        """Function resets the score of the player """
        self.score = 0
        return self.score

    def add_score(self, score_to_be_added):
        self.score += score_to_be_added
