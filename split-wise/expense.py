from typing import List, Dict, Optional
from user import User
from split_strategy import SplitStrategy  # pylint: disable=unused-import

class Expense:
    def __init__(self, expense_id: str, amount: float, payer: User, participants: List[User], strategy: SplitStrategy, shares: Optional[Dict[str, float]] = None):
        self.expense_id = expense_id
        self.amount = round(amount, 2)
        self.payer = payer
        self.participants = participants
        self.strategy = strategy
        self.shares = shares
        self.splits: Dict[str, float] = {}

    def calculate_splits(self):
        self.splits = self.strategy.split(self.amount, self.participants, self.payer, self.shares)
        for participant in self.participants:
            if participant.user_id in self.splits:
                participant.update_balance(self.payer.user_id, self.splits[participant.user_id])
                self.payer.update_balance(participant.user_id, -self.splits[participant.user_id])

    def __str__(self):
        return f"Expense {self.expense_id}: {self.amount:.2f} paid by {self.payer}, split among {len(self.participants)} users"