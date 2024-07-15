import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Event Logger")
running = True

def handle_mousedown(event):
    pygame.draw.circle(screen, getColor(), event.pos, 10) 
    pygame.display.flip()

def getColor():
    """색상을 랜덤으로 가져옴"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mousedown(event)

pygame.quit()