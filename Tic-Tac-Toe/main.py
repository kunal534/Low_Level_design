from player import Player
from game import TicTacToe

def main():
    player1=Player("Player 1", "X")
    player2=Player("Player 2", "O")
    game=TicTacToe(player1,player2)
    game.play()

if __name__=="__main__":
    main()
# This is the main entry point of the Tic Tac Toe game.