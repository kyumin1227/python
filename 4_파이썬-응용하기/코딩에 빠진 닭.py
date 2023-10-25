sum = 0

with open("data/chicken.txt", "r", encoding="UTF-8") as f:
    for line in f:  # 자동으로 for문 돌리기 가능
        data = line.split("일: ")
        sum += int(data[1])
        day = int(data[0])
    print(sum / day)
    