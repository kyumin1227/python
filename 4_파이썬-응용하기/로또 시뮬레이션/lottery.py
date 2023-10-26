from random import randint

def generate_numbers(n):
    num_array = []
    while True:
        if(len(num_array) == n):
            break
        num = randint(1, 45)
        if(not num in num_array):
            num_array.append(num)
    return num_array

def draw_winning_numbers():
    numbers = generate_numbers(6)
    numbers.sort()
    while True:
        num = randint(1, 45)
        if(not num in numbers):
            numbers.append(num)
            break
    return numbers

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for i in numbers:
        if(i in winning_numbers):
            count += 1
    return count

def check(numbers, winning_numbers: list):
    match_count = count_matching_numbers(numbers, winning_numbers[:6])
    if(match_count == 6):
        return 1000000000
    elif(match_count == 5):
        if(count_matching_numbers(numbers, winning_numbers) == 6):
            return 50000000
        else:
            return 1000000
    elif(match_count == 4):
        return 50000
    elif(match_count == 3):
        return 5000
    else:
        return 0
        
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))