from user import User
from splitwise import Splitwise

def main():
    splitwise = Splitwise()

    # Add users
    splitwise.add_user("u1", "Alice", "alice@example.com", "1234567890")
    splitwise.add_user("u2", "Bob", "bob@example.com", "0987654321")
    splitwise.add_user("u3", "Charlie", "charlie@example.com", "1122334455")

    # Add expenses
    splitwise.add_expense("e1", 100.0, "u1", ["u1", "u2", "u3"], "EQUAL")
    splitwise.add_expense("e2", 200.0, "u2", ["u1", "u2", "u3"], "EXACT", {"u1": 80.0, "u2": 60.0, "u3": 60.0})
    splitwise.add_expense("e3", 150.0, "u3", ["u1", "u2", "u3"], "PERCENT", {"u1": 40, "u2": 40, "u3": 20})

    # Show expenses and balances
    splitwise.show_user_expenses("u1")
    splitwise.display_balances()

if __name__ == "__main__":
    main()