# 숫자를 입력 받음
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))

# 결과값에 num1을 넣은 후 num2, num3와 차례로 비교해서 가장 큰 값을 출력
result = num1
if num2 > result:
    result = num2
if num3 > result:
    result = num3

print(f"가장 큰 숫자는 {result}입니다.")