import random

def select_one(arg_start, arg_last = 0):
    if arg_last == 0:
        arg_last = arg_start
    for i in range(arg_start, arg_last + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()

def select_two(arg_height):
    num_list = []
    num_len = 3 if arg_height == 2 else 6
    while len(num_list) < num_len:
        number = random.randint(0, 9)

        isExist = False
        for num in num_list:
            if num == number:
                isExist = True
                break

        if not isExist:
            num_list.append(number)

    count = 0
    for i in range(arg_height):
        print(" " * (arg_height - i - 1), end="")
        for j in range(i + 1):
            print(num_list[count], end="")
            count += 1
        print()


while True:
    print("----------------\n1. 구구단 출력\n2. 랜덤값 삼각형 출력\n3. 종료\n----------------")
    user_select = input("원하는 메뉴 번호를 입력하세요: ")

    if not (user_select >= "1" and user_select <= "3"):
        print("1~3 사이의 값을 입력하세요")
        continue

    user_select = int(user_select)
    
    if user_select == 1:
        first = True
        check = True
        while first or check:
            first = False
            answer = True
            user_select_one = list(map(int, input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n").split("~")))

            for num in user_select_one:
                if num < 2 or num > 9:
                    print("2~9 사이의 값으로 입력하세요")
                    answer = False
                    break

            if len(user_select_one) > 2 or (len(user_select_one) > 1 and user_select_one[0] > user_select_one[1]):
                print("잘못된 입력입니다.")
                answer = False

            if answer:
                select_one(*user_select_one)
                check = False

    elif user_select == 2:
        user_select_two = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)"))
        while not (user_select_two >= 2 and user_select_two <= 3):
            user_select_two = int(input("2 또는 3을 입력하세요"))

        select_two(user_select_two)

    else:
        break