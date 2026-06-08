# 🎓 Student Toolkit

A command-line Python utility designed for CS/BCA students — combining a **GPA Calculator** and a **Quiz App** in one clean, interactive package.

---

## 📦 Features

### 1. GPA Calculator
- **SGPA Calculator** — Enter subject names, credit hours, and grades to compute your Semester GPA
- **CGPA Calculator** — Input SGPA and credits for multiple semesters to get your Cumulative GPA
- Supports standard 10-point grading scale (O, A+, A, B+, B, C, P, F)
- Displays detailed result summary with remarks

### 2. Quiz App
- **3 Topics**: Python, Data Structures & Algorithms, General CS
- **Random Mixed Mode** — Pulls questions from all topics
- **Timed Mode** — 20 seconds per question for extra challenge
- **Answer Review** — See explanations for every question after the quiz
- Score, percentage, and performance remark at the end

---

## 🚀 Getting Started

### Requirements
- Python 3.7 or higher
- No external libraries required (uses standard library only)

### Run the project

```bash
# Clone the repository
git clone https://github.com/your-username/student-toolkit.git
cd student-toolkit

# Run the toolkit
python main.py
```

---

## 🗂️ Project Structure

```
student_toolkit/
│
├── main.py                    # Entry point — Main Menu
│
├── gpa_calculator/
│   ├── __init__.py
│   └── gpa.py                 # SGPA & CGPA logic
│
└── quiz_app/
    ├── __init__.py
    └── quiz.py                # MCQ quiz engine + question bank
```

---

## 📸 Sample Output

```
╔════════════════════════════════════════════╗
║        🎓  STUDENT TOOLKIT  🎓             ║
║   Your all-in-one academic utility belt    ║
╚════════════════════════════════════════════╝

  Main Menu
  ──────────────────────────────
  1.  GPA Calculator
  2.  Quiz App
  0.  Exit
```

```
  Q1. Which data structure follows LIFO order?
      A) Queue
      B) Stack
      C) Linked List
      D) Tree

  Your answer: B
  ✅ Correct!
```

---

## 🧮 Grading Scale Used

| Grade | Points |
|-------|--------|
| O     | 10     |
| A+    | 9      |
| A     | 8      |
| B+    | 7      |
| B     | 6      |
| C     | 5      |
| P     | 4      |
| F     | 0      |

---

## 🛠️ How to Add More Quiz Questions

Open `quiz_app/quiz.py` and add entries to the `QUESTIONS` dictionary:

```python
{
    "q": "Your question here?",
    "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
    "answer": "A",
    "explanation": "Brief explanation of the correct answer."
}
```

---

## 👨‍💻 Author

**Pratik**  
BCA Student — C.M.P. Degree College, Allahabad  
University of Allahabad

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
