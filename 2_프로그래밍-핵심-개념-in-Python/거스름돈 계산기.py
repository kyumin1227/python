def calculate_change(payment, cost):
    change = payment - cost
    print(f"50000원 지폐: {int(change / 50000)}장")
    change %= 50000
    print(f"10000원 지폐: {int(change / 10000)}장")
    change %= 10000
    print(f"5000원 지폐: {int(change / 5000)}장")
    change %= 5000
    print(f"1000원 지폐: {int(change / 1000)}장")


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)