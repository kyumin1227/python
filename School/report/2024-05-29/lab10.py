import random

# 1부터 100 까지의 수 중 랜덤으로 뽑음
answer = random.randint(1, 100)
user = 0
win = False

# 10번 반복
for i in range(10):
    user = int(input(f"기회 {i + 1}/10 - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): "))

    # 입력값이 0이면 종료
    if user == 0:
        exit()
    elif answer > user:
        print("더 큰 숫자입니다.")
    elif answer < user:
        print("더 작은 숫자입니다.")
    # 숫자가 같으면 win을 True로 변경하고 종료
    else:
        win = True
        break

# 반복이 종료되었을 때 win이 True면 정답 출력
if win:
    print("정답입니다!")
# 아닌 경우 출력
else:
    print(f"모든 기회를 사용하였습니다. 정답은 {answer}입니다.")

print("게임이 끝났습니다.")