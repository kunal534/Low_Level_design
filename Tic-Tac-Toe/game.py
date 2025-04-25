from typing import Optional
from board import Board
from player import Player

class TicTacToe:
    def __init__(self,Player1:Player, Player2:Player):
        self.board = Board()
        self.current_player = [Player1, Player2]
        self.current_player_index = 0
    
    def currrent_player(self)->Player:
        return self.current_player[self.current_player_index]

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play_turn(self)->Optional[Player]:
        player=self.currrent_player()
        print(f"{player}'s turn")
        while True:
            try:
                row=int(input("Enter row (0-2): "))
                col=int(input("Enter column (0-2): "))
                if self.board.is_valid_move(row,col):
                    self.board.place_symbol(row,col,player.symbol)
                    break
                else:  
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
        self.board.display()
        if self.board.check_winner(player.symbol):
            return player
        elif self.board.is_full():
            return None
        self.switch_player()   
        return None

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.display()
        winner=None
        while winner is None and not self.board.is_full():
            winner=self.play_turn()

        if winner:
            print(f"{winner} wins!")
        else:
            print("It's a draw!")