from typing import Dict

class User:
    def __init__(self, user_id: str, name: str, email: str, mobile_number: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.balances: Dict[str, float] = {}  # user_id -> amount (positive = owes them, negative = they owe me)

    def update_balance(self, other_user_id: str, amount: float):
        """
        Update the balance with another user.
        - Positive amount: This user owes the other user.
        - Negative amount: The other user owes this user.
        """
        if other_user_id == self.user_id or amount == 0:
            return  # No balance with self or zero amount
        current_balance = self.balances.get(other_user_id, 0)
        new_balance = round(current_balance + amount, 2)
        self.balances[other_user_id] = new_balance

    def get_balance(self, other_user_id: str) -> float:
        return self.balances.get(other_user_id, 0)

    def __str__(self):
        return f"{self.name} ({self.user_id})"