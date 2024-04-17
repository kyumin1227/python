# import random

# bar = list()

# for _ in range(0, 5):
#     bar.append(random.randint(1, 100))

# print(bar)

# print(bar[-1])

# bar = [10, 20, 30, 40]

# foo = bar[0:1:1]
# foo = bar[0:2:1]
# foo = bar[0:3:1]
# foo = bar[0:4:1]

# print(bar[-1::-1])

bar = [7, 7, 0, 2, 2, 5, '-', 3, 9, 8, 3, 8, 1, 3]

birth = bar[:6]
back = bar[7:-1]
last = bar[-1]

print(birth)
print(back)
print(last)

print(bar[0::-1])