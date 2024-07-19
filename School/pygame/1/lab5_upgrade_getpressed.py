import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Event Logger")
running = True
clock = pygame.time.Clock()
fps = 60
speed = 500

now_x = int(screen.get_width() / 2)
now_y = int(screen.get_height() / 2)

def getColor():
    """색상을 랜덤으로 가져옴"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def draw_line(arg_x, arg_y):
    pygame.draw.line(screen, color, (now_x, now_y), (arg_x, arg_y), 5)

    pygame.display.flip()
    

color = getColor()

print(pygame.event.get())

while running:
    dt = clock.tick(fps) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    change_x = now_x
    change_y = now_y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        change_x -= speed * dt
    if keys[pygame.K_RIGHT]:
        change_x += speed * dt
    if keys[pygame.K_UP]:
        change_y -= speed * dt
    if keys[pygame.K_DOWN]:
        change_y += speed * dt

    if 0 <= change_x <= screen.get_width() and 0 <= change_y <= screen.get_height()\
        and (change_x != now_x or change_y != now_y):
        draw_line(change_x, change_y)
        now_x = change_x
        now_y = change_y

pygame.quit()
