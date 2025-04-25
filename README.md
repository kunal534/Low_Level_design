# 🧠 Low Level Design in Python

This repository contains Python implementations of popular Low-Level Design (LLD) problems. Each module is designed with Object-Oriented Programming (OOP) principles and simulates real-world system behavior, making it a perfect resource for system design interview preparation.

---

## 📁 Repository Structure

```
Low_Level_design/
│
├── TicTacToe/
│   ├── Board.py
│   ├── Game.py
│   ├── Player.py
│   └── main.py
│
├── snake_ladder/
│   ├── Board.py
│   ├── Dice.py
│   ├── Jumper.py
│   ├── Player.py
│   └── main.py
│
├── splitwise/
│   ├── Expense.py
│   ├── Split_strategy.py
│   ├── Splitwise.py
│   ├── User.py
│   └── main.py
```

---

## 🎮 Projects

### 1. 🎲 Snake and Ladder

A simulation of the classic board game with configurable board, snakes, ladders, and multiple players.

**Features:**
- Random dice roll using `Dice` class
- Snakes and ladders implemented via `Jumper` class
- Board management through `Board` class
- Player state management
- Victory condition detection

**Run:**
```bash
cd snake_ladder
python main.py
```

---

### 2. ❌⭕ Tic Tac Toe

A two-player command-line version of Tic Tac Toe using OOP.

**Features:**
- Player vs Player game
- Win and draw conditions
- 3x3 Board class
- Game orchestrated through `Game` class

**Run:**
```bash
cd TicTacToe
python main.py
```

---

### 3. 💸 Splitwise

A mini-expense sharing app modeled after Splitwise.

**Features:**
- Add users
- Add expenses with equal or exact splits
- Track debts between users
- Show balances
- Modular classes like `Expense`, `Split`, `BalanceSheet`, etc.

**Run:**
```bash
cd splitwise
python main.py
```

**Example Output:**
```
Enter: SHOW
No balances

Enter: EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
Enter: SHOW u2
u2 owes u1: 250.0
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Design:** Object-Oriented Programming (OOP)  
- **No external dependencies**

---

## 🚀 Getting Started

Clone the repository:
```bash
git clone https://github.com/kunal534/Low_Level_design.git
cd Low_Level_design
```

Choose a project and run its `main.py`.

---

## 📌 Future Plans

- Add more systems like:
  - Parking Lot
  - Logging System
  - Rate Limiter
  - Elevator Design
- Add Unit Tests using `pytest`
- Add GUI support for games

---

## 🤝 Contributing

Pull requests and suggestions are welcome! If you find an issue or have an idea for improvement, feel free to open an issue or submit a PR.

---

## 👨‍💻 Author

**Kunal Uttam**  
🔗 [GitHub](https://github.com/kunal534)  
🔗 [LinkedIn](https://www.linkedin.com/in/kunaluttam/)

---

## 📄 License

This project is licensed under the MIT License.
