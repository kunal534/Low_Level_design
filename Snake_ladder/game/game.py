class Game:
    def __init__(self,board,players,dice,output):
        self.board=board
        self.player=players
        self.dice=dice# injecting dice dependency
        self.output=output# injectecting output handler
        self.current_player_idx=0
    
    def play_turn(self):
        player=self.player[self.current_player_idx]
        dice_value=self.dice.roll()
        old_pos=player.position
        new_pos=player.move(dice_value,self.board)
        self.output.print_move(player,dice_value,old_pos,new_pos)
        return new_pos == self.board.size
    
    def start(self):
        while True:
            if self.play_turn():
                self.output.print_winner(self.player[self.current_player_idx])
                break
            self.current_player_idx=(self.current_player_idx+1)%len(self.player)
