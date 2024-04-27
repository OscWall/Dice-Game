"""Random"""


import random


class DiceHand():
    """Class used for a player to be able to roll"""
    def __init__(self, dice1, dice2):
        self.dice1 = dice1
        self.dice2 = dice2

    def roll_pvi(self, player, dice1, dice2):
        """Function used to roll against cpu"""
        score = 0
        score_to_check_dice1 = 0
        score_to_check_dice2 = 0

        # If cpu difficulty is easy
        if player.get_difficulty_level == 1:
            # Make sure the Dice class has a method called "get_sides"
            score_to_check_dice1 = random.randint(1, dice1.get_sides())
            # Make sure the Dice class has a method called "get_sides"
            score_to_check_dice2 = random.randint(1, dice2.get_sides())
            if (score_to_check_dice1 == 1 or score_to_check_dice2 == 1):
                score += score_to_check_dice1
                score += score_to_check_dice2
                player.add_score(score)
            elif (score_to_check_dice1 == 1 and score_to_check_dice2 == 1):
                player.reset_score()
            else:
                score += score_to_check_dice1
                score += score_to_check_dice2

        # If cpu difficulty is medium
        elif player.get_difficulty_level() == 2:
            # Make sure the Dice class has a method called "get_sides"
            score_to_check_dice1 = random.randint(3, dice1.get_sides())
            # Make sure the Dice class has a method called "get_sides"
            score_to_check_dice2 = random.randint(3, dice2.get_sides())
            if (score_to_check_dice1 == 1 or score_to_check_dice2 == 1):
                score += score_to_check_dice1
                score += score_to_check_dice2
            elif (score_to_check_dice1 == 1 and score_to_check_dice2 == 1):
                player.reset_score()
            else:
                score += score_to_check_dice1
                score += score_to_check_dice2

        # If cpu difficulty is hard
        else:
            # Make sure the Dice class has a method called "get_sides"
            score_to_check_dice1 = random.randint(4, dice1.get_sides())
            # Make sure the Dice class has a method called "get_sides"
            score_to_check_dice2 = random.randint(4, dice2.get_sides())
            if (score_to_check_dice1 == 1 or score_to_check_dice2 == 1):
                score += score_to_check_dice1
                score += score_to_check_dice2
            elif (score_to_check_dice1 == 1 and score_to_check_dice2 == 1):
                score = player.reset_score()
            else:
                score += score_to_check_dice1
                score += score_to_check_dice2
        return score

    def roll_pvp(self, player, dice1, dice2):
        """Function performs rolls for both players"""
        score = 0
        score_to_check_dice1 = random.randint(1, dice1.get_sides())
        score_to_check_dice2 = random.randint(1, dice2.get_sides())

        if (score_to_check_dice1 == 1 or score_to_check_dice2 == 1):
            score += score_to_check_dice1
            score += score_to_check_dice2
            player.add_score(score)

        elif (score_to_check_dice1 == 1 and score_to_check_dice2 == 1):
            player.reset_score()
            # condition = False

        else:
            score += score_to_check_dice1
            score += score_to_check_dice2
            player.addScore(score)

        return score
