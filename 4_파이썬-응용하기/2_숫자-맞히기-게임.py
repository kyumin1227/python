import random

target_number = random.randint(1, 20)

for i in range(0, 5):
    if(i == 4):
        print(f"아쉽습니다 정답은 {target_number}였습니다.")
        break
    user_number = int(input(f"기회가 {4 - i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    if(user_number == target_number):
        print(f"축하합니다. {i + 1}번만에 숫자를 맞히셨습니다.")
        break
    elif(user_number > target_number):
        print("Down")
    elif(user_number < target_number):
        print("Up")
    