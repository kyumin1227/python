import turtle
import threading

screen = turtle.Screen()

# def doingPaint()

t = turtle.Turtle()

t2 = turtle.Turtle()

t.speed(10)

t2.speed(10)

# t.forward(100)

# t.right(90)

# t.backward(200)

# t.left(270)

# t.penup()

# t.home()

# t.pendown()

# t.left(90)

# t.forward(100)

t2.right(45)

for _ in range(90):

    for _ in range(4):
        t.circle(50)
        t2.circle(100)

        t.right(90)
        t2.right(90)

    t.right(10)
    t2.right(10)