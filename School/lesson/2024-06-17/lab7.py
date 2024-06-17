def contains(arg_list, arg_target):
    for num in arg_list:
        if num == arg_target:
            return True
    return False

print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))