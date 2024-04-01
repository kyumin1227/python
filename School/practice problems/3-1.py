# 체크 함수 선언
def reservation_check(age, event_code, reservation_date):
    success = "예약이 완료되었습니다!"

    # 입력값이 잘못된 경우 확인
    if not reservation_date in [i for i in range(1, 31)] or not event_code in ["E1", "E2", "E3"]:
        return "잘못된 입력입니다. 프로그램을 종료합니다"
    
    # 이벤트 코드 확인
    if event_code == "E1":
        if age >= 18:
            return success
        else :
            return "나이 제한으로 인해 예약할 수 없습니다."
    elif event_code == "E2":
        if reservation_date % 2 == 0:
            return success
        else:
            return "선택하신 날짜에는 예약할 수 없습니다."
    elif event_code == "E3":
        if reservation_date % 7 == 0 and age >= 16:
            return success
        elif age < 16:
            return "나이 제한으로 인해 예약할 수 없습니다."
        else:
            return "선택하신 날짜에는 예약할 수 없습니다."

# 정보 입력
age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

print(reservation_check(age, event_code, reservation_date))