from .board_entity import board

class Ladder(board):
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def get_destination(self,position):
        return self.end if position == self.end else position