from functools import singledispatch, singledispatchmethod

@singledispatch
def bar(x):
    # 지원하지 않는 자료형의 처리 로직
    raise TypeError("unsupported type")

@bar.register(float)
def _(x: float):
    print("float")

@bar.register(int)
def _(x: int):
    print("int")
