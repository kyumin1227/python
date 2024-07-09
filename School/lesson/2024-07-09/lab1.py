import os

def printMenu():
    """메뉴 출력"""
    print("[메뉴 선택]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 화면 출력")
    print("3. 학생 성적 파일 출력")
    print("4. 종료")

def inputGrade():
    """성적 입력 함수"""
    name = input("학생 이름: ")
    korean_score = int(input("국어 점수: "))
    english_score = int(input("영어 점수: "))
    math_score = int(input("수학 점수: "))

    grades.append({"name": name, "korean": korean_score, "english": english_score\
                   , "math": math_score})

def printGrades(arg_type):
    """성적 출력 (1 = 화면, 2 = 파일)"""
    result = "이름\t국어\t영어\t수학\t총점\t평균\t등수"

    # 등수를 구하기 위한 배열 생성
    rank = []
    for i in range(len(grades)):
        rank.append(grades[i]["korean"] + grades[i]["english"] + grades[i]["math"])
    rank.sort(reverse=True)

    for i in range(len(grades)):
        sum_score = grades[i]["korean"] + grades[i]["english"] + grades[i]["math"]
        result += f"\n{grades[i]["name"]}\t{grades[i]["korean"]}\t{grades[i]["english"]}\t{grades[i]["math"]}\t{sum_score}\t{sum_score / 3:.2f}\t{rank.index(sum_score) + 1}"

    # 선택한 형식에 따라 출력
    if arg_type == 1:
        print(result + "\n")

    elif arg_type == 2:
        file_name = input("파일 이름을 입력하세요: ")
        cwd = os.getcwd()
        print(cwd)
        with open(f"{cwd}/{file_name}.txt", "w") as file:
            file.write(result)

grades = []

while True:
    printMenu()
    select = int(input("메뉴를 선택하세요: "))
    print()

    if select == 1:
        inputGrade()
    elif select == 2:
        print("[학생 성적 목록]")
        printGrades(1)
    elif select == 3:
        printGrades(2)
    elif select == 4:
        break