n = 0
sum = 0

# 1000까지 반복
while n <= 1000:
    # n을 3으로 나눈 수가 0이라면 sum에 합산
    if n % 3 == 0:
        sum += n
    n += 1

print(sum)