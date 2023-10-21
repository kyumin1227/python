count = 0
num = 1

while num <= 120:
    if(120 % num == 0):
        print(num)
        count += 1
    num += 1

print(f"120의 약수는 총 {count}개입니다.")