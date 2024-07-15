import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

screen.fill((255, 255, 255))
pygame.display.flip()

circle_count = random.randint(5, 20)

for i in range(circle_count):
    circle_x = random.randint(0, 800)
    circle_y = random.randint(0, 600)
    circle_size = random.randint(5, 100)
    
    circle_red = random.randint(0, 255)
    circle_green = random.randint(0, 255)
    circle_blue = random.randint(0, 255)

    pygame.draw.circle(screen, (circle_red, circle_green, circle_blue), (circle_x, circle_y), circle_size)

pygame.display.flip()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()