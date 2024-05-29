# color = input()

# car = ""

# if (color == "red"):
#     car = "ford"
# elif (color == "gray"):
#     car = "bentley"
# elif (color == "black" or color == "blue"):
#     car = "hyundai"
# # else:
# #     car = "bentley"

# print(car)

# model = input()

# list_bmw = ["M3", "M5", "M7"]
# list_tesla = ["Y", "X"]
# list_lexus = ["ES", "LS"]
# list_hyundai = ["G80", "G90"]

# maker = ""

# if (model in list_bmw):
#     maker = "BMW"
# elif (model in list_tesla):
#     maker = "Tesla"
# elif (model in list_lexus):
#     maker = "Lexus"
# elif (model in list_hyundai):
#     maker = "Hyundai"
# else:
#     maker = "알수 없는 모델입니다."

# print(maker)





# # IN 안쓰고
# def checkIn(args_value, args_list):
#     for i in args_list:
#         if args_value == i:
#             return True
#     return False

# model = input()

# list_bmw = ["M3", "M5", "M7"]
# list_tesla = ["Y", "X"]
# list_lexus = ["ES", "LS"]
# list_hyundai = ["G80", "G90"]

# maker = ""

# if checkIn(model, list_bmw):
#     maker = "BMW"
# elif checkIn(model, list_tesla):
#     maker = "Tesla"
# elif checkIn(model, list_lexus):
#     maker = "Lexus"
# elif checkIn(model, list_hyundai):
#     maker = "Hyundai"
# else:
#     maker = "알수 없는 모델입니다."

# print(maker)







# model = input()

# list_bmw = ["M3", "M5", "M7"]
# list_tesla = ["Y", "X"]
# list_lexus = ["ES", "LS"]
# list_hyundai = ["G80", "G90"]

# check_list = list_bmw + list_tesla + list_lexus + list_hyundai

# count = 0
# isExist = False
# for i in check_list:
#     if model == i:
#         isExist = True
#         break
#     else:
#         count += 1

# if count < len(list_bmw):
#     maker = "BMW"
# elif count < len(list_bmw) + len(list_tesla):
#     maker = "Tesla"
# elif count < len(list_bmw) + len(list_tesla) + len(list_lexus):
#     maker = "Lexus"
# elif count < len(list_bmw) + len(list_tesla) + len(list_lexus) + len(list_hyundai):
#     maker = "Hyundai"
# else:
#     maker = "알수 없는 모델입니다."

# print(maker)





# model = input()

# list_bmw = ["M3", "M5", "M7"]
# list_tesla = ["Y", "X"]
# list_lexus = ["ES", "LS"]
# list_hyundai = ["G80", "G90"]

# maker = ""

# for i in list_bmw:
#     if i == model:
#         maker = "BMW"
#         break

# if maker == "":
#     for i in list_tesla:
#         if i == model:
#             maker = "Tesla"
#             break

# if maker == "":
#     for i in list_lexus:
#         if i == model:
#             maker = "Lexus"
#             break

# if maker == "":
#     for i in list_hyundai:
#         if i == model:
#             maker = "Hyundai"
#             break

# if maker == "":
#     maker = "알수 없는 모델입니다."

# print(maker)






model = input()

list_bmw = ["M3", "M5", "M7"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_hyundai = ["G80", "G90"]

list_list = [list_bmw, list_tesla, list_lexus, list_hyundai]
list_maker = ["BMW", "Tesla", "Lexus", "Hyundai"]

maker = ""

count = 0
isNotExist = True
while count < len(list_maker) and isNotExist:
    for value in list_list[count]:
        if value == model:
            isNotExist = False
            maker = list_maker[count]
            break
    count += 1

if isNotExist:
    maker = "알수 없는 모델입니다."  

print(maker)