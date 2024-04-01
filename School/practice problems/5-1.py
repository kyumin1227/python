# 입력
num1 = int(input("첫 번째 수 입력: "))
num2 = int(input("두 번째 수 입력: "))
num3 = int(input("세 번째 수 입력: "))

# 출력
if (num1 == num2 and num2 == num3):
    print("모든 수가 같습니다.")
elif (num1 == num2):
    print("두 수가 같습니다. (", num1, "와 ", num2, ")", sep="")
elif (num2 == num3):
    print("두 수가 같습니다. (", num2, "와 ", num3, ")", sep="")
elif (num1 == num3):
    print("두 수가 같습니다. (", num1, "와 ", num3, ")", sep="")
else:
    max_num = num1
    if max_num < num2:
        max_num = num2
    if max_num < num3:
        max_num = num3
    print("모든 수가 다릅니다. 가장 큰 수는 ", max_num, "입니다.", sep="")