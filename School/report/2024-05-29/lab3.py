myString = "hello hyundai hoho"

count = 0
# 문자열의 문자를 하나씩 순회하며 h와 같은지 확인
for c in myString:
    if c == "h":
        count += 1

print("문자열 내 h 개수 : ", count)