# bar = [2, 3, 4, 5]
# foo = (6, 7, 8, 9)

# print(bar[0])
# print(foo[0])

# bar[0] = 20
# foo[0] = 60

# kin = 20, 30, 40, 50    # 하나의 함수에 여러 값을 넣게 되면 자동으로 튜플로 묶임

# print(kin)

# bar = "hello"

# for char in bar:
#     print(char, end="")

# print()

# for char in (foo := "world"):
#     print(char, end="")


# def getCalcValues(argA, argB):
#     return (argA + argB, argA - argB, argA * argB, argA / argB)

# sum, substract, multiply, division = getCalcValues(2, 3)
# print(f"{sum}, {substract}, {multiply}, {division}")


# result = (x := 10) + (y := 20)

# print(result)

# def myInOperator(argValue, argSeqObj):
#     for value in argSeqObj:
#         if value == argValue:
#             return True

#     return False

# def myNotInOperator(argValue, argSeqObj):
#     for value in argSeqObj:
#         if value == argValue:
#             return False

#     return True

bar = [2, 3, 4]
foo = [2, 3, 4]

if bar == foo:
    print("참")
else:
    print("거짓")

if bar is foo:
    print("참")
else:
    print("거짓")

