input_s = input("문자열 입력: ")
input_target = input("단어 입력: ")

count = 0   # 출현 빈도
index = 0   # target을 확인 할 인덱스
isBlank = True  # 공백 확인

for i in range(len(input_s)):
    # index가 0일 경우 앞의 값이 공백이고 첫 글자가 일치하면 체크 시작
    if index == 0:
        if isBlank and input_s[i] == input_target[index]:
            index += 1
    # index가 0이 아닌 경우 글자의 일치를 확인
    else:
        if input_s[i] == input_target[index]:
            index += 1
        else:
            index = 0
        
    # 타겟 단어와 모든 문자가 일치하고 단어가 끝이난 경우 count 1 증가 및 index 초기화
    if index == len(input_target):
        if (i == len(input_s) - 1 or input_s[i + 1] == " " or input_s[i + 1] == ","):
            count += 1
            index = 0
        else:
            index = 0
    
    # 공백 검사
    if input_s[i] == " " or input_s[i] == ",":
        isBlank = True
    else:
        isBlank = False

print(f"단어 '{input_target}'의 출현 빈도: {count}")