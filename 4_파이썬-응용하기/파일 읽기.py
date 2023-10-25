with open('data/chicken.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        print(line.strip()) # 각 줄의 시작과 끝의 \n \t 뛰어쓰기 같은 개행문자를 제거