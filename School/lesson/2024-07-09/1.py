# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("example.txt", "w") as file:
#     file.write("Hello, Kyumin!\n")


# with open("example.txt", "a") as file:
#     file.write("Hello, World!\n")


# with open("example.txt", "r+") as file:
#     content = file.read()
#     print("Original Content: ", content)
#     file.seek(0)
#     file.write("Update Content")


# with open("example.txt", "w+") as file:
#     file.write("New Content")
#     file.seek(0)
#     print(file.read())


with open("example.txt", "a") as file:
    file.write("\nHello again!")