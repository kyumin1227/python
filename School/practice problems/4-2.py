password = input("비밀번호를 입력하세요: ")

condition1 = False
condition2 = False
condition3 = False

# 문자열로 된 숫자 리스트 생성
number_list = list(map(str, [i for i in range(0, 10)]))

# 조건 검증
# 1번 조건 (8자 이상인지)
if len(password) >= 8:
    condition1 = True
for c in password:
    # 2번 조건 (숫자인지)
    if c in number_list:
        condition2 = True
    # 3번 조건 (대문자인지)
    if c.isupper():
        condition3 = True

# 출력
if condition1 and condition2 and condition3:
    print("비밀번호가 안전합니다.")
else:
    print("비밀번호가 안전하지 않습니다.")