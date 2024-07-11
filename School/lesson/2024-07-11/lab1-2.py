import os
import csv

path = os.getcwd()

file_path = path + "/School/data/2024_std_num_high_school.csv"

male_student = 0
female_student = 0

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if row["제외여부"] == "Y":
            continue
        male_student += int(row["계(남)"])
        female_student += int(row["계(여)"])

all_student = male_student + female_student
print(f"전체 고등학생 수: {all_student:,}")
print(f"남성 고등학생 수: {male_student:,}")
print(f"여성 고등학생 수: {female_student:,}")
print(f"남성 학생 비율: {male_student / all_student * 100:.2f} %")
print(f"여성 학생 비율: {female_student / all_student * 100:.2f} %")