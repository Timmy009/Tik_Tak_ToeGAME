from GameException import GameException


class Game:

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = 0

    def play(self, position: str, player):
        self.play_tik(position, player)

    def play_tik(self, position, player):
        print("Choose between 1 to 9 to play")
        if position == "1":
            if self.board[0][0] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[0][0] = player.get_player_identity()
        if position == "2":
            if self.board[0][1] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[0][1] = player.get_player_identity()
        if position == "3":
            if self.board[0][2] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[0][2] = player.get_player_identity()
        if position == "4":
            if self.board[1][0] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[1][0] = player.get_player_identity()
        if position == "5":
            if self.board[1][1] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[1][1] = player.get_player_identity()
        if position == "6":
            if self.board[1][2] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[1][2] = player.get_player_identity()
        if position == "7":
            if self.board[2][0] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[2][0] = player.get_player_identity()
        if position == "8":
            if self.board[2][1] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[2][1] = player.get_player_identity()
        if position == "9":
            if self.board[2][2] != " ":
                raise GameException('This position has been played before. Kindly replay')
            else:
                self.board[2][2] = player.get_player_identity()
        self.print_board()
        print(self.check_winner(player))

    def print_board(self):
        for score in self.board:
            print(score)

    def check_winner(self, player):
        if self.board[0][0] == player.identity and self.board[0][1] == player.identity and self.board[0][
            2] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        if self.board[1][0] == player.identity and self.board[1][1] == player.identity and self.board[1][
            2] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        if self.board[2][0] == player.identity and self.board[2][1] == player.identity and self.board[2][
            2] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        if self.board[0][0] == player.identity and self.board[1][0] == player.identity and self.board[2][
            0] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        if self.board[0][1] == player.identity and self.board[1][1] == player.identity and self.board[2][
            1] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        if self.board[0][2] == player.identity and self.board[1][2] == player.identity and self.board[2][
            2] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        if self.board[0][0] == player.identity and self.board[1][1] == player.identity and self.board[2][
            2] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        if self.board[2][0] == player.identity and self.board[1][1] == player.identity and self.board[0][
            2] == player.identity:
            self.done = 1
            return player.get_player_name(), "won the game. The game has ended"
        self.default_return()

    def default_return(self):
        detect = 0
        for th in self.board:
            for pl in th:
                if pl != " ":
                    detect = detect + 1
                    if detect == 9:
                        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
