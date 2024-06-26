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
        self.user_input = None
        self.user_input_int = None
        self.dice_hand = None
        self.difficulty_level = None
        self.difficulty_level_int = None
        self.counter_player_1 = 0
        self.counter_player_2 = 0
        self.counter_cpu = 0

    def displayUI(self, player_1_name, player_2_name, player_1_score, player_2_or_cpu_score):
        print(f"""+---------+---------+
|   {player_1_name:6}|    {player_2_name:5}|
+---------+---------+
|         |         |
|{player_1_score:5}    |{player_2_or_cpu_score:5}    |
|         |         |
+---------+---------+
""")

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
        self.user_input = input("""Welcome to the dice game
Select:
1. Player vs Player
2. Player vs CPU
""")
        try:
            self.user_input_int = int(self.user_input)
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
        # Resets the values of players and cpu
        self.player_1 = None
        self.player_2 = None
        self.cpu = None

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
                print("Here")
                if self.input_difficulty_level() is not False:
                    print("Here")
                    self.player_1 = Player(name_of_player_1, 0, 1)
                    self.cpu = Intelligence(name_of_cpu, 0, self.difficulty_level_int)
                    self.dice_1 = Dice(6)
                    self.dice_2 = Dice(6)
                    self.dice_hand = DiceHand(self.dice_1, self.dice_2)
                    self.print_rules()

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

    def roll_cpu(self):
        condition = True
        while condition:
            if self.dice_hand.roll_pvi(self.cpu, self.dice_1, self.dice_2):
                print(f"{self.cpu.get_name()}'s score: {self.cpu.get_score()}")
                user_input = self.dice_hand.roll_or_not()
                try:
                    user_input_int = int(user_input)
                except ValueError:
                    print("Invalid input")
                if user_input_int == 2:
                    self.counter_cpu += 1
                    break
            else:
                print(f"{self.cpu.get_name()}'s score: {self.cpu.get_score()}")
                self.counter_cpu += 1
                break

    def roll_player_1(self):
        condition = True
        while condition:
            if self.dice_hand.roll_pvp(self.player_1, self.dice_1, self.dice_2):
                print(f"{self.player_1.get_name()}'s score: {self.player_1.get_score()}")
                user_input = input("Do you want to 1. Roll again 2. Hold: ")
                try:
                    user_input_int = int(user_input)
                except ValueError:
                    print("Invalid input")
                if user_input_int == 2:
                    self.counter_player_1 += 1
                    break
                elif self.counter_player_1 == 1:
                    continue
                else:
                    print("Please input a valid value")
            else:
                print(f"{self.player_1.get_name()}'s score: {self.player_1.get_score()}")
                self.counter_player_1 += 1
                break

    def roll_player_2(self):
        condition = True
        while condition:
            if self.dice_hand.roll_pvp(self.player_2, self.dice_1, self.dice_2):
                print(f"{self.player_2.get_name()}'s score: {self.player_2.get_score()}")
                user_input = input("Do you want to 1.roll again 2. Hold: ")
                try:
                    user_input_int = int(user_input)
                except ValueError:
                    print("Invalid input")
                if user_input_int == 2:
                    self.counter_player_2 += 1
                    break
                elif self.counter_player_1 == 1:
                    continue
            else:
                print(f"{self.player_2.get_name()}'s score: {self.player_2.get_score()}")
                self.counter_player_2 += 1
                break

    def do_roll(self, args):
        """Function is used to roll the dices"""
        # If it's player v player
        if self.player_1 is None:
            print("Please start the game first")
            return

        if self.player_2 is not None:
            if self.player_1.get_score() < 100 or self.player_2.get_score() < 100:
                if self.counter_player_1 == self.counter_player_2:
                    print(f"It's {self.player_1.get_name()}s turn")
                    self.roll_player_1()
                else:
                    print(f"It's {self.player_2.get_name()}s turn")
                    print(f"{self.player_2.get_name()} has rolled")
                    self.roll_player_2()

            else:
                print("The game is over")

        else:
            if self.player_1.get_score() < 100 or self.cpu.get_score() < 100:
                if self.counter_player_1 == self.counter_cpu:
                    print(f"It's {self.player_1.get_name()}'s turn")
                    self.roll_player_1()

                else:
                    print(f"It's {self.cpu.get_name()}'s turn")
                    print(f"{self.cpu.get_name()} has rolled")
                    self.roll_cpu()
            else:
                print("The game is over")

    def do_display_score(self, args):
        """Function used to display the score"""
        if self.player_2 is not None:
            self.displayUI(self.player_1.get_name(), self.player_2.get_name(), self.player_1.get_score(), self.player_2.get_score())
        else:
            self.displayUI(self.player_1.get_name(), self.cpu.get_name(), self.player_1.get_score(), self.cpu.get_score())

    def do_print_users(self, args):
        """Function used to print the name of the users"""
        if self.player_2 is not None:
            print(f"""Name of Player 1: {self.player_1.get_name()}
Name of Player 2: {self.player_2.get_name()}""")
        else:
            print(f"""Name of Player 1: {self.player_1.get_name()}
Name of CPU: {self.cpu.get_name()}""")

    def do_change_difficulty_level(self, args):
        if self.player_2 is not None:
            print("You can't change the difficulty level")
        else:
            if self.input_difficulty_level() is not False:
                self.cpu.set_difficulty_level(self.difficulty_level_int)


if __name__ == '__main__':
    Main().cmdloop()
