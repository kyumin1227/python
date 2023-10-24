# 자리수 합 리턴
def sum_digit(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
sum = 0
for i in range(1, 1001):
    num = sum_digit(i)
    sum += int(num)
    
print(sum)