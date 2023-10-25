import random

vocabulary = {}
keys = []

with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    for line in f:
        data = line.split(": ")
        vocabulary[data[1]] = data[0]
        keys.append(data[1])

while True:
    key = keys[random.randint(0, len(keys) - 1)]
    
    answer = input(f"{key}: ")
    
    if(answer == "q"):
        break
    elif(answer == vocabulary.get(key)):
        print("맞았습니다!")
    else:
        print(f"틀렸습니다. 정답은 {vocabulary.get(key)}입니다.")
    