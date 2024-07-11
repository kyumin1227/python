import os
import csv

path = os.getcwd()

file_path = path + "/School/data/2024_std_num_high_school.csv"

male_students = [0] * 3
female_students = [0] * 3

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if row["제외여부"] == "Y":
            continue
        for i in range(3):
            male_students[i] += int(row[f"{i + 1}학년(남)"])
            female_students[i] += int(row[f"{i + 1}학년(여)"])

print(f"전체 고등학생 수: {sum(male_students) + sum(female_students)}")
for i in range(3):
    print(f"{i + 1}학년 - 남학생 수: {male_students[i]:,}, 여학생 수: {female_students[i]:,}, 남학생 비율: {male_students[i] / (male_students[i] + female_students[i]) * 100:.2f}%, 여학생 비율: {female_students[i] / (male_students[i] + female_students[i]) * 100:.2f}%")