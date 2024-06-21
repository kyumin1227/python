import random

# 숫자 체크
# 数字をチェック
def check(arg_num):
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == arg_num:
                bingo_board[i][j] = 0
                return (j, i)
            
    return False

# 빙고 개수 체크
# bingoの数をチェック
def bingo_check(arg_x, arg_y):
    bingo = 0

    # 가로 세로
    # 横　縦
    if sum(bingo_board[arg_y]) == 0:
        bingo += 1
    if sum(line[arg_x] for line in bingo_board) == 0:
        bingo += 1

    # 대각선
    # 斜め
    if arg_x - arg_y == 0 and sum(bingo_board[i][i] for i in range(5)) == 0:
        bingo += 1
    if arg_x + arg_y == 4 and sum(bingo_board[i][4 - i] for i in range(5)) == 0:
        bingo += 1

    return bingo

# 빙고판 생성
# bingo版を作る
def create_board():
    global bingo_board
    candi_numbers = [num for num in range(1, 26)]

    for _ in range(5):
        bingo_line = []
        for _ in range(5):
            index = random.randint(0, len(candi_numbers) - 1)
            bingo_line.append(candi_numbers.pop(index))
        bingo_board.append(bingo_line)
            

bingo_board = []

create_board()

# 빙고판 출력
# bingo版を出力
for line in bingo_board:
    for num in line:
        print(str(num).zfill(2) + " ", end="")
    print()

# 빙고 시작
# ゲームの始め
bingo = 0
current_bingo = 0
count = 0
while current_bingo < 3:
    count += 1
    number = int(input(f"\n{count}번째 시도 - 숫자를 입력 해 주세요: "))
    while not (1 <= number <= 25):
        number = int(input("1에서 25사이의 숫자를 입력 해 주세요: "))

    isCheck = check(number)

    if isCheck:
        print("숫자를 체크했습니다!")
    else:
        print("이미 체크 된 숫자입니다")
        continue

    bingo = bingo_check(*isCheck)

    if bingo > 0:
        print("BINGO!!!!!!!")
        current_bingo += bingo

    print(f"현재까지의 빙고: {current_bingo}")

print(f"{current_bingo}개 빙고!! 시도 횟수 {count}")