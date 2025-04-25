class Player:
    def __init__(self,name):
        self.name=name
        self.position=0
    def move(self,steps, board):
        new_pos=self.position+steps
        self.position=board.get_final_position(new_pos)
        return self.position
