
from pathlib import Path
import json
from datetime import datetime

BASE = Path(__file__).parent
DATA = BASE / "data"

def save_score(topic, score, total):
    DATA.mkdir(exist_ok=True)
    with open(DATA / "scores.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} | {topic} | {score}/{total}\n")

def grade_from_percent(percent):
    if percent >= 90: return "A+"
    if percent >= 80: return "A"
    if percent >= 70: return "B"
    if percent >= 60: return "C"
    return "D"
