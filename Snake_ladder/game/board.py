class Board:
    def __init__(self,size,entities):
        self.size=size# size of board
        self.entities=entities#list of entities
    
    def get_final_position(self,position):
        final_pos=position
        for entity in self.entities:
            final_pos=entity.get_destination(final_pos) # checks with the entites where would be land the player
        return final_pos if final_pos <=self.size else position# meaning if position is less than size then send new postion else send old one
    