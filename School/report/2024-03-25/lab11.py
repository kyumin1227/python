# 섭씨를 화씨로 변환하는 함수 작성
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# 섭씨 온도를 입력 받음
inputValue = int(input("섭씨 온도를 입력하세요: "))

# 함수의 반환값 출력
print("화씨 온도는 {}입니다.".format(convert_celsius_to_fahrenheit(inputValue)))