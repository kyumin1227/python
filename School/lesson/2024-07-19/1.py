import random

def get_matrix(*args):
    if len(args) == 1:
        return [[random.randint(1, 100) for _ in range(args[0])] for _ in range(args[0])]
    elif len(args) == 2:
        return [[random.randint(1, 100) for _ in range(args[0])] for _ in range(args[1])]
    print(args)

print(get_matrix())
print(get_matrix(4))
print(get_matrix(2, 3))
