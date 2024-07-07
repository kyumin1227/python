def showMenu(arg_len_data, arg_avg):
    """메뉴를 출력"""

    print("*" * 20)
    print("  1. 학생 성적 입력")
    print("  2. 학생 목록 출력(입력 순)")
    print("  3. 프로그램 종료")
    print(f"\n 현 입력데이터 갯수 : {arg_len_data}")
    print(f" 전체 학생 평균 값 : {arg_avg:.2f}")
    print("*" * 20)

def appendScore():
    """성적을 입력 후 합계를 반환"""

    score = []

    student_num = int(input("학번을 입력하세요\n"))
    name = input("이름을 입력하세요\n")
    korean_score = int(input("국어 성적을 입력하세요\n"))
    english_score = int(input("영어 성적을 입력하세요\n"))
    math_score = int(input("수학 성적을 입력하세요\n"))

    score.extend([student_num, name, korean_score, english_score, math_score])

    scores.append(score)

    return korean_score + english_score + math_score


def printScores():
    """학생 목록을 출력"""
    for score in scores:
        sum_num = score[2] + score[3] + score[4]
        print(f"[ id : {score[0]} name : {score[1]} kor : {score[2]} eng : {score[3]} math : {score[4]} sum : {sum_num} avg : {sum_num / 3:.1f}]")

def calSum(arg_sum, arg_len):
    if arg_sum == 0:
        return 0
    
    return arg_sum / (arg_len * 3)

scores = []
sum_num = 0

while True:
    showMenu(len(scores), calSum(sum_num, len(scores)))
    
    select = int(input())

    if select == 1:
        sum_num += appendScore()
    elif select == 2:
        printScores()
    elif select == 3:
        print("프로그램 종료")
        break