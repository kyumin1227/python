import random

# 1번의 입력 값 검증
def check_one(arg_list):
    for num in arg_list:
        if num < 2 or num > 9:
            return False
        
    if len(arg_list) > 2 or (len(arg_list) > 1 and arg_list[0] > arg_list[1]):
        return False
    
    return True

# 1번의 출력
def result_one(arg_start, arg_last = 0):
    if arg_last == 0:
        arg_last = arg_start
    for i in range(arg_start, arg_last + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()

# 2번의 입력 값 검증
def check_two(arg_num):
    if arg_num != 2 and arg_num != 3:
        return False

    return True

# 2번의 출력
def result_two(arg_num):
    num_list = []
    num_len = 3 if arg_num == 2 else 6

    # 출력할 숫자를 선정
    while len(num_list) < num_len:
        random_num = random.randint(0, 9)

        if random_num not in num_list:
            num_list.append(random_num)

    count = 0
    for i in range(arg_num):
        print(" " * (arg_num - i - 1), end="")
        for _ in range(i + 1):
            print(num_list[count], end="")
            count += 1
        print()


while True:
    print("----------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n----------------")
    user_select = int(input("원하는 메뉴 번호를 입력하세요: "))

    if not (user_select >= 1 and user_select <= 3):
        print("1~3 사이의 값을 입력하세요")
        continue

    
    if user_select == 1:
        while True:
            user_select_one = input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n")
            user_select_one = list(map(int, user_select_one.split("~")))
            
            if check_one(user_select_one):
                result_one(*user_select_one)
                break
            else:
                print("2~9 사이의 값으로 입력하세요")

    elif user_select == 2:
        while True:
            user_select_two = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하"))

            if check_two(user_select_two):
                result_two(user_select_two)
                break
            else:
                print("2 또는 3을 입력하세요")

    else:
        break