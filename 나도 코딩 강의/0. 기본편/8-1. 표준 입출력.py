# # 표준 입출력
# import sys
# # 터미널에서의 출력 결과는 똑같지만 log 등에서 체크할 때 구분 가능
# print("Python", "Java", file=sys.stdout)    # 표준 출력
# print("Python", "Java", file=sys.stderr)    # 표준 에러

# 출력
# Python Java
# Python Java

# # 출력 활용
# print("Python", "Java", sep=" vs ", end=" ")    # sep이 기본은 " " 값이며 변경 가능
# print("Python", "Java", sep=" vs ", end=" ")

# 출력
# Python vs Java Python vs Java

# 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 출력
# 수학      :   0
# 영어      :  50
# 코딩      : 100
    
# 은행 대기 순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# 출력
# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# ...
# 대기번호 : 020