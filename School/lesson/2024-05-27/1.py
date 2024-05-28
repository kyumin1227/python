import random
import turtle

screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width()
height = screen.window_height()

print(width, "*", height)

t = turtle.Turtle()

def move_forward():
    t.forward(10)

    x, y = t.position()
    print(x, y)

    check_end()

def move_backward():
    t.backward(10)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))

def change_color_to_black():
    t.pencolor("black")

def change_color_to_red():
    t.pencolor("red")

def redToBlackOrBlackToRed():
    penColor = t.pencolor()

    if penColor == "red":
        change_color_to_black()
    elif penColor == "black":
        change_color_to_red()

def change_color():
    # print("색깔 선택: ")
    # print("1. 파란색")
    # print("2. 검정색")
    # print("3. 노란색")

    # input_value = int(input("숫자 입력: "))

    # while not (input_value >= 1 and input_value <= 3):
    #     print("색깔 선택: ")
    #     print("1. 파란색")
    #     print("2. 검정색")
    #     print("3. 노란색")
    #     input_value = int(input("숫자 입력: "))

    # while True:
    #     print("색깔 선택: ")
    #     print("1. 파란색")
    #     print("2. 검정색")
    #     print("3. 노란색")

    #     input_value = int(input("숫자 입력: "))

    #     if input_value >= 1 and input_value <= 3:
    #         break

    while not (1 <= input_value <= 3):
        input_value = int(input("숫자 입력: "))

    if input_value == 1:
        t.pencolor("blue")
    elif input_value == 2:
        t.pencolor("black")
    else:
        t.pencolor("yellow")

def check_end():
    x, y = t.position()

    if x >= width / 2 or x <= -width / 2 or y >= height / 2 or y <= -height / 2:
        t.left(180)
        


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_random, "c")
screen.onkey(change_color_to_black, "b")
screen.onkey(change_color_to_red, "r")
screen.onkey(redToBlackOrBlackToRed, "i")
screen.onkey(change_color, "t")

screen.mainloop()