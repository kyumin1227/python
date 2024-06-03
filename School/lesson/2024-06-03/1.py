for _ in range(10):
    print(1)


for _ in range(8):
    print(_, end="")

print("\n", "*" * 20, sep="")

for dan in range(2, 10):
    print(dan, end="")

print()

numbers = [num for num in range(1, 21)]

numbers = [7 for _ in range(100)]

bar = [value for value in range(1, 21) if value % 3 == 0]

print(bar)

foo = ["abc", "dcd", "ef", "gh"]

result1 = [value for value in foo if "c" in value]

print(result1)

result2 = [value for value in foo if len(value) >= 3]

print(result2)

numbers = [num * 20 if num % 2 == 0 else num * 10 for num in range(1, 11)]

print(numbers)

user_num = int(input())
while (user_num <= 0):
    user_num = int(input())

count = 1
while count <= 10:
    print(count)
    count += 1

bar = ["hello", "world", "Richard"]
found_word = False

for word in bar:
    if word == "word":
        print("단어를 찾았음")
        found_word = True
        break

if not found_word:
    print("단어를 찾지 못했음.")

for word in bar:
    if word == "world":
        print("단어를 찾았음")
        break
# 정상적으로 반복이 종료되면 실행
else:
    print("단어를 찾지 못했음")