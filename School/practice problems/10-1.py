books = []

while True:
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ")
    # 입력값이 "종료"면 반복문 종료
    if title == "종료":
        break
    # 리스트에 책 추가
    books.append(title)
    
print("도서 목록:", books)