template = float(input("현재 온도(섭씨)를 입력하세요: "))
exercise = ""

if template >= 30:
    exercise = "수영"
elif template >= 20:
    exercise = "등산"
elif template >= 10:
    exercise = "자전거 타기"
else:
    exercise = "스키"

print("현재 온도: " + str(template) + "도")
print("추천 활동:", exercise)