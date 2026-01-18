import csv
import os

def read_csv(file_path):
    assert os.path.exists(file_path), f"CSV file not found: {file_path}"

    data = []
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if any(row.values()):   # prevents empty rows
                data.append(row)

    return data
