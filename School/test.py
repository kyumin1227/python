# # test = 123

# # print(test)

# # test = "123iufjaweklfnsjkdfcasd"

# # print(test)

# # arr = [i for i in range(10)]

# # print(arr)

# # my_list = [1, "Hello", 3.14, [1, 2, 3]]

# # print(my_list.count(1))

# # numbers = [1, 1, 1, 3, 2, 1, 6]

# # numbers.reverse()

# # numbers.sort()

# # print(numbers)

# # names = ["김규민", "박정민", "김근형", "나오", "권혁일"]

# # names.sort()

# # print(names)

# # numbers = []

# # n = int(input())

# # for i in range(n):
# # 	numbers.append(int(input()))

# # names = ["김규민", "박정민", "김근형", "나오", "권혁일"]

# # for name in names:

# # print(name)

# # n = int(input())

# # num = 0

# # count = 1

# # while True:
# #     num += n
# #     count += 1
# #     if count == 3:
# #         break
    
# # print(num)

# # s = input()

# # for i in s:
# #     print(i)


# # i = 0

# # while i < 10:
# # 	i += 1 
# # 	if i == 5:
# # 		continue
# # 	print(i)
	
# # import sys

# # input = sys.stdin.readline

# # s = input()

# # s.rstrip()

# # map(int, input().split())

# # with open("test.txt", "r") as file:
# #     print(file.read())


# # numbers = []

# # numbers.sort(reverse=True)

# # numbers = []

# # n = int(input())

# # for i in range(n):
# # 	# numbers.append(int(input()))
# #     numbers[i] = int(input())

# # print(numbers)

# # a = int(input())
# # list1 = list(map(int, input().split()))
# # x = int(input())
# # # count=0

# # # listaa = list(map(int,list1.split()))
# # # for i in listaa:
# # #     if i == x:
# # #     	count += 1
# # print(list1.count(x))

# # print(chr(65))
# # print(ord('A'))

# # s = "hello world"
# # print(s.count('l'))  # 'l'의 개수
# # print(s.find("world"))  # 'world'의 시작 인덱스
# # print(s.split())  # 공백을 기준으로 문자열 분리
# # print(len(s)) # 11
# # print(s.replace("world", "kyumin"))

# number = 0

# while number < 10:
#     print(number)
#     if number == 5:
#         continue
#     number += 1

# 정수 3개를 입력 받아서 제일 큰 값을 출력하시요?

number1 = int(input("1番目の整数を入力してください："))
number2 = int(input("2番目の整数を入力してください："))
number3 = int(input("3番目の整数を入力してください："))

print(max(number1,number2,number3))

if (number1 >= number2 and number1 >= number3):
    print(number1)
elif (number2 >= number1 and number2 >= number3):
    print(number2)
elif (number3 >= number1 and number3 >= number2):
    print(number3)