import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Event Logger")
running = True

now_x = 0
now_y = 0

def draw_line(event_scancode):
    code = (79, 80, 81, 82)
    x = [10, -10, 0, 0]
    y = [0, 0, 10, -10]

    index = code.index(event_scancode)
    pygame.draw.line(screen, color, (now_x, now_y), (change_x := now_x + x[index], change_y := now_y + y[index]))

    return change_x, change_y

def getColor():
    """색상을 랜덤으로 가져옴"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
    

color = getColor()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if 79 <= event.scancode <= 82:
                now_x, now_y = draw_line(event.scancode)
                pygame.display.flip()

pygame.quit()