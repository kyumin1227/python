score = [99, 29, 30, 40, 20, 60]

student_num = 0
sum = 0
for s in score:
    sum += s
    student_num += 1

avg = sum / student_num

print("학생수 : ", student_num, ", 총점 : ", sum, ", 평균 : ", avg)