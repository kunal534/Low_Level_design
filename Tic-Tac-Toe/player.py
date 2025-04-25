class Player:
    def __init__(self, name:str,symbol:str):
        self.name=name
        self.symbol=symbol

    def __str__(self):
        return f"{self.name} ({self.symbol})"

