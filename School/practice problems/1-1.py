age = int(input("사용자의 나이를 입력해주세요: "))

if age > 0 and age <= 12:
    print("어린이 이용권을 사용할 수 있습니다.")
elif age > 12 and age <= 18:
    print("청소년 이용권을 사용할 수 있습니다.")
elif age > 18:
    print("성인 이용권을 사용할 수 있습니다.")