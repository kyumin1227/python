# dir : 어던 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())
print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

name = "kyumin"
print(dir(name))