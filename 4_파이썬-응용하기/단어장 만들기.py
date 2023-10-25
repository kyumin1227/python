with open("vocabulary.txt", "w", encoding="UTF-8") as f:
    while True:
        english = input("영어 단어를 입력하세요: ")
        if(english == "q"):
            break
        
        korea = input("한국어 뜻을 입력하세요: ")
        if(korea == "q"):
            break
        
        f.write(f"{english}: {korea}\n")