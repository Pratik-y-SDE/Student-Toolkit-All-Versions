"""
Quiz App
--------
A multi-topic MCQ quiz with timer, scoring, and review.
Topics: Python, Data Structures & Algorithms, General CS
"""

import time
import random
import threading

QUESTIONS = {
    "Python": [
        {
            "q": "Which of the following is used to define a function in Python?",
            "options": ["A) function", "B) def", "C) define", "D) fun"],
            "answer": "B",
            "explanation": "'def' keyword is used to define functions in Python."
        },
        {
            "q": "What is the output of: print(type([]))?",
            "options": ["A) <class 'tuple'>", "B) <class 'dict'>", "C) <class 'list'>", "D) <class 'set'>"],
            "answer": "C",
            "explanation": "[] is an empty list literal, so type([]) returns <class 'list'>."
        },
        {
            "q": "Which method removes and returns the last element of a list?",
            "options": ["A) remove()", "B) delete()", "C) pop()", "D) discard()"],
            "answer": "C",
            "explanation": "list.pop() removes and returns the last element by default."
        },
        {
            "q": "What does 'len(range(5))' return?",
            "options": ["A) 4", "B) 5", "C) 6", "D) Error"],
            "answer": "B",
            "explanation": "range(5) generates 0,1,2,3,4 — five elements, so len() returns 5."
        },
        {
            "q": "Which of the following is immutable in Python?",
            "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
            "answer": "D",
            "explanation": "Tuples are immutable — they cannot be changed after creation."
        },
        {
            "q": "What is the correct way to open a file for reading in Python?",
            "options": ["A) open('f', 'w')", "B) open('f', 'a')", "C) open('f', 'r')", "D) open('f', 'x')"],
            "answer": "C",
            "explanation": "'r' mode opens a file for reading (default mode)."
        },
    ],
    "Data Structures": [
        {
            "q": "Which data structure follows LIFO (Last In First Out) order?",
            "options": ["A) Queue", "B) Stack", "C) Linked List", "D) Tree"],
            "answer": "B",
            "explanation": "Stack follows LIFO — the last inserted element is removed first."
        },
        {
            "q": "What is the time complexity of binary search?",
            "options": ["A) O(n)", "B) O(n²)", "C) O(log n)", "D) O(1)"],
            "answer": "C",
            "explanation": "Binary search repeatedly halves the search space, giving O(log n)."
        },
        {
            "q": "In a singly linked list, each node contains:",
            "options": [
                "A) Only data",
                "B) Data and two pointers",
                "C) Data and one pointer (next)",
                "D) Only a pointer"
            ],
            "answer": "C",
            "explanation": "A singly linked list node holds data and a 'next' pointer to the following node."
        },
        {
            "q": "Which traversal of a Binary Search Tree gives sorted output?",
            "options": ["A) Pre-order", "B) Post-order", "C) Level-order", "D) In-order"],
            "answer": "D",
            "explanation": "In-order traversal (Left → Root → Right) of a BST yields sorted ascending order."
        },
        {
            "q": "What is the worst-case time complexity of Bubble Sort?",
            "options": ["A) O(n log n)", "B) O(n)", "C) O(n²)", "D) O(log n)"],
            "answer": "C",
            "explanation": "Bubble Sort has O(n²) worst-case due to nested comparisons."
        },
        {
            "q": "A Queue is best implemented using which structure for O(1) enqueue and dequeue?",
            "options": ["A) Array", "B) Binary Tree", "C) Circular Array or Linked List", "D) Hash Table"],
            "answer": "C",
            "explanation": "Circular arrays or linked lists allow O(1) enqueue and dequeue operations."
        },
    ],
    "General CS": [
        {
            "q": "What does CPU stand for?",
            "options": [
                "A) Central Processing Unit",
                "B) Computer Processing Utility",
                "C) Central Program Unit",
                "D) Core Processing Unit"
            ],
            "answer": "A",
            "explanation": "CPU stands for Central Processing Unit — the brain of the computer."
        },
        {
            "q": "Which layer of the OSI model is responsible for routing?",
            "options": ["A) Data Link", "B) Transport", "C) Network", "D) Session"],
            "answer": "C",
            "explanation": "The Network layer (Layer 3) handles logical addressing and routing."
        },
        {
            "q": "What does SQL stand for?",
            "options": [
                "A) Structured Query Language",
                "B) Simple Query Language",
                "C) Standard Query Logic",
                "D) Sequential Query Language"
            ],
            "answer": "A",
            "explanation": "SQL stands for Structured Query Language, used to manage relational databases."
        },
        {
            "q": "Which of these is a non-volatile memory?",
            "options": ["A) RAM", "B) Cache", "C) ROM", "D) Register"],
            "answer": "C",
            "explanation": "ROM (Read-Only Memory) retains data even when power is off — it is non-volatile."
        },
        {
            "q": "What is the binary representation of decimal 10?",
            "options": ["A) 1010", "B) 1100", "C) 1001", "D) 0110"],
            "answer": "A",
            "explanation": "10 = 8+2 = 1010 in binary."
        },
        {
            "q": "Which protocol is used to assign IP addresses automatically?",
            "options": ["A) FTP", "B) HTTP", "C) DHCP", "D) DNS"],
            "answer": "C",
            "explanation": "DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses."
        },
    ],
}

def timed_input(prompt, timeout):
    """
    Prompt for input with a timeout (cross-platform using threading).
    Returns the user's answer, or '' if time runs out.
    """
    result = [None]

    def _get_input():
        try:
            result[0] = input(prompt).strip().upper()
        except EOFError:
            result[0] = ''

    t = threading.Thread(target=_get_input, daemon=True)
    t.start()
    t.join(timeout)

    if t.is_alive():
        # Thread is still blocked on input() — signal timeout
        result[0] = '__TIMEOUT__'
        return '__TIMEOUT__'

    return result[0]



def display_progress(current, total):
    filled = int((current / total) * 20)
    bar    = "█" * filled + "░" * (20 - filled)
    print(f"  Progress: [{bar}] {current}/{total}")

def run_quiz(topic, questions, timed=False):
    score      = 0
    review     = []
    total      = len(questions)
    start_time = time.time()

    print(f"\n{'=' * 50}")
    print(f"  Topic: {topic}  |  Questions: {total}")
    if timed:
        print(f"  Mode : Timed (20 seconds per question)")
    print(f"{'=' * 50}")
    print("  Type the letter (A/B/C/D) for your answer.")
    print("  Type 'skip' to skip a question.\n")
    input("  Press Enter to begin...")

    for i, item in enumerate(questions, 1):
        print(f"\n  Q{i}. {item['q']}")
        print()
        for opt in item['options']:
            print(f"      {opt}")
        print()
        q_start = time.time()

        if timed:
            print(f"\n  ⏱  You have 20 seconds!")

        # --- BUG FIX: replaced broken while+elapsed loop with timed_input ---
        ans = ''
        while True:
            if timed:
                remaining = max(0, 20 - int(time.time() - q_start))
                raw = timed_input(f"\n  Your answer [{remaining}s left]: ", remaining + 1)
            else:
                raw = input("\n  Your answer: ").strip().upper()

            if raw == '__TIMEOUT__' or (timed and time.time() - q_start >= 20):
                print("\n  ⏰ Time's up for this question!")
                ans = ''
                break

            if raw in ['A', 'B', 'C', 'D', 'SKIP']:
                ans = raw
                break
            print("  [!] Enter A, B, C, D, or 'skip'.")
        # --- END FIX ---

        if ans == item['answer']:
            print("  ✅ Correct!")
            score += 1
            review.append((item['q'], ans, item['answer'], True, item['explanation']))
        elif ans == 'SKIP' or ans == '':
            print(f"  ⏭  Skipped. Correct answer: {item['answer']}")
            review.append((item['q'], "Skipped", item['answer'], False, item['explanation']))
        else:
            print(f"  ❌ Wrong! Correct answer: {item['answer']}")
            review.append((item['q'], ans, item['answer'], False, item['explanation']))

        # BUG FIX: show updated progress AFTER answering so final question shows 6/6
        display_progress(i, total)

    elapsed_total = time.time() - start_time

    print(f"\n{'=' * 50}")
    print(f"           QUIZ COMPLETE — {topic}")
    print(f"{'=' * 50}")
    print(f"  Score       : {score} / {total}")
    print(f"  Percentage  : {(score/total)*100:.1f}%")
    print(f"  Time Taken  : {elapsed_total:.1f} seconds")

    pct = (score / total) * 100
    if pct == 100:
        grade = "Perfect Score! 🏆"
    elif pct >= 80:
        grade = "Excellent! ⭐"
    elif pct >= 60:
        grade = "Good 👍"
    elif pct >= 40:
        grade = "Average — keep practicing"
    else:
        grade = "Needs more revision ⚠"

    print(f"  Remark      : {grade}")
    print(f"{'=' * 50}")

    show_review = input("\n  Show answer review? (y/n): ").strip().lower()
    if show_review == 'y':
        print(f"\n{'=' * 50}")
        print("            ANSWER REVIEW")
        print(f"{'=' * 50}")
        for idx, (q, given, correct, is_correct, explanation) in enumerate(review, 1):
            status = "✅" if is_correct else "❌"
            print(f"\n  {idx}. {q}")
            print(f"     Your answer : {given}")
            print(f"     Correct     : {correct}  {status}")
            print(f"     Explanation : {explanation}")
        print(f"{'=' * 50}")

def run():
    while True:
        print("\n╔══════════════════════════════╗")
        print("║          QUIZ APP            ║")
        print("╠══════════════════════════════╣")
        print("║  1. Python                   ║")
        print("║  2. Data Structures          ║")
        print("║  3. General CS               ║")
        print("║  4. Random Mixed Quiz        ║")
        print("║  5. Back to Main Menu        ║")
        print("╚══════════════════════════════╝")

        choice = input("\n  Enter choice (1-5): ").strip()

        if choice in ['1', '2', '3']:
            topics = {
                '1': 'Python',
                '2': 'Data Structures',
                '3': 'General CS'
            }
            topic     = topics[choice]
            questions = QUESTIONS[topic].copy()
            random.shuffle(questions)
            timed     = input("\n  Enable timed mode? (y/n): ").strip().lower() == 'y'
            run_quiz(topic, questions, timed)

        elif choice == '4':
            all_qs = []
            for topic, qs in QUESTIONS.items():
                for q in qs:
                    all_qs.append({**q, '_topic': topic})
            random.shuffle(all_qs)
            num      = min(10, len(all_qs))
            # BUG FIX: strip the '_topic' helper key before passing to run_quiz
            selected = [{k: v for k, v in q.items() if k != '_topic'} for q in all_qs[:num]]
            timed    = input("\n  Enable timed mode? (y/n): ").strip().lower() == 'y'
            run_quiz("Mixed (Random)", selected, timed)

        elif choice == '5':
            break
        else:
            print("  [!] Invalid choice.")
