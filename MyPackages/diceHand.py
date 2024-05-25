"""Random"""


import random


class DiceHand:
    """Class used for a player to be able to roll"""
    def __init__(self, dice1, dice2):
        self.dice1 = dice1
        self.dice2 = dice2

    def roll_pvi(self, player, dice1, dice2):
        """Function used to roll against cpu"""
        score = 0
        score_to_check_dice1 = 0
        score_to_check_dice2 = 0
        difficulty_level = player.get_difficulty_level()
        print("Here 1")
        # If cpu difficulty is easy
        if difficulty_level == 1:
            score_to_check_dice1 = random.randint(1, dice1.get_sides())
            score_to_check_dice2 = random.randint(1, dice2.get_sides())
        elif difficulty_level == 2:
            score_to_check_dice1 = random.randint(3, dice1.get_sides())
            score_to_check_dice2 = random.randint(3, dice2.get_sides())
        elif difficulty_level == 3:
            score_to_check_dice1 = random.randint(4, dice1.get_sides())
            score_to_check_dice2 = random.randint(4, dice2.get_sides())

        if (score_to_check_dice1 == 1 or score_to_check_dice2 == 1):
            score += score_to_check_dice1
            score += score_to_check_dice2
            player.add_score(score)
            return False
        elif (score_to_check_dice1 == 1 and score_to_check_dice2 == 1):
            player.reset_score()
            return False
        else:
            score += score_to_check_dice1
            score += score_to_check_dice2
            player.add_score(score)
            return True

    def roll_pvp(self, player, dice1, dice2):
        """Function performs rolls for both players"""
        score = 0
        score_to_check_dice1 = random.randint(1, dice1.get_sides())
        score_to_check_dice2 = random.randint(1, dice2.get_sides())

        if (score_to_check_dice1 == 1 or score_to_check_dice2 == 1):
            score += score_to_check_dice1
            score += score_to_check_dice2
            player.add_score(score)
            return False

        elif (score_to_check_dice1 == 1 and score_to_check_dice2 == 1):
            player.reset_score()
            # condition = False
            return False
        else:
            score += score_to_check_dice1
            score += score_to_check_dice2
            player.add_score(score)
            return True

    def roll_or_not(self):
        roll_or_not = random.randint(1, 2)
        return roll_or_not
