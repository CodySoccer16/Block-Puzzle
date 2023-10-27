import pygame
from tkinter import * 
from tkinter import messagebox 
  


# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((700, 700))
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

activeBox = None
shapeList = []
x = 450
y = 100

box = pygame.Rect(x,y, 50, 50) #1x1 - iterate through a list of positions with variables 
shapeList.append(box) #for width and height to not repeat code

box = pygame.Rect(x, y + 75, 100, 50) #2x1
shapeList.append(box)
box = pygame.Rect(x, y + 300, 150, 150) #3x3
shapeList.append(box)
box = pygame.Rect(x - 125, y + 350, 100, 100) #2x2
shapeList.append(box)
box = pygame.Rect(x, y + 225, 200, 50) #4x1
shapeList.append(box)
box = pygame.Rect(x, y + 150, 150, 50) #3x1
shapeList.append(box)
box = pygame.Rect(x - 200, y + 350, 50, 100) #1x2
shapeList.append(box)
box = pygame.Rect(x - 275, y + 350, 50, 150) #1x3
shapeList.append(box)
box = pygame.Rect(x - 350, y+ 350, 50, 200) #1x4
shapeList.append(box)

blockerList = [] 
blocker1 = pygame.Rect(150, 100, 50, 50) #Make these random from a list of spots that works
blockerList.append(blocker1)
blocker2 = pygame.Rect(200, 250, 50, 50)
blockerList.append(blocker2)
blocker3 = pygame.Rect(300, 100, 50, 50)
blockerList.append(blocker3)
blocker4 = pygame.Rect(350, 200, 50, 50)
blockerList.append(blocker4)


my_font = pygame.font.SysFont('Comic Sans MS', 30)
my_font2 = pygame.font.SysFont('Comic Sans MS', 15)
winfont = pygame.font.SysFont('Comic Sans MS', 50)
displayText = my_font.render("Block Puzzle", False, "White")
instrucText = my_font2.render("Drag the blocks to complete the puzzle", False, "White")


gridRectList = []
for x in range(100, 400, block_size):
    for y in range(100, 400, block_size):
        rect = pygame.Rect(x, y, block_size, block_size)
        gridRectList.append(rect)

def winCheck():
    winner = 0
    winNum = []
    for blocker in blockerList:
        for box in shapeList:
            for num, rect in enumerate(gridRectList):
                if rect.colliderect(blocker) or rect.colliderect(box): #needs to test each one not just the first one
                    winNum.append(num)
    for x in range(36):
        if x in winNum:
            winner += 1

    if winner == 36:
        messagebox.showinfo("Winner!", "You Won!")


def main(screen):
    global activeBox, shapeList, blockerList, gridRectList

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for num, box in enumerate(shapeList):
                        if box.collidepoint(event.pos):
                            activeBox = num
                            activeBoxTopLeft = box.topleft

            if event.type == pygame.MOUSEMOTION:
                if activeBox != None:
                    shapeList[activeBox].move_ip(event.rel)

            if event.type == pygame.MOUSEBUTTONUP:
                if activeBox != None:
                    for rect in gridRectList:
                        if rect.collidepoint(event.pos):
                            shapeList[activeBox].topleft = rect.topleft
                            for blocker in blockerList:
                                if shapeList[activeBox].contains(blocker):
                                    shapeList[activeBox].topleft = activeBoxTopLeft
                            for box in shapeList:
                                if box != shapeList[activeBox]:
                                    if shapeList[activeBox].colliderect(box):
                                        shapeList[activeBox].topleft = activeBoxTopLeft
                winCheck()
                if event.button == 1:
                    activeBox = None


            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.fill((0,0,0))


        for rect in gridRectList:
            pygame.draw.rect(screen, "Black", rect)
            pygame.draw.rect(screen, "Grey", rect, 1)

        for blocker in blockerList:
            pygame.draw.rect(screen, "Grey", blocker)

        shape_colors = [(21, 71, 52), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128), (200,0,40), (150,60,80)]

        for box in shapeList:
            pygame.draw.rect(screen, shape_colors[shapeList.index(box)] , box)

        
        screen.blit(displayText, (165, 10))
        screen.blit(instrucText, (115, 50))

        clock.tick(60)

        pygame.display.update()
        pygame.display.flip()


pygame.display.update()
pygame.display.flip()

main(screen)


clock.tick(60)  # limits FPS to 60

pygame.quit()