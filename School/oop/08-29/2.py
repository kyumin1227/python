class Foo:
    test = 10

    def __init__(self):
        self.test = 20

obj = Foo()
print(Foo.test)
print(obj.test)