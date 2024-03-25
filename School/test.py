# test = 123

# print(test)

# test = "123iufjaweklfnsjkdfcasd"

# print(test)

# arr = [i for i in range(10)]

# print(arr)

# my_list = [1, "Hello", 3.14, [1, 2, 3]]

# print(my_list.count(1))

# numbers = [1, 1, 1, 3, 2, 1, 6]

# numbers.reverse()

# numbers.sort()

# print(numbers)

# names = ["김규민", "박정민", "김근형", "나오", "권혁일"]

# names.sort()

# print(names)

# numbers = []

# n = int(input())

# for i in range(n):
# 	numbers.append(int(input()))

# names = ["김규민", "박정민", "김근형", "나오", "권혁일"]

# for name in names:

# print(name)

# n = int(input())

# num = 0

# count = 1

# while True:
#     num += n
#     count += 1
#     if count == 3:
#         break
    
# print(num)

# s = input()

# for i in s:
#     print(i)


# i = 0

# while i < 10:
# 	i += 1 
# 	if i == 5:
# 		continue
# 	print(i)
	
# import sys

# input = sys.stdin.readline

# s = input()

# s.rstrip()

# map(int, input().split())

# with open("test.txt", "r") as file:
#     print(file.read())


# numbers = []

# numbers.sort(reverse=True)

# numbers = []

# n = int(input())

# for i in range(n):
# 	# numbers.append(int(input()))
#     numbers[i] = int(input())

# print(numbers)

a = int(input())
list1 = list(map(int, input().split()))
x = int(input())
# count=0

# listaa = list(map(int,list1.split()))
# for i in listaa:
#     if i == x:
#     	count += 1
print(list1.count(x))