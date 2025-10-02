from typing import Union

x: int = 3

def div(a: Union[int, float], b: Union[int, float]) -> float:
    return(a / b)

print(div(4, 2))
print(div(4.0, 2.0))
print(div("4", "2"))
