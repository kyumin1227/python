import os

msg = os.getcwd()
print(type(msg), msg)

msg = os.listdir()
print(type(msg), msg)

os.mkdir("kin")

os.chdir("kin")

msg = os.getcwd()
print(type(msg), msg)