import csv

# newline="" 옵션을 통해 파일에서 읽을 때 발생할 수 있는 불필요한 줄바꿈을 방지
with open("grade.csv", "r", newline="", encoding="utf-8") as f_handler:
    reader = csv.reader(f_handler)

    header = next(reader)

    for item in header:
        print(item, end="\t")
    
    print()

    for row in reader:
        for item in row:
            print(item, end="\t")
        print()