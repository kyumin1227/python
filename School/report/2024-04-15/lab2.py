import random

# 수를 랜덤으로 뽑는 함수 (check를 통과하면 숫자를 반환, 통과하지 못하면 함수를 재호출)
def random_num():
    num = random.randint(1, 100)

    if check_num(num):
        return num
    else:
        return random_num()

# 수가 중복되는지 확인하는 함수 (중복되면 False 중복되지 안으면 True 반환)
def check_num(num):
    global number_list

    for number in number_list:
        if number == num:
            return False
    return True

number_list = []
success = False

while not success:
    n = int(input("N값을 입력하세요 (1-100): "))
    
    # n이 범위를 만족하는 경우
    if n > 0 and n <= 100:
        # 리스트 생성
        for _ in range(n):
            number_list.append(random_num())
        print("생성된 리스트:", number_list)

        while True:
            input_index = int(input(f"원하는 원소의 인덱스를 입력하세요 (0-{n - 1}): "))
            # input_index가 범위를 만족하는 경우
            if input_index >= 0 and input_index < n:
                print("선택한 인덱스의 원소:", number_list[input_index])
                success = True
                break
            # input_index가 범위를 벗어난 경우
            else:
                print("에러: 유효한 인덱스 범위를 벗어났습니다.")
                continue
    # n이 범위를 벗어난 경우
    else:
        print("에러: N은 1 이상 100 이하의 정수여야 합니다.")
        continue