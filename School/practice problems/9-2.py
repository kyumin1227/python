# 입력값을 리스트로 변환
resident_number = list(input("주민번호를 입력하세요: "))

resident_number.remove("-")
check_nums = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

sum = 0

for i in range(12):
    sum += int(resident_number[i]) * check_nums[i]

# 검증 후 출력
if (11 - (sum % 11)) % 10 == int(resident_number[-1]):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")