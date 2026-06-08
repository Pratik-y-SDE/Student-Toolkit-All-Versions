"""
Student Toolkit
===============
A command-line utility for BCA / CS students.

Tools included:
  1. GPA Calculator  — SGPA and CGPA computation
  2. Quiz App        — MCQ quiz on Python, DSA, General CS

Author : Pratik
Version: 1.0.0
"""

import sys
import os

# Make sub-packages importable regardless of how/where the script is launched
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from gpa_calculator import gpa
from quiz_app       import quiz

BANNER = r"""
╔════════════════════════════════════════════╗
║                                            ║
║        >>>  STUDENT TOOLKIT  >>>             ║
║                                            ║
║   Your all-in-one academic utility belt    ║
║                                            ║
╚════════════════════════════════════════════╝
"""

def main():
    print(BANNER)

    while True:
        print("\n  Main Menu")
        print("  " + "─" * 30)
        print("  1.  GPA Calculator")
        print("  2.  Quiz App")
        print("  0.  Exit")
        print("  " + "─" * 30)

        choice = input("\n  Enter choice: ").strip()

        if choice == '1':
            gpa.run()
        elif choice == '2':
            quiz.run()
        elif choice == '0':
            print("\n  Goodbye! Study hard. \n")
            break
        else:
            print("  [!] Invalid choice. Enter 0, 1, or 2.")

if __name__ == "__main__":
    main()
