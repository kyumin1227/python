import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Event Logger")
running = True

def handle_keydown(event):
    print(f"Key pressed: {pygame.key.name(event.key)}")

def handle_mousedown(event):
    print(f"Mouse button {event.button} clicked at position ({event.pos})")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_keydown(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mousedown(event)

pygame.quit()