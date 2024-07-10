
f_handler_1 = open("test_1.txt", "w", encoding="utf-8")
f_handler_2 = open("test_2.txt", "w")
f_handler_3 = open("test_3.txt", "w")

f_handler_1.write("안녕하세요")
f_handler_2.write("Hello")
f_handler_3.write("Konnichiwa")

f_handler_1.close()
f_handler_2.close()
f_handler_3.close()