"""
Task: Date & Time Operations - Target Date Countdown & Duration

Practice using Python's datetime module:
1. Format and display current system timestamp with strftime().
2. Parse user string input into a date object using strptime().
3. Compare dates and calculate timedelta durations for upcoming or past events.
"""

import datetime

current_datetime = datetime.datetime.now().strftime("Today is: %A, %B %d, %Y (%I:%M %p)")
print(current_datetime)

today = datetime.datetime.now().date()

target_date_str = input("Enter Target Date (DD-MM-YYYY): ")
target_date = datetime.datetime.strptime(target_date_str, "%d-%m-%Y").date()

if today < target_date:
    days_left = (target_date - today).days
    day_name = target_date.strftime("%A")
    print(f"{days_left} days left till your target date! (Falls on a {day_name})")
elif target_date < today:
    days_passed = (today - target_date).days
    day_name = target_date.strftime("%A")
    print(f"{days_passed} days passed since your target date! (Was a {day_name})")
else:
    print("Today is your target date!")
