for i in range(1, 400):
    for j in range(i + 1, 400):
        for z in range(j + 1, 400):
            if(i ** 2 + j ** 2 == z ** 2 and i + j + z == 400):
                print(i * j * z)
                break