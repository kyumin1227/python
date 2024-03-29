# 변수 입력 받기
seed_money = int(input("초기 자본금을 입력하세요: "))
stock_price_buy = int(input("주식 가격을 입력하세요: "))
stock_count = int(input("구매할 주식 수를 입력하세요: "))
stock_price_sell = int(input("판매할 때의 주식 가격을 입력하세요: "))

# 남은 자본금
remain_money = seed_money - stock_price_buy * stock_count

# 만약 자본금이 부족하면 거르기
if remain_money < 0:
    print("자본금이 부족합니다.")
else:
    profit = stock_price_sell * stock_count - stock_price_buy * stock_count

    print(f"구매 후 남은 자본금: {float(remain_money):.2f}")
    print(f"예상 이익: {float(profit):.2f}")

    # 이익과 손실에 따라 다르게 출력
    if profit > 0 :
        print("예상되는 이익입니다.")
    elif profit < 0:
        print("예상되는 손실입니다.")