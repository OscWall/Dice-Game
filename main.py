from player import Player
from intelligence import Intelligence
import cmd
from dice import Dice
from diceHand import DiceHand

class Main(cmd.Cmd):
    """Class runs the program"""
    player_1 = None
    player_2 = None
    cpu = None
    user_input_int = None

    def do_start(self, args):
        """Starts the game"""
        user_input = input("""Welcome to the dice game
Select:
1. Player vs Player
2. Player vs CPU
""")
        try:
            self.user_input_int = int(user_input)
        except ValueError:
            print("Input a valid value")


        while(self.user_input_int<1 and self.user_input_int>2):
            print("Please enter a valid number")

        if self.user_input_int == 1:
            nameOfPlayer1 = input("Enter name of player 1: ")
            nameOfPlayer2 = input("Enter name of player 2: ")
            self.player_1 = Player(nameOfPlayer1, 0, 1)
            self.player_2 = Player(nameOfPlayer2, 0, 1)

        else:
            nameOfPlayer1 = input("Enter name of player 1: ")
            nameofCPU = input("Input name of CPU: ")
            difficultyLevel = int(input("""Enter difficulty level 
                                        (1. Easy 2. Medium 3. Hard):"""))

            while difficultyLevel < 1 or difficultyLevel > 3:
                print("Input a valid number")
                difficultyLevel = int(input("""Enter difficulty level
                                            (1. Easy 2. Medium 3. Hard): """))

            self.player_1 = Player(nameOfPlayer1, 0, 1)
            self.cpu = Intelligence(nameofCPU, 0, difficultyLevel)
        # playername = self.player1.getName()
        dice1 = Dice(6)
        dice2 = Dice(6)
        dice_hand = DiceHand(dice1, dice2)
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
        pass
    
    def do_displayScore(self, args):
        pass
    

if __name__ == '__main__':
    Main().cmdloop()
