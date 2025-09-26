class A:
    def __init__(self):
        self.__age = None

    # getter
    @property
    def age(self):
        return f"나이는 : {self.age}"

    # setter
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("음수 값 오류")
        self.__age = age

obj = A()
obj.age = 100
print(obj.age)
