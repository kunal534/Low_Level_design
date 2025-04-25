from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from user import User  # Only import User, not SplitStrategy

class SplitStrategy(ABC):
    @abstractmethod
    def split(self, amount: float, participants: List[User], payer: User, shares: Optional[Dict[str, float]] = None) -> Dict[str, float]:
        pass

class EqualSplitStrategy(SplitStrategy):
    def split(self, amount: float, participants: List[User], payer: User, shares: Optional[Dict[str, float]] = None) -> Dict[str, float]:
        if not participants:
            return {}
        base_share = amount / len(participants)
        splits = {}
        remainder = round(amount - base_share * (len(participants) - 1), 2)
        first_assigned = False
        for participant in participants:
            if participant.user_id != payer.user_id:
                if not first_assigned:
                    splits[participant.user_id] = round(remainder, 2)
                    first_assigned = True
                else:
                    splits[participant.user_id] = round(base_share, 2)
        return splits

class ExactSplitStrategy(SplitStrategy):
    def split(self, amount: float, participants: List[User], payer: User, shares: Dict[str, float]) -> Dict[str, float]:
        if not shares or sum(shares.values()) != amount:
            raise ValueError("Exact shares must sum to total amount")
        splits = {uid: round(amt, 2) for uid, amt in shares.items() if uid != payer.user_id}
        return splits

class PercentSplitStrategy(SplitStrategy):
    def split(self, amount: float, participants: List[User], payer: User, shares: Dict[str, float]) -> Dict[str, float]:
        if not shares or round(sum(shares.values()), 2) != 100:
            raise ValueError("Percentages must sum to 100")
        splits = {}
        for participant in participants:
            if participant.user_id != payer.user_id and participant.user_id in shares:
                splits[participant.user_id] = round(amount * shares[participant.user_id] / 100, 2)
        return splits