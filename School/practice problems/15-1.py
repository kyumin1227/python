import random

win = 0
divide = 0
lose = 0

select_list = ["가위", "바위", "보"]
msg = "전적: {}승 {}패 {}무"

# 둘 중 하나가 2승이 될 때 까지 반복
while win < 2 and lose < 2:
    user_select = input("가위, 바위, 보 중 하나를 입력하세요: ")
    
    # 올바른 값이 입력되었을 경우
    if user_select == "가위" or user_select == "바위" or user_select == "보":
        computer_select = random.choice(select_list)

        print("컴퓨터: ", computer_select)

        user_num = select_list.index(user_select)
        computer_num = select_list.index(computer_select)

        # 결과를 숫자로 받아서 확인
        result_num = user_num - computer_num

        if result_num == 0:
            divide += 1
            print("무승부! 현재 " + msg.format(win, lose, divide))
        elif result_num == 1 or result_num == -2:
            win += 1
            print("승리! 현재 " + msg.format(win, lose, divide))
        else:
            lose += 1
            print("패배! 현재 " + msg.format(win, lose, divide))

    # 올바르지 않은 값이 입력되었을 경우
    else:
        print("가위, 바위, 보 중에서 선택하세요.")

# 종료 시 실행
print(msg.format(win, lose, divide))
if win >= 2:
    print("최종 승자: 사용자")
else:
    print("최종 승자: 컴퓨터")