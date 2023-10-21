num1 = 0;
num2 = 1;
count = 0

while count < 50:
    num = num2
    num2 += num1
    num1 = num
    print(num1)
    count += 1