from colorama import Fore, Back, Style

from Game import Game
from HumanPlayer import HumanPlayer

from ComputerPlayer import ComputerPlayer
from PlayerException import PlayerException


class TikTakToe:

    def __init__(self):
        self.gam = Game()
        self.player_one = "0"
        self.player_two = "0"

    def main_menu(self):
        option = input( "TIKTAKTOE \nHi, Welcome.\n 1. Multiplayer   : \n 2. Single "
                                                      "player:  " )
        if option == "1":
            self.multi_player()
        elif option == "2":
            self.single_player()
        else:
            print("Enter either 1 or 2")
            self.main_menu()

    def single_player(self):
        inp1 = self.player_input()

        print("PLAY")

        while True:
            self.human_player_one_play(inp1.get_player_name(), inp1.get_player_identity(), self.gam, inp1)
            if self.gam.done == 1:
                break
            self.computer_player_two_play("COMPUTER", "C", self.gam)
            if self.gam.done == 1:
                break

    def player_input(self):
        print("Enter your name and your identity for player ONE")
        name1 = input("Your name: ")
        identity = input("Your identity. Like *(X, or O): ")

        try:
            self.player_one = HumanPlayer(name1, identity)

        except PlayerException:
            print(Fore.RED + "INVALID INPUT" + Style.RESET_ALL)
            self.player_input()
        return self.player_one

    def player_input_two(self):
        print("Enter your name and your identity for player TWO")
        name1 = input("Your name: ")
        identity = input("Your identity. Like *(X, or O): ")

        try:
            self.player_two = HumanPlayer(name1, identity)

        except PlayerException:
            print("INVALID INPUT")
            self.player_input_two()

        return self.player_two

    def human_player_one_play(self, name, identity, gam, player_one):
        print(player_one.get_player_name(), "  PLAYING")
        try:
            gam.play(player_one.move(), player_one)
        except:
            print(Fore.RED +"Invalid Move. Please replay" + Style.RESET_ALL)
            self.human_player_one_play(name, identity, gam, player_one)

    def computer_player_two_play(self, name2, identity2, gam):
        print("COMPUTER PLAYING")
        player_two = ComputerPlayer(name2, identity2)

        try:
            gam.play(player_two.move(), player_two)
        except:
            print(Fore.RED + "Invalid Move. Please replay" + Style.RESET_ALL)
            self.computer_player_two_play(name2, identity2, gam)

    def multi_player(self):
        inp1 = self.player_input()
        inp2 = self.player_input_two()
        while True:
            self.human_player_one_play(inp1.get_player_name(), inp1.get_player_identity(), self.gam, inp1)
            if self.gam.done == 1:
                break
            self.human_player_one_play(inp2.get_player_name(), inp2.get_player_identity(), self.gam, inp2)
            if self.gam.done == 1:
                break
