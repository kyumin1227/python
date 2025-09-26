class A:
    def __init__(self):
        self.__age = 20

    def prt(self):
        print(self.__age)

obj = A()
obj.prt()
# print(obj.__age)
obj._A__age = 100
obj.prt()