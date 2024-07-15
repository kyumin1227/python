import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Event Listener and Handler Example")
running = True

def handle_keydown(event):
    if event.key == pygame.K_SPACE:
        print("Spacebar pressed - handled by function.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed - handled by algorithm.")
                running = False
            else:
                handle_keydown(event)

pygame.quit()