from typing import Dict, List, Optional
from user import User
from split_strategy import SplitStrategy, EqualSplitStrategy, ExactSplitStrategy, PercentSplitStrategy
from expense import Expense

class Splitwise:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.expenses: Dict[str, Expense] = {}

    def add_user(self, user_id: str, name: str, email: str, mobile_number: str):
        if user_id in self.users:
            print(f"User {user_id} already exists.")
            return False
        self.users[user_id] = User(user_id, name, email, mobile_number)
        print(f"User {user_id} added successfully.")
        return True

    def add_expense(self, expense_id: str, amount: float, payer_id: str, participant_ids: List[str], split_type: str, shares: Optional[Dict[str, float]] = None):
        payer = self.users.get(payer_id)
        participants = [self.users.get(pid) for pid in participant_ids if pid in self.users]
        if not payer or not participants:
            print("Invalid payer or participants.")
            return False

        strategy_map = {
            "EQUAL": EqualSplitStrategy(),
            "EXACT": ExactSplitStrategy(),
            "PERCENT": PercentSplitStrategy()
        }
        strategy = strategy_map.get(split_type.upper())
        if not strategy:
            print("Invalid split type.")
            return False

        try:
            expense = Expense(expense_id, amount, payer, participants, strategy, shares)
            expense.calculate_splits()
            self.expenses[expense_id] = expense
            print(f"Expense {expense_id} added successfully.")
            return True
        except ValueError as e:
            print(f"Error in adding expense: {e}")
            return False

    def show_user_expenses(self, user_id: str):
        user = self.users.get(user_id)
        if not user:
            print(f"User {user_id} not found")
            return
        print(f"Expenses for {user.name} ({user.user_id}):")
        for expense in self.expenses.values():
            if user == expense.payer or user in expense.participants:
                print(expense)

    def display_balances(self):
        print("Current Balances:")
        seen_pairs = set()  # To avoid duplicates
        for user in self.users.values():
            non_zero_balances = {uid: amt for uid, amt in user.balances.items() if amt != 0}
            for other_user_id, amount in non_zero_balances.items():
                pair = tuple(sorted([user.user_id, other_user_id]))
                if pair not in seen_pairs:
                    if amount > 0:
                        print(f"{user.name} owes {self.users[other_user_id].name}: {amount:.2f}")
                    elif amount < 0:
                        print(f"{self.users[other_user_id].name} owes {user.name}: {-amount:.2f}")
                    seen_pairs.add(pair)
                    