import pygame
import random
#from shapeFormat import shapeFormat

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

s_width = 800
s_height = 700
play_width = 300  # red border
play_height = 300  # meaning 600 // 10 = 30 height per block
block_size = 50

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

sx = 100
sy = 100
gridx = 6
gridy = 6


S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]


shapes = [S, Z]
shape_colors = [(0, 255, 0), (255, 0, 0)]
# index 0 - 6 represent shape


class Piece(object):  # *
    def __init__(self, x, y, shape):
        self.rect = pygame.Rect(x, y, block_size, block_size)
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def get_shape():
    S = Piece(5, 0, shapes[0])
    Z = Piece(5, 0, shapes[1])
    return [S, Z]

def draw_shapes(surface, shape):
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                shapeRect = pygame.Rect(sx + j*block_size, sy + i*block_size, block_size, block_size)
                pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)
    return shapeRect

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

    activeBox = None
    shapeList = []
    
    """
    for i in range(5):
        x = random.randint(50,700)
        y = random.randint(50,350)
        w = 50
        h = 50
        box = pygame.Rect(x, y, w, h)"""
    
    shape = Piece(50, 50, shapes[0])
    shapeList.append(shape)
    
    """
    shape = Piece(5, 0, shapes[1])
    shapeList.append(shape)
"""
        


    running = True
    while running:
        grid = create_grid(locked_positions)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, shape in enumerate(shapeList):
                        if shape.rect.collidepoint(event.pos): # This is where the error is, it never turns true
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

        screen.fill((255, 255, 255))
        draw_window(screen, create_grid(locked_positions))
        """
        for box in shapeList:
            pygame.draw.rect(screen, "blue", box)
            pygame.draw.rect(screen, "black", box, 2)
            """
        for shape in shapeList:
            draw_shapes(screen, shape)
       

        
        
        clock.tick(60)

        pygame.display.update()
        pygame.display.flip()

    # flip() the display to put your work on screen

pygame.display.update()
pygame.display.flip()
main(screen)


clock.tick(60)  # limits FPS to 60

pygame.quit()