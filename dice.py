import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.current_value = None

    def roll(self):
        self.current_value = random.randint(1, self.sides)
        return self.current_value

    def get_current_value(self):
        return self.current_value

    def set_sides(self, num_sides):
        if num_sides < 2:
            raise ValueError("Number of sides must be at least 2")
        self.sides = num_sides

    def get_sides(self):
        return self.sides