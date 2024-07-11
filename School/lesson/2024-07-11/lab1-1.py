import os
import csv

path = os.getcwd()

file_path = path + "/School/data/2024_std_num_high_school.csv"

education_office = set()

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        education_office.add(row["시도교육청"])

for index, item in enumerate(education_office, start=1):
    print(f"{index}번, {item}")