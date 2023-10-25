import pygame
import random
#from shapeFormat import shapeFormat

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

s_width = 800
s_height = 700
play_width = 300  # red border
play_height = 300  # meaning 600 // 10 = 30 height per block
block_size = 51

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

sx = 100
sy = 100
gridx = 6
gridy = 6

def createGridRect():
    pass


def create_grid(locked_pos={}):  
    grid = [[(0,0,0) for x in range(gridx)] for y in range(gridy)]

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
    createGridRect()

    activeBox = None
    shapeList = []

    x = 500
    y = 500
    box = pygame.Rect(x,y, 50, 50) #iterate through a list of positions with variables 
    shapeList.append(box) #for width and height to not repeat code
    box = pygame.Rect(x,y, 100, 50)
    shapeList.append(box)
    box = pygame.Rect(x, y, 150, 150)
    shapeList.append(box)
    box = pygame.Rect(x, y, 100, 100)
    shapeList.append(box)
    box = pygame.Rect(x, y, 200, 50)
    shapeList.append(box)
    box = pygame.Rect(x, y, 150, 50)
    shapeList.append(box)
    box = pygame.Rect(x, y, 50, 100)
    shapeList.append(box)
    box = pygame.Rect(x, y, 50, 150)
    shapeList.append(box)
    box = pygame.Rect(x, y, 50, 200)
    shapeList.append(box)

    blockerList = [] 
    blocker1 = pygame.Rect(151, 101, 50, 50) #Make these random from a list of spots that works
    blockerList.append(blocker1)
    blocker2 = pygame.Rect(203, 254, 50, 50)
    blockerList.append(blocker2)
    blocker3 = pygame.Rect(304, 101, 50, 50)
    blockerList.append(blocker3)
    blocker4 = pygame.Rect(355, 203, 50, 50)
    blockerList.append(blocker4)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, box in enumerate(shapeList):
                        if box.collidepoint(event.pos):
                            print("True")
                            activeBox = num

            if event.type == pygame.MOUSEMOTION:
                if activeBox != None:
                    shapeList[activeBox].move_ip(event.rel)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    activeBox = None


            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))

        gridRectList = []
        for x in range(100, 400, block_size):
            for y in range(100, 400, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                gridRectList.append(rect)

        for rect in gridRectList:
            pygame.draw.rect(screen, "Red", rect, 1)

        for blocker in blockerList:
            pygame.draw.rect(screen, "Pink", blocker)

        for box in shapeList:
            pygame.draw.rect(screen, "blue", box)
            pygame.draw.rect(screen, "black", box, 2)
        
        
        
        clock.tick(60)

        pygame.display.update()
        pygame.display.flip()

    # flip() the display to put your work on screen

pygame.display.update()
pygame.display.flip()
main(screen)


clock.tick(60)  # limits FPS to 60

pygame.quit()