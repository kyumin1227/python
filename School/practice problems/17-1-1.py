import random

def upOrDown(arg_float):
    num_int = int(arg_float)
    return num_int + 1 if arg_float > num_int else num_int

word_list = []
for n in ["첫", "두", "세"]:
    word = input(f"{n} 번째 단어를 입력 하세요\n")
    while not (len(word) >= 3 and len(word) <= 20):
        word = input("3이상 20이하 글자로 구성된 단어를 입력 하세요\n")
    word_list.append(word)

select_num = random.randint(0, len(word_list) - 1)
word_selected = list(word_list[select_num])

print(f"\n단어 선택 완료 게임을 시작합니다. 선택된 단어: {"".join(word_selected)}\n")

blind_index = set()
blind_num = upOrDown(len(word_selected) / 2)

while len(blind_index) < blind_num:
    blind_index.add(random.randint(0, len(word_selected) - 1))

for i in blind_index:
    word_selected[i] = "_"

count = 0

while len(blind_index) != 0:
    count += 1
    alpha = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{''.join(word_selected)}\n\n")
    print()
    isExist = 0
    for i in blind_index.copy():
        if alpha == word_list[select_num][i]:
            isExist += 1
            word_selected[i] = word_list[select_num][i]
            blind_index.remove(i)
    print(f"입력한 알파벳 단어 내 포함: {isExist}글자") if isExist > 0 else print("단어 내 포함되지 않은 알파벳입니다.")
    
print(f"Clear - 선택된 단어: {word_list[select_num]}. 총 시도 횟수: {count}")