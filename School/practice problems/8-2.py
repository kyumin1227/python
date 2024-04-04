baseValue = float(input("기본값을 입력하세요: "))

def selectOperation():
    global baseValue

    # 선택 가능 옵션 출력
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")

    select = int(input("선택: "))
    value = int(input("숫자 입력: "))

    # 나누기에 0인 경우 확인
    if select == 4 and value == 0:
        print("에러: 0으로 나눌 수 없습니다.")
        return
        
    if select == 1:
        baseValue += value
    elif select == 2:
        baseValue -= value
    elif select == 3:
        baseValue *= value
    elif select == 4:
        baseValue /= value
        
    print("연산 결과: ", baseValue)
    return

selectOperation()