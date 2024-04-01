# 입력
n = int(input("N 입력: "))

# 줄 개수
for i in range(1, n * 2):
    
    # 별의 개수가 최대 값 찍기 전
    if i <= n:
        # 별 개수
        for j in range(0, i):
            # end: 줄 변경을 막기 위해 입력
            print("*", end="")

    # 별의 개수가 최대 값 찍은 후
    else:
        # 별 개수
        for j in range(n * 2, i, -1):
            print("*", end="")

    # 줄 변경
    print()