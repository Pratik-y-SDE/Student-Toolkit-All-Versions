# Student Toolkit

A command-line Python utility for BCA / CS students.  
Includes a **GPA Calculator** and a **Quiz App** -- both fully tested on Windows CMD, PowerShell, and VS Code terminal.

---

## Features

### GPA Calculator
- **SGPA** -- enter subjects, credit hours, and grades to compute Semester GPA
- **CGPA** -- enter multiple semester SGPAs to compute Cumulative GPA
- 10-point grading scale: O, A+, A, B+, B, C, P, F, AB
- Input validation: rejects zero, negative, non-numeric, and out-of-range values
- SGPA values above 10 are rejected in CGPA mode

### Quiz App
- **3 topics**: Python, Data Structures, General CS (6 questions each)
- **Random Mixed** mode: picks 10 questions across all topics
- **Timed mode**: advisory 20-second countdown per question
- **Answer review**: explanations shown at the end
- Progress bar after every answer

---

## Requirements

- Python 3.7 or higher
- No external libraries required (standard library only)

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/your-username/student-toolkit.git
cd student-toolkit

# 2. Run
python main.py
```

> **VS Code users:** If output appears delayed, run with:
> ```bash
> python -u main.py
> ```
> Or set the environment variable `PYTHONUNBUFFERED=1` in your VS Code launch config.

---

## Project Structure

```
student_toolkit/
|
+-- main.py                    <- Entry point
|
+-- gpa_calculator/
|   +-- __init__.py
|   +-- gpa.py                 <- SGPA & CGPA logic
|
+-- quiz_app/
    +-- __init__.py
    +-- quiz.py                <- Quiz engine + question bank
```

---

## Grading Scale

| Grade | Points |
|-------|--------|
| O     | 10     |
| A+    | 9      |
| A     | 8      |
| B+    | 7      |
| B     | 6      |
| C     | 5      |
| P     | 4      |
| F / AB | 0     |

---

## How to Add Quiz Questions

Open `quiz_app/quiz.py` and add to the `QUESTIONS` dictionary:

```python
{
    "q": "Your question?",
    "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
    "answer": "A",
    "explanation": "Brief explanation of the correct answer."
}
```

---

## Compatibility

| Environment        | Status  |
|--------------------|---------|
| Windows CMD        | OK      |
| Windows PowerShell | OK      |
| VS Code terminal   | OK      |
| Linux terminal     | OK      |
| macOS terminal     | OK      |

---

## Author

**Pratik**  
BCA Student -- C.M.P. Degree College, Allahabad  
University of Allahabad

---

## License

MIT License -- see [LICENSE](LICENSE)
