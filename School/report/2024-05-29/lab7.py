height = 5  # 높이

for i in range(height * 2 - 1):
    # 공백과 별의 수를 계산
    blank = height - i - 1 if i < height else i - height + 1
    star = 1 + 2 * i if i < height else 4 * height - 2 * i - 3

    # 출력
    print(" " * blank, end="")
    print("*" * star, end="")

    print()