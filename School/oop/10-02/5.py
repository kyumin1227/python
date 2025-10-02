from functools import singledispatch

@singledispatch
def prt(x):
    raise TypeError(f"unsupported type {type(x)}")

@prt.register(int)
def _(x: int) -> str:
    return f"int {x}"

@prt.register(float)
def _(x: float) -> str:
    return f"float {x}"

# 싱클 디스패치의 탐색 순서는 가장 마지막에 생성된 함수부터 찾음
print(prt(2.0))
print(prt(2))
print(prt("abc"))
