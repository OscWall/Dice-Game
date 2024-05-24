from player import Player
from intelligence import Intelligence
import cmd
from dice import Dice
from diceHand import DiceHand


class Main(cmd.Cmd):
    """Class runs the program"""
    def __init__(self):
        super().__init__()
        self.dice_1 = None
        self.dice_2 = None
        self.player_1 = None
        self.player_2 = None
        self.cpu = None
        self.user_input_int = None
        self.dice_hand = None
        self.difficulty_level = None
        self.difficulty_level_int = None
        self.counter_player_1 = 0
        self.counter_player_2 = 0
        self.counter_cpu = 0

    def print_rules(self):
        print("""The rules of the game are as follows:

    - Each player will roll 2 dices, if the number they get om both dices is
      not 1 then the number gets added to the score of the player and the
      player is allowed to roll the dice again

    - If a player gets a 1 on one of the dices,
      it becomes the next players turn

    - If a player gets a 1 on both dices then the score is reset to 0

    - A player may decide to “hold” after one or more rolls,
      if this happens then the player gets to keep their points
      and it becomes the next players turn to roll

    - The first player to score 100 or more points wins\n""")

    def input_choice(self):
        user_input = input("""Welcome to the dice game
Select:
1. Player vs Player
2. Player vs CPU
""")
        try:
            self.user_input_int = int(user_input)
            if self.user_input_int < 1 or self.user_input_int > 2:
                print("Please enter a valid number")
                return False
        except ValueError:
            print("Input a valid value")
            return False

    def input_difficulty_level(self):
        self.difficulty_level = input("""Enter difficulty level
(1. Easy 2. Medium 3. Hard):""")
        try:
            self.difficulty_level_int = int(self.difficulty_level)
            if self.difficulty_level_int < 1 or self.difficulty_level_int > 3:
                print("""Please input a valid number
for the difficulty level""")
                return False
        except ValueError:
            print("Input a valid value")
            return False

    def do_start(self, args):
        """Starts the game"""
        # Checks if the user choice is an integer
        if self.input_choice() is not False:
            if self.user_input_int == 1:
                name_of_player_1 = input("Enter name of player 1: ")
                name_of_player_2 = input("Enter name of player 2: ")
                self.player_1 = Player(name_of_player_1, 0, 1)
                self.player_2 = Player(name_of_player_2, 0, 1)
                self.dice_1 = Dice(6)
                self.dice_2 = Dice(6)
                self.dice_hand = DiceHand(self.dice_1, self.dice_2)
                self.print_rules()

            else:
                name_of_player_1 = input("Enter name of player 1: ")
                name_of_cpu = input("Input name of CPU: ")

                if self.input_difficulty_level():
                    self.player_1 = Player(name_of_player_1, 0, 1)
                    self.cpu = Intelligence(name_of_cpu, 0, self.difficultyLevel_int)
                    self.dice_1 = Dice(6)
                    self.dice_2 = Dice(6)
                    self.dice_hand = DiceHand(self.dice_1, self.dice_2)
                    self.print_rules()
                    return True
                else:
                    return False

    def do_exit(self, args):
        """This command exits the program"""
        print("Thanks for playing!!")
        return True
    do_quit = do_exit

    def do_printrules(self, args):
        """Prints the rules of the game"""
        print("""The rules of the game are as follows:

    - Each player will roll 2 dices, if the number they get om both dices is
      not 1 then the number gets added to the score of the player and the
      player is allowed to roll the dice again

    - If a player gets a 1 on one of the dices,
      it becomes the next players turn

    - If a player gets a 1 on both dices then the score is reset to 0

    - A player may decide to “hold” after one or more rolls,
      if this happens then the player gets to keep their points
      and it becomes the next players turn to roll

    - The first player to score 100 or more points wins

    - Type "roll" to roll the dice

    - type help for all the commands\n""")

    def do_roll(self, args):
        # If it's player v player
        condition = True
        if self.player_1 is None:
            print("Please start the game first")
            return False
        else:
            if self.player_2 is not None:
                if self.player_1.get_score() < 100 and self.player_2.get_score() < 100:
                    if self.counter_player_1 == self.counter_player_2:
                        print(f"It's {self.player_1.get_name()}s turn")
                        while condition:
                            if self.dice_hand.roll_pvp(self.player_1, self.dice_1, self.dice_2):
                                print(f"{self.player_1.get_name()}'s score: {self.player_1.get_score()}")
                                user_input = input("Do you want to 1. Roll again 2. Hold")
                                try:
                                    user_input_int = int(user_input)
                                except ValueError:
                                    print("Invalid input")
                                if user_input_int == 2:
                                    self.counter_player_1 += 1
                                    break
                    else:
                        print(f"It's {self.player_2.get_name()}s turn")
                        print(f"{self.player_1.get_name()} has rolled")
                        while condition:
                            if self.dice_hand.roll_pvp(self.player_2, self.dice_1, self.dice_2):
                                print(f"{self.player_1.get_name()}'s score: {self.player_1.get_score()}")
                                user_input = input("Do you want to 1.roll again 2. hold")
                                try:
                                    user_input_int = int(user_input)
                                except ValueError:
                                    print("Invalid input")
                                if user_input_int == 2:
                                    self.counter_player_2 += 1
                                    break
                    #if counter_player_1 == counter_player_2:
                    #    counter_player_1 += 1
                    #else:
            
                    #    counter_player_2 += 1
            else:
                if self.player_1.get_score() < 100 and self.cpu.get_score < 100:
                    if counter_player_1 == counter_player_2:
                        print(f"It's {self.player_1.get_name()}s turn")
                        print(f"It's {self.player_1.get_name()}s turn")

                        while condition:
                            if self.dice_hand.roll_pvi(self.player_1, self.dice_1, self.dice_2):
                                user_input = input("Do you want to 1.roll again 2. hold")
                                try:
                                    user_input_int = int(user_input)
                                except ValueError:
                                    print("Invalid input")
                                if user_input_int == 2:
                                    break
                else:
                    if counter_player_1 == counter_cpu:
                        counter_player_1 += 1
                    else:
                        counter_cpu += 1

    def do_displayScore(self, args):
        """Function used to display the score"""
        pass

    def do_print_users(self, args):
        """Function used to print the name of the users"""
        if self.player_2 is not None:
            print(f"""Name of Player 1: {self.player_1.get_name()}
Name of Player 2: {self.player_2.get_name()}""")


if __name__ == '__main__':
    Main().cmdloop()
