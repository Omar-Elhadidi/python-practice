"""
Task: Event Countdown & Date Calculator

Working with Python datetime module (Bro Code #72):
1. Format current timestamp using strftime().
2. Parse user-entered date string using strptime().
3. Compare dates and calculate the exact difference in days using date arithmetic.
"""

import datetime

current_datetime = datetime.datetime.now().strftime("Today is: %A, %B %d, %Y (%H:%M %p)")
print(current_datetime)

today = datetime.datetime.now().date()

target_date = input("Enter Target Day (D-M-Y): ")
target_date = datetime.datetime.strptime(target_date, "%d-%m-%Y").date()

if today < target_date:
    days_left = (target_date - today).days
    print(f"{days_left} days left till your target date!")

elif target_date < today:
    days_passed = (today - target_date).days
    print(f"{days_passed} days passed since your target date!")

else:
    print("today is your target date")
