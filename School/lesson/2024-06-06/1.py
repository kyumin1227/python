# for value in range(3):
    
#     input_value = int(input("Enter a number: "))

#     if input_value <= 0:
#         break

#     print(value)

# # break 미사용으로 반복문이 종료 되었을 때
# else:
#     print("break 미사용")

for _ in range(4):
    for _ in range(3):
        print("*", end="")
    print()
