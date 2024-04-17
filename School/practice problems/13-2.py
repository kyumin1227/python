# 문자열 입력받기 split
msg = input("문자열 입력:").split()
# 사용자 지정 단어 입력받기
input_msg = input("단어 입력:")
# 카운트 선언
count = 0
# 문자열를 반복
for message in msg :
# 지정 단어가 나오면 카운트
    if input_msg == message:
        count += 1
# 카운트 결과를 출력
print("단어{}의 출현 빈도:".format(input_msg), count)
