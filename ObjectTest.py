import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 450))
clock = pygame.time.Clock()

activeBox = None
boxes = []
for i in range(5):
    x = random.randint(50,700)
    y = random.randint(50,350)
    w = 50
    h = 50
    box = pygame.Rect(x, y, w, h)
    boxes.append(box)


running = True



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        activeBox = num

        if event.type == pygame.MOUSEMOTION:
            if activeBox != None:
                boxes[activeBox].move_ip(event.rel)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                activeBox = None


        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255, 255, 255))


    for box in boxes:
        pygame.draw.rect(screen, "blue", box)
        pygame.draw.rect(screen, "black", box, 2)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60

pygame.quit()