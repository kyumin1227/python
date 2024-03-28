# 함수 선언
def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    result = 20

    # 결석 시간에 지각 수를 포함
    absence_hours += tardy_count // 3

    # F 미리 거르기    
    if hours_per_week * 15 / 4 < absence_hours:
        return -1
    
    result -= 20 * absence_hours / (hours_per_week * 15)

    return result
    
    
# 사용자 입력
hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

result = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)

# result가 -1이면 F 이므로 출력 변경
if result == -1:
    print("당신의 출석 점수는 F (학점 미부여)점입니다.")
else:
    print("당신의 출석 점수는 {:.2f}점입니다.".format(result))