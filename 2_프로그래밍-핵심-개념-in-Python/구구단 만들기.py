num1 = 1
num2 = 1

while num1 <= 9:
    while num2 <= 9:
        print(f"{num1} * {num2} = {num1*num2}")
        num2 += 1
    num1 += 1
    num2 = 1