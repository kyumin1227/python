# bar = [10, 20, 30]

# foo = [100, 200, 300]

# bar = foo

# bar[0] = 1000

# print(foo[0], bar[0])


# bar = [10, 20, 30]

# foo = bar

# pos = foo

# pos[0] = 1000

# print(bar[0], foo[0], pos[0])


bar = [90, 10, 20]

def test(argValue):
    for index in range(0, len(argValue)):
        argValue[index] += 1

test(bar)

print(bar)