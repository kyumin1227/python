englishs = []
koreas = []

with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    for line in f:
        data = line.split(": ")
        englishs.append(data[0])
        koreas.append(data[1])
        
for i in range(0, len(englishs)):
    answer = input(f"{koreas[i]}: ")
    if(answer == englishs[i]):
        print("맞았습니다!")
    else:
        print(f"아쉽습니다. 정답은 {englishs[i]}입니다.")