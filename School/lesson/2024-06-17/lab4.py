def max_or_three(arg_a, arg_b, arg_c):
    max_num = arg_a
    if max_num < arg_b:
        max_num = arg_b
    if max_num < arg_c:
        max_num = arg_c

    return max_num

print(max_or_three(10, 20, 15))