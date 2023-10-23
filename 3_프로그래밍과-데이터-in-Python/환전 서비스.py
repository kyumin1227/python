# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    count = 0
    while count < len(krw):
        krw[count] = round(krw[count] / 1000, 1)
        count += 1
    return krw


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    count = 0
    while count < len(usd):
        usd[count] = round(usd[count] / 8 * 1000, 1)
        count += 1
    return usd


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# prices를 원화(￦)에서 달러($)로 변환하기
# 여기에 코드를 작성하세요
prices = krw_to_usd(prices)

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
# 여기에 코드를 작성하세요
prices = usd_to_jpy(prices)

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))