myString = "It is a great weather with you"

# word = 1

# for c in myString:
#     if c == " ":
#         word += 1

word = 0    # 단어의 개수
word_len = 0    # 단어의 길이

if len(myString) > 0:
    for c in myString.upper():
        # A 〜　Z 사이인지 확인
        if ord(c) >= 65 and ord(c) <= 90:
            word_len += 1
        # 공백인 경우 단어의 길이가 0 이상인지 확인
        elif c == " " and word_len > 0:
            word += 1
            word_len = 0

# 공백으로 끝나지 않고 단어로 끝나는 경우 확인
if word_len > 0:
    word += 1

print("문자열 단어 개수 : ", word)