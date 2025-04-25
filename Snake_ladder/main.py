from entities import Snake, Ladder
from game import Board, Player, Game, Output
from dice import Rolling_effect

snakes=[Snake(16,6),Snake(47,26)]
ladders=[Ladder(1,36), Ladder(4,14)]
entities=snakes+ladders
board=Board(100,entities)
players=[Player("A"),Player("B")]
dice=Rolling_effect()
output=Output()

game=Game(board,players,dice,output)
game.start()
