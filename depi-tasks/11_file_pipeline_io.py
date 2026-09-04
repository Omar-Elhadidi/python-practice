"""
Task: Local File Pipeline - File Detection, CSV Export & Ingestion

Demonstrate File I/O operations (Bro Code #68, #69, #70):
1. Detect and verify file existence using os.path.exists() and os.path.isfile().
2. Export structured dictionaries to a CSV file using csv.DictWriter with headers.
3. Read CSV data using csv.reader, skip headers with next(), and calculate salary metrics.
"""

import csv
import json
import os

path = "C:/Users/user/Desktop/hadidi.csv"

raw_jobs = [
    {"company": "Amazon", "role": "Data Engineer", "salary": 140000},
    {"company": "Google", "role": "Software Engineer", "salary": 165000},
    {"company": "Meta", "role": "Data Analyst", "salary": 110000},
    {"company": "Spotify", "role": "Data Engineer", "salary": 135000},
]


def export_to_csv(file_path, data):
    headers = list(data[0].keys())

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        print(f"CSV file created at {file_path}")


def verify_file(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print(f"File '{file_path}' exists and is ready for ingestion.")
        return True
    else:
        print(f"File '{file_path}' does not exist!")
        return False


def read_and_calculate_average(file_path):
    total_salary = 0
    count = 0

    with open(file_path, "r") as file:
        rows = csv.reader(file)
        header = next(rows)

        for row in rows:
            print(f"Salary found: ${float(row[2]):,.0f}")
            total_salary += float(row[2])
            count += 1

        avg_salary = total_salary / count

    print(f"Average Salaries: ${avg_salary:,.2f}")


if __name__ == "__main__":
    export_to_csv(path, raw_jobs)
    if verify_file(path):
        read_and_calculate_average(path)
