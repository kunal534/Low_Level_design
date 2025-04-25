import random
from .dice import Dice

class Rolling_effect(Dice):
    def roll(self):
        return random.randint(1,6)