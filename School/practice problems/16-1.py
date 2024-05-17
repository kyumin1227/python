import random

# 랜덤한 수 세개를 중복없이 뽑는 함수
def getComputerNumber():
    number_list = []

    while len(number_list) < 3:
        number = random.randint(0, 9)
        isExist = False
        for num in number_list:
            if num == number:
                isExist = True
        if not isExist:
            number_list.append(number)

    return number_list

# Strike와 Ball을 계산하는 함수
def getStrikeAndBall(argList):
    strike = 0
    ball = 0

    for i in range(3):
        for j in range(3):
            if computer_list[i] == argList[j] and i == j:
                strike += 1
            elif computer_list[i] == argList[j]:
                ball += 1

    return strike, ball
    
    

computer_list = getComputerNumber()
win = False
out = 0

# 5번 실행
for i in range(5):
    # 숫자를 입력 받아 계산
    user_list = list(map(int, input(f"시도 {i + 1}: 입력한 숫자 - ").split()))
    strike, ball = getStrikeAndBall(user_list)

    if strike + ball == 0:
        out += 1

    print(f"결과: {strike} Strike, {ball} Ball, {out} Out" if out > 0 else f"결과: {strike} Strike, {ball} Ball")
    
    # 종료 조건
    if strike == 3:
        win = True
        break

    if out == 2:
        break

# 종료 시 결과 확인
if win:
    print("\n게임 종료: 승리")
elif out == 2:
    print("\n게임 종료: 패배 (스트라이크 아웃)")
else:
    print("\n게임 종료: 패배 (시도 횟수 5회 초과)")

print(f"정답: {" ".join(map(str, computer_list))}")