import random

def isIn(arg_value, arg_list):
    for value in arg_list:
        if value == arg_value:
            return True
    return False

def checkStrikeAndBall(arg_com_list, arg_user_list):
    strike = 0
    ball = 0
    for i in range(len(arg_com_list)):
        for j in range(len(arg_user_list)):
            if arg_com_list[i] == arg_user_list[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return strike, ball

# 랜덤으로 숫자 생성
com_sel_num = []
while len(com_sel_num) < 3:
    num = random.randint(0, 9)
    if not isIn(num, com_sel_num):
        com_sel_num.append(num)

print(com_sel_num)

strike = 0
ball = 0
out = 0
count = 0

while strike < 3 and out < 3 and count < 5:
    count += 1
    user_sel_num = list(map(int, input(f"시도 {count}: 입력한 숫자 - ").split()))
    strike, ball = checkStrikeAndBall(com_sel_num, user_sel_num)
    if strike + ball < 1:
        out += 1

    out_msg = "" if out == 0 else f", {out} Out"

    print(f"결과: {strike} Strike, {ball} Ball{out_msg}")

result_msg = "승리" if strike == 3 else "패배 (시도 횟수 5회 초과)" if count == 5 else "패배 (스트라이크 아웃)"

print(f"게임 종료: {result_msg}\n정답: {" ".join(map(str, com_sel_num))}")