from typing import List, Optional

class Board:
    def __init__(self):
        self.grid: List[List[Optional[str]]] = [[None for _ in range(3)] for _ in range(3)]

    def is_valid_move(self,row:int,col:int)->bool:
        return 0<=row<3 and 0<=col<3 and self.grid[row][col] is None

    def place_symbol(self,row:int,col:int,symbol:str)->bool:
        if self.is_valid_move(row,col):
            self.grid[row][col]=symbol
            
    def is_full(self)->bool:
        return all(self.grid[row][col] is not None for row in range(3) for col in range(3))

    def check_winner(self,symbol:str)->bool:
        #check row
        for row in range(3):
            if all(self.grid[row][col]== symbol for col in range(3)):
                return True
        #check column
        for col in range(3):
            if all(self.grid[row][col]== symbol for row in range(3)):
                return True
        #check diagonals
        #top left to bottom right
        if all(self.grid[i][i]==symbol for i in range(3)):
            return True
        #bottom left to top right
        if all(self.grid[i][2-i]==symbol for i in range(3)):
            return True

    def display(self):
        for row in self.grid:
            print(" | ".join(cell if cell else " " for cell in row))
            print("-" * 9)