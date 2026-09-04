"""
Task: File I/O & Path Detection Pipeline

Build a local staging pipeline combining file detection, writing, and reading:
1. Export: Use csv.DictWriter to write raw job dictionaries to a CSV file with headers.
2. Verify: Check file existence and type using os.path.exists() and os.path.isfile().
3. Ingest: Read rows using csv.reader, skip header with next(), and calculate the average salary.
"""

import csv
import os

path = "staged_jobs.csv"

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
        print(f"[EXPORT] CSV file created at '{file_path}'")


def verify_file(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        print(f"[INFO] File '{file_path}' exists and is ready for ingestion.")
        return True
    else:
        print(f"[ERROR] File '{file_path}' does not exist!")
        return False


def read_and_calculate_average(file_path):
    total_salary = 0
    count = 0

    with open(file_path, "r") as file:
        rows = csv.reader(file)
        header = next(rows)

        for row in rows:
            total_salary += float(row[2])
            count += 1

    avg_salary = total_salary / count if count > 0 else 0
    print(f"[METRIC] Total Jobs Read: {count}")
    print(f"[METRIC] Average Salary: ${avg_salary:,.2f} USD")


if __name__ == "__main__":
    export_to_csv(path, raw_jobs)
    if verify_file(path):
        read_and_calculate_average(path)
