# 함수 선언
def convert_to_square_feet(square_meters):
    return square_meters * 10.7639

def convert_to_acres(square_meters):
    return square_meters / 4046.86

# 입력
square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))

# 출력
if square_meters < 0:
    print("잘못된 입력입니다.")
else:
    print(f"{square_meters} 제곱미터는 {convert_to_square_feet(square_meters)} 평방피트입니다.")
    print(f"{square_meters} 제곱미터는 {convert_to_acres(square_meters)} 에이커입니다.")