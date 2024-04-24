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

# Create a six-sided dice
my_dice = Dice()

# Roll the dice
result = my_dice.roll()
print("Result of the roll:", result)

# Get the current value
current_value = my_dice.get_current_value()
print("Current value of the dice:", current_value)

# Change the number of sides
my_dice.set_sides(12)

# Get the new number of sides
print("Number of sides after modification:", my_dice.get_sides())
