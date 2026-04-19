# 🧠 Smart Quiz App

> A command-line quiz application with adaptive difficulty levels, real-time scoring, and a persistent leaderboard — built for the curious mind.

---

## 📌 Overview

**Smart Quiz App** is an interactive terminal-based quiz game developed in Python. It challenges users across three difficulty levels — Easy, Medium, and Hard — featuring instant feedback, score tracking with a penalty system, and a ranked leaderboard. Designed for educational fun, it's lightweight, dependency-free, and runs anywhere Python runs.
## ✨ Features
| Feature | Description |
|---|---|
| 🎯 **3 Difficulty Levels** | Easy, Medium, and Hard question sets |
| ⚡ **Instant Feedback** | Right/Wrong revealed immediately after each answer |
| ➕➖ **Penalty System** | +1 for correct, -1 for wrong (floor at 0) |
| 🏆 **Leaderboard** | Ranked by score across all attempts in the session |
| 📋 **Last Score Viewer** | Instantly recall your most recent attempt |
| 🧩 **Input Validation** | Handles invalid entries gracefully at every prompt |
| 📊 **Performance Rating** | Ranked as Failure / Beginner / Intermediate / Advanced |

## 🗂️ Project Structure

```
smart-quiz-app/
│
├── quiz.py          # Main application file
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- No external libraries required — uses only Python built-ins

### Run the App

```bash
# Clone the repository
git clone https://github.com/Shahzaib695/smart-quiz-app.git

# Navigate into the project
cd smart-quiz-app

# Run the app
python quiz.py
```

---

## 🕹️ How to Play

1. **Launch** the app and enter your name
2. **Choose a difficulty:**
   - `1` → Easy (general knowledge)
   - `2` → Medium (math, computers, geography)
   - `3` → Hard (DSA, binary, algorithms)
3. **Answer** each question by typing `A`, `B`, `C`, or `D`
4. **Get instant feedback** — correct answers earn a point, wrong ones deduct one (minimum 0)
5. **View your result** and see where you rank on the leaderboard

---

## 📊 Scoring System

| Percentage | Rank |
|---|---|
| 0% – 24% | 💀 Failure |
| 25% – 49% | 🟡 Beginner |
| 50% – 74% | 🟠 Intermediate |
| 75% – 100% | 🟢 Advanced |

**Score formula:**  
`Percentage = (Score / Total Questions) × 100`

---

## 📸 App Flow

```
Welcome Screen
    │
    ├── 1. Start Quiz
    │       ├── Enter Name
    │       ├── Choose Difficulty (Easy / Medium / Hard)
    │       ├── Answer 10 Questions
    │       └── View Result + Save to Leaderboard
    │
    ├── 2. Leaderboard     → View all attempts ranked by score
    ├── 3. Last Score      → View your most recent result
    └── 4. Exit
```

---

## 🧪 Question Categories

### 🟢 Easy
Basic arithmetic, general knowledge, everyday objects

### 🟡 Medium
Web technologies (HTML/CSS), computer hardware, capitals, multiplication

### 🔴 Hard
Data Structures & Algorithms, binary, time complexity, OOP principles, networking

---

## 💡 Sample Output

```
=============WELCOME TO SMART QUIZ APP=================

Smart Quiz Application

1: Start the Quiz
2: LeaderBoard
3: View Last Score
4: Exit

Enter Your Suitable Option: 1
Enter Your Name: Shahzaib

...

What is the time complexity of binary search?
A) O(n)
B) O(log n)
C) O(n^2)
D) O(1)

Enter Your Answer (A/B/C/D): B
Correct!
Score = 1

...

===== RESULT =====
Name: Shahzaib
Score: 8
Percentage: 80.0
Level: Advanced
```

---

## 🛠️ Built With

- **Language:** Python 3
- **Paradigm:** Procedural / Structured Programming
- **I/O:** Command-Line Interface (CLI)
- **Libraries:** None (pure Python)

---

## 🙌 Author

**Shahzaib**    
Built as part of a Hackathon Project 🏆

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> *"The more you quiz, the more you know."* 🚀
