import random

# 1부터 100 사이의 수를 랜덤으로 뽑음
answer = random.randint(1, 100)
user = 0

# 뽑은 숫자와 유저의 숫자가 다르면 반복
while answer != user:
    user = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    if answer > user:
        print("더 큰 숫자입니다.")
    elif answer < user:
        print("더 작은 숫자입니다.")
    else:
        print("정답입니다!")