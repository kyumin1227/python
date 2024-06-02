score = [99, 29, 30, 40, 20, 60]

student_num = 0
sum = 0 # 합계
# 성적 리스트를 순회
for s in score:
    # 합계에 성적을 더함
    sum += s
    # 학생 수 계산
    student_num += 1

# 평균
avg = sum / student_num

print("학생수 : ", student_num, ", 총점 : ", sum, ", 평균 : ", avg)