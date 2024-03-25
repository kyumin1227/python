# 소득세를 구하는 함수 작성
def calculate_tax(income):
    tax = 0

    # 10000달러 미만의 세금 계산
    if income > 0:
        tax += min(1000, income / 10)
        income -= 10000
    
    # 10000달러 초과 20000달러 미만의 세금 계산
    if income > 0:
        tax += min(1500, income * 15 / 100)
        income -= 10000

    # 나머지 금액의 세금 계산
    if income > 0:
        tax += income / 5

    return tax

# 소득 금액 입력 받음
inputNum = int(input("소득 금액을 입력하세요: "))

# 함수의 반환 값 출력
print("소득세는 {}달러입니다.".format(calculate_tax(inputNum)))