numbers = [0, 1, 2, 3]
print(numbers)  # [0, 1, 2, 3]
print(len(numbers))  # 3

numbers.append(4)
print(numbers)  # [0, 1, 2, 3, 4]

del numbers[2]
print(numbers)  # [0, 1, 3, 4]

numbers.insert(2, 2)
print(numbers)  # [0, 1, 2, 3, 4]

new_numbers = numbers[1:]   # 콜론의 앞을 비우면 0부터 뒤를 비우면 끝까지
print(new_numbers)  # [1, 2, 3, 4]

numbers = [2, 53, 31, 14, 67, 8, 19]
sorted_numbers = sorted(numbers)    # 오름차 정렬
print(sorted_numbers)   # [2, 8, 14, 19, 31, 53, 67]

sorted_numbers = sorted(numbers, reverse=True)  # 내림차 정렬
print(sorted_numbers)   # [67, 53, 31, 19, 14, 8, 2]

numbers.sort()  # 정렬된 배열을 반환하는 것이 아닌 배열 자체를 정렬 (위의 sorted는 정렬된 배열을 반환)
print(numbers)  # [2, 8, 14, 19, 31, 53, 67]