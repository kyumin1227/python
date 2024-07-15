import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

print(screen.get_width(), screen.get_height())

center_x = int(screen.get_width() / 2)
center_y = int(screen.get_height() / 2)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.draw.circle(screen, RED, (center_x, center_y), 40)
pygame.draw.circle(screen, GREEN, (0, 0), 40)
pygame.draw.circle(screen, BLUE, (799, 599), 40)
pygame.display.flip()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()