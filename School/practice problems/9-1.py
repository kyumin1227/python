# 입력
departure_hour = int(input("출발 시 (시간)을 입력하세요: "))
departure_minute = int(input("출발 시 (분)을 입려하세요: "))
arrival_hour = int(input("도착 시 (시간)을 입력하세요: "))
arrival_minute = int(input("도착 시 (분)을 입력하세요: "))
distance = int(input("이동 거리(km)를 입력하세요: "))

# 평균 속도 계산
hour = (arrival_hour - departure_hour) + (arrival_minute - departure_minute) / 60
result = round(distance / hour, 2)

# 출력
print(f"이동 거리: {distance}km")
print(f"출발 시간: {departure_hour}시 {departure_minute}분")
print(f"도착 시간: {arrival_hour}시 {arrival_minute}분")
print(f"평균 속도: {result:.2f}km/h")

# 속도 상태
speed_status = ""
if result >= 90:
    speed_status = "빠름"
elif result >= 60:
    speed_status = "보통"
else:
    speed_status = "느림"
print(f"속도 상태: {speed_status}")