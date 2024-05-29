import random

answer = random.randint(1, 100)
user = 0
win = False

for i in range(10):
    user = int(input(f"기회 {i + 1}/10 - 1부터 100 사이의 숫자를 맞춰보세요 (종료하려면 0 입력): "))

    if user == 0:
        exit()
    elif answer > user:
        print("더 큰 숫자입니다.")
    elif answer < user:
        print("더 작은 숫자입니다.")
    else:
        win = True
        break

if win:
    print("정답입니다!")
else:
    print(f"모든 기회를 사용하였습니다. 정답은 {answer}입니다.")

print("게임이 끝났습니다.")