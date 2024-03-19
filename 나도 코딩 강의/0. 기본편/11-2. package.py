# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import thailand
# trip_to = thailand.ThailandPackage()

# 패키지 파일 위치 확인 가능
import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))