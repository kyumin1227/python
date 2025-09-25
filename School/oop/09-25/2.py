class A:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

obj = A()
print(obj.public)
print(obj._protected)
# print(obj.__private)

print(obj._A__private)