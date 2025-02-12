try:
    num = input("1 또는 2를 입력 하세요")

    result = int(num)

    raise KeyboardInterrupt

    raise IndexError

    raise KeyError

    print("pos")

    print(1/0)

    print("bar")

    kin()

    raise IndexError

# except :
#     print("Error")
except Exception:
    print("Error")
# except LookupError:
#     print("LookupError 예외 발생")
# except ValueError:
#     print("ValueError 예외 발생")
# except IndexError:
#     print("IndexError 예외 발생")
# except NameError:
#     print("NameError 예외 발생")
# except ZeroDivisionError:
#     print("ZeroDivisionError 예외 발생")

print("Final")
