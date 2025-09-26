# / 앞의 모든 파라미터는 포지션 기반으로 입력
def calculate(x, y, /, op = "+"):
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    else:
        print("error")

calculate()

def prt(a, *arg):
    print(a, arg)

prt(1)
prt(1, 2)
prt(1, 2, 3)
