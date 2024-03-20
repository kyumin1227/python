# 성별을 입력받음
inputValue = input("성별을 한글로 입력하세요 (남자/여자): ")

# 남자일 경우, 여자일 경우, 나머지 값일 경우를 구분하여 출력
if (inputValue == "남자"):
    print("MAN")
elif (inputValue == "여자"):
    print("WOMAN")
else:
    print("잘못된 입력입니다.")