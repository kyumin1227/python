# 문자 입력받기
inputValue = input("한 문자를 입력하세요: ")

# a, e, i, o, u 에 속하는지 확인하여 출력
if inputValue == "a" or inputValue == "e" or inputValue == "i" or inputValue == "o" or inputValue == "u":
    print(f"{inputValue}는 모음입니다.")
else:
    print(f"{inputValue}는 모음이 아닙니다.")