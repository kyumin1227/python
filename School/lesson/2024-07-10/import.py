# # import 시 모듈 검색 순서

# import sys

# print(type(sys.path))

# for path in sys.path:
#     print(path)


# 동적 모듈 검색 경로 추가
import sys
import os

print("Current sys.path:")
for path in sys.path:
    print(path)

# sys.path.pop()

# my_module = os.getcwd() + "/sub_module"
# sys.path.append(my_module)

print("\nUpdated sys.path:")
for path in sys.path:
    print(path)
