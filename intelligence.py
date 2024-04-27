"""No module"""


class Intelligence:
    """Class used to create a cpu"""
    def __init__(self, name, score, difficulty_level):
        self.name = name
        self.score = score
        self.difficulty_level = difficulty_level

    def get_name(self):
        """Function that returns the name"""
        return f"{self.name}"

    def set_name(self, name):
        """Function that changes the name"""
        self.name = name

    def get_score(self):
        """Function that returns the score"""
        return self.score

    def set_score(self, score):
        """Function that changes the score"""
        self.score = score

    def get_difficulty_level(self):
        """Function that returns the difficulty level"""
        return self.difficulty_level

    def set_difficulty_level(self, difficulty_level):
        """Function changes the difficulty level
        if the difficulty level isn't above 3"""
        if difficulty_level > 3:
            raise ValueError("Difficulty level can not be over hard")
        else:
            self.difficulty_level = difficulty_level

    def reset_score(self):
        """Function resets the score to 0"""
        self.score = 0
        return self.score
