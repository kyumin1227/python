# 방향을 입력 받음
inputValue = input("방향을 입력하세요(left, right, up, down): ")

# 방향을 확인하여 출력, 만약 일치하는 방향이 없다면 "알 수 없는 명령입니다"를 출력
if (inputValue == "left"):
    print("왼쪽으로 이동합니다.")
elif (inputValue == "right"):
    print("오른쪽으로 이동합니다.")
elif (inputValue == "up"):
    print("위로 이동합니다.")
elif (inputValue == "down"):
    print("아래로 이동합니다.")
else:
    print("알 수 없는 명령입니다.")