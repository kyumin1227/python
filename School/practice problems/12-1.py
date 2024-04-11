import random

choices = ["가위", "바위", "보"]
computer_choice = random.choice(choices)

# 입력 및 컴퓨터의 선택 출력
user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
print(computer_choice)

# 가위, 바위, 보 중에 입력했는지 확인
if user_choice in choices:

    # 가위 바위 보의 결과를 숫자로 받기
    result_num = choices.index(computer_choice) - choices.index(user_choice)

    # 결과에 맞게 출력
    if result_num == 0:
        print("결과: 무승부입니다!")    
    elif result_num == 1 or result_num == -2:
        print("결과: 당신이 졌습니다!")
    else:
        print("결과: 당신이 이겼습니다!")

else:
    print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요")