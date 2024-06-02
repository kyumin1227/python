sum_num = 0 # 합계

# 1부터 20까지 순회하는 for문
for i in range(1, 21):
    # 홀수인 경우에는 continue
    if (i % 2 == 1):
        continue
    sum_num += i

print("1부터 20까지의 짝수 합계 (홀수 건너뜀):", sum_num)