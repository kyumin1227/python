numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(0, round(len(numbers)/2)):   # 파이썬에서는 // 를 사용하여 정수나눗셈 가능
    num = numbers[i]
    numbers[i] = numbers[len(numbers) - i - 1]
    numbers[len(numbers) - i - 1] = num

print("뒤집어진 리스트: " + str(numbers))