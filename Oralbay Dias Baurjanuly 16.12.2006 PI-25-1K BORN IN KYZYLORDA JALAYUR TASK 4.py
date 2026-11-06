import math
import random
from datetime import date, timedelta
import sys
import re

# ==========================================
# 1. Find the hypotenuse using math.sqrt() and math.pow()
# ==========================================
print("--- 1. Hypotenuse Calculation ---")
a = 3
b = 4
hypotenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f"The hypotenuse of a triangle with legs {a} and {b} is: {hypotenuse}\n")


# ==========================================
# 2. Shuffle a list of cards using random.shuffle()
# ==========================================
print("--- 2. Shuffle Cards ---")
cards = ["Ace", "King", "Queen", "Jack"]
print(f"Original cards: {cards}")
random.shuffle(cards)
print(f"Shuffled cards: {cards}\n")


# ==========================================
# 3. Add 100 days to today's date using datetime.timedelta
# ==========================================
print("--- 3. Add 100 Days ---")
today = date.today()
future_date = today + timedelta(days=100)
print(f"Today's date: {today}")
print(f"Date in 100 days: {future_date}\n")


# ==========================================
# 4. Print command-line arguments using sys.argv
# ==========================================
print("--- 4. Command-Line Arguments (sys.argv) ---")
print(f"All arguments: {sys.argv}")
for index, arg in enumerate(sys.argv):
    print(f"Argument {index}: {arg}")
print()


# ==========================================
# 5. Check if a string consists only of Russian letters using re.match()
# ==========================================
print("--- 5. Check Only Russian Letters ---")

def check_russian_letters(input_text):
    # Pattern to match only Russian characters from start to end
    pattern = r'^[а-яёА-ЯЁ]+$'
    if re.match(pattern, input_text):
        print(f"'{input_text}' -> Consists ONLY of Russian letters.")
    else:
        print(f"'{input_text}' -> Contains other characters (numbers, English, spaces, etc.).")

# Test cases
check_russian_letters("Привет")  # True
check_russian_letters("Hello")   # False
check_russian_letters("Ёжик")    # True
check_russian_letters("Привет123") # False