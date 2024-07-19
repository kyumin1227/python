import pygame
import random
import threading

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Event Logger")
running = True
clock = pygame.time.Clock()

now_x = int(screen.get_width() / 2)
now_y = int(screen.get_height() / 2)

def draw_line():
    global now_x
    global now_y
    # print("call function", clicked, now_x, now_y)
    if running:
        threading.Timer(0.05, draw_line).start()
    if True in clicked:
        x = [10, -10, 0, 0]
        y = [0, 0, 10, -10]

        change_x = now_x
        change_y = now_y

        for i in range(4):
            if clicked[i] == True:
                change_x += x[i]
                change_y += y[i]

        # 화면 밖으로 나가는 경우 실행 시키지 않음
        if not (0 <= change_x <= screen.get_width() and 0 <= change_y <= screen.get_height()):
            return

        pygame.draw.line(screen, color, (now_x, now_y), (change_x, change_y), 5)

        now_x = change_x
        now_y = change_y

        pygame.display.flip()

    return

def getColor():
    """색상을 랜덤으로 가져옴"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
    

color = getColor()

print(pygame.event.get())

clicked = [False, False, False, False]

draw_line()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if 79 <= event.scancode <= 82:
                clicked[event.scancode - 79] = True
        elif event.type == pygame.KEYUP:
            if 79 <= event.scancode <= 82 and True in clicked:
                if clicked[event.scancode - 79] == True:
                    clicked[event.scancode - 79] = False
    
    clock.tick(30)

pygame.quit()