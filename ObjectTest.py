import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

s_width = 800
s_height = 700
play_width = 500  # meaning 300 // 10 = 30 width per block
play_height = 500  # meaning 600 // 10 = 30 height per block
block_size = 50

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

sx = 150
sy = 100


def create_grid(locked_pos={}):  
    grid = [[(0,0,0) for x in range(10)] for y in range(10)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def draw_grid(surface, grid):
    
    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))

def draw_window(surface, grid):
    
    surface.fill((0, 0, 0))

    pygame.font.init()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (sx, sy, play_width, play_height), 5)

    draw_grid(surface, grid)



def main(screen):
    locked_positions = {}
    grid = create_grid(locked_positions)

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
        grid = create_grid(locked_positions)
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
                pygame.quit()

        screen.fill((255, 255, 255))
        draw_window(screen, create_grid(locked_positions))
        for box in boxes:
            pygame.draw.rect(screen, "blue", box)
            pygame.draw.rect(screen, "black", box, 2)

        
        
        clock.tick(60)

        pygame.display.update()
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE
    

    # flip() the display to put your work on screen

pygame.display.update()
pygame.display.flip()
main(screen)


clock.tick(60)  # limits FPS to 60

pygame.quit()