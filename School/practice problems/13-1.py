input_s = input("문자열 입력: ")
input_target = input("단어 입력: ")

tmp = ""
count = 0

for char in input_s:
    # 공백일 경우 tmp의 값을 검사
    if char == " " or char == ",":
        if tmp == input_target:
            count += 1
            tmp = ""
        else:
            tmp = ""
    # 공백이 아닌 경우 tmp에 값을 추가
    else:
        tmp += char

# tmp에 남아 있는 값 체크
if tmp == input_target:
    count += 1

print(f"단어 '{input_target}'의 출현 빈도: {count}")