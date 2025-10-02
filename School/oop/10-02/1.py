def bar(a, b, *args):
    print(a, b, args)

bar(1, 2, 3, 4, 5, 6)

def foo(a, b, c):
    pass

# foo(1, 2)   # error

def pos(a, b, c = 20):
    pass

pos(1, 2)   # ok