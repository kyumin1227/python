# km를 입력 받음
inputKm = float(input("여행할 거리를 킬로미터(km) 단위로 입력하세요: "))

# 받은 km를 빛의 속도 (299792)로 나누어 시간을 구함
kmToSecond = inputKm / 299792

# 양식에 맞게 출력
print(f"빛이 {inputKm} 킬로미터를 여행하는데 걸리는 시간은 {kmToSecond} 초입니다.")