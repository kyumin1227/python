def calculate_average(math_score, science_score, english_score):
    return (math_score + science_score + english_score) / 3

math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

average = calculate_average(math_score, science_score, english_score)

if average >= 90:
    print(f"평균 점수는 {average}점이고, 학점은 A입니다.")
elif average >= 80:
    print(f"평균 점수는 {average}점이고, 학점은 B입니다.")
elif average >= 70:
    print(f"평균 점수는 {average}점이고, 학점은 C입니다.")
elif average >= 60:
    print(f"평균 점수는 {average}점이고, 학점은 D입니다.")
else:
    print(f"평균 점수는 {average}점이고, 학점은 F입니다.")