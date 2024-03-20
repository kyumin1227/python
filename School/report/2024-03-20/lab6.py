# 나이를 입력 받음
age = input("나이를 입력하세요: ")

# 나이를 숫자로 변환 후 정해진 값에 맞게 그룹을 출력
try:
    age = int(age)

    if (age >= 13 and age <= 19):
        print("You are in the 'Teenager' age group.")
    elif (age >= 20 and age <= 64):
        print("You are in the 'Adult' age group.")
    elif (age > 64):
        print("You are in the 'Senior' age group.")
    else:
        print("You are in the 'Unknown age group' age group.")

# 숫자가 아닌 값이 들어올 경우 "Invalid input" 을 출력
except:
    print("Invalid input")