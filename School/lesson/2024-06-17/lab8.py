def calculate_average(*arg_list):
    sum_num = 0
    for num in arg_list:
        sum_num += num
    
    return f"{(sum_num / len(arg_list)):.1f}"

print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))