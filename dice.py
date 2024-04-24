"""Module used to generate random numbers"""
import random


class Dice:
    """Class used to create a dice"""
    def __init__(self, sides=6):
        self.sides = sides
        self.current_value = None

    def roll(self):
        """Class used to roll a dice"""
        self.current_value = random.randint(1, self.sides)
        return self.current_value

    def get_current_value(self):
        """Function to get the current value"""
        return self.current_value

    def set_sides(self, num_sides):
        """Function to change the amount of sides"""
        if num_sides < 6:
            raise ValueError("Number of sides must be at least 6")
        self.sides = num_sides

    def get_sides(self):
        """Function to get the number of sides"""
        return self.sides
