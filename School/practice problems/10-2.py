menus = ["피자", "파스타", "샐러드", "스시", "버거"]

index = int(input("메뉴의 인덱스를 선택하세요 (0부터 시작): "))

# 유효한 인덱스인지 확인
if index >= len(menus):
    print("유효하지 않은 선택입니다.")
else:
    print("선택된 메뉴:", menus[index])