import os
import csv

path = os.getcwd()

file_path = path + "/School/data/2024_std_num_high_school.csv"

education_office = []
male_students = []
female_students = []

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        if row["시도교육청"] not in education_office:
            education_office.append(row["시도교육청"])
            male_students.append([0] * 3)
            female_students.append([0] * 3)

        if row["제외여부"] == "Y":
            continue

        for i in range(3):
            male_students[education_office.index(row["시도교육청"])][i] += int(row[f"{i + 1}학년(남)"])
            female_students[education_office.index(row["시도교육청"])][i] += int(row[f"{i + 1}학년(여)"])

all_students = [sum(male_students[i]) + sum(female_students[i]) for i in range(len(education_office))]
index_list = list(enumerate(all_students))
sorted_list = sorted(index_list, key=lambda x: x[1], reverse=True)

print("Top 5 Education Offices by Student Numbers: ")
for i in range(5):
    print(f"{education_office[sorted_list[i][0]]}: Total Students = {sorted_list[i][1]:,} 명")

print()

for i in range(len(education_office)):
    print(f"{education_office[i]}:")
    for j in range(3):
        print(f" {j + 1}학년 - 남학생 수: {male_students[i][j]:,} 명, 여학생 수: {female_students[i][j]:,} 명")