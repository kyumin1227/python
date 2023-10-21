sum = 0
num = 0

while num < 1000:
    if(num % 2 == 0):
        sum += num
    elif(num % 3 == 0):
        sum += num
    num += 1

print(sum)