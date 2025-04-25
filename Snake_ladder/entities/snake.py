from .board_entity import board

class Snake(board):
    def __init__(self,head,tail):
        self.head=head
        self.tail=tail
    def get_destination(self, position):
        return self.tail if position == self.head else position