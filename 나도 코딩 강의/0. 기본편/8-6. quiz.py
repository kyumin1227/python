for i in range(1, 51):
    with open(f"{i}주차.txt", "w", encoding="utf8") as report:
        report.write(f"- {i} 주차 주간보고 -\n")
        report.write("부서 : \n")
        report.write("이름 : \n")
        report.write("업무 요약 : ")
