year = 1988
money = 50000000    
apart = 1100000000

while year < 2016:
    money += money * 0.12
    year += 1
    
print(f"{money - apart:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.")