class Output:
    @staticmethod
    def print_move(player,dics_value,old_pos,new_pos):
        print(f"{player.name} rolled a {dics_value} and moved from {old_pos} to {new_pos}")
    
    @staticmethod
    def print_winner(player):
        print(f"{player.name} wins the game")