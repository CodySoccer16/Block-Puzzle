import pygame
from tkinter import * 
from tkinter import messagebox 
import time
  


# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

s_width = 800
s_height = 700
play_width = 300  # red border
play_height = 300  # red border
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

#This creates each shape and appends them to a shape list
box = pygame.Rect(x,y, 50, 50) #1x1
shapeList.append(box) 
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


#These make all of the set blockers and append them to a blocker list
blockerList = [] 
blocker1 = pygame.Rect(150, 100, 50, 50) 
blockerList.append(blocker1)
blocker2 = pygame.Rect(200, 250, 50, 50)
blockerList.append(blocker2)
blocker3 = pygame.Rect(300, 100, 50, 50)
blockerList.append(blocker3)
blocker4 = pygame.Rect(350, 200, 50, 50)
blockerList.append(blocker4)

#This is the title amd instructions
my_font = pygame.font.SysFont('Comic Sans MS', 30)
my_font2 = pygame.font.SysFont('Comic Sans MS', 15)
winfont = pygame.font.SysFont('Comic Sans MS', 50)
displayText = my_font.render("Block Puzzle", False, "White")
instrucText = my_font2.render("Drag the blocks to complete the puzzle", False, "White")

#creates the grid
gridRectList = []
for x in range(100, 400, block_size):
    for y in range(100, 400, block_size):
        rect = pygame.Rect(x, y, block_size, block_size)
        gridRectList.append(rect)

#This checks if the player has won
def winCheck():
    winner = 0
    winNum = []
    for blocker in blockerList:
        for box in shapeList:
            for num, rect in enumerate(gridRectList):
                if rect.colliderect(blocker) or rect.colliderect(box):
                    winNum.append(num)
    for x in range(36):
        if x in winNum:
            winner += 1

    if winner == 36:
        time.sleep(0.5)
        messagebox.showinfo("Winner!", "You Won!")


def main(screen):
    global activeBox, shapeList, blockerList, gridRectList

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #Left mouse button clicked
                    for num, box in enumerate(shapeList): 
                        if box.collidepoint(event.pos): #checks if the mouse is on a box
                            activeBox = num #sets the active box to the box that the mouse is on
                            activeBoxTopLeft = box.topleft #Gets the orignal position of the box

            if event.type == pygame.MOUSEMOTION:
                if activeBox != None:
                    shapeList[activeBox].move_ip(event.rel) #Moves the box with the mouse

            if event.type == pygame.MOUSEBUTTONUP:
                if activeBox != None:
                    for rect in gridRectList:
                        if rect.collidepoint(event.pos):
                            shapeList[activeBox].topleft = rect.topleft #Snaps the box to the grid 
                            for blocker in blockerList:
                                if shapeList[activeBox].contains(blocker):
                                    shapeList[activeBox].topleft = activeBoxTopLeft #If the box is on a blocker, it goes back to the original position
                            for box in shapeList:
                                if box != shapeList[activeBox]:
                                    if shapeList[activeBox].colliderect(box): #If the box is on another box, it goes back to the original position
                                        shapeList[activeBox].topleft = activeBoxTopLeft
                winCheck() #Calls wincheck after every box is placed
                if event.button == 1:
                    activeBox = None #Resets the active box to none if the button is released
                

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        
        screen.fill((0,0,0)) #Fill screen with black

        #Draws the grid
        for rect in gridRectList: 
            pygame.draw.rect(screen, "Black", rect)
            pygame.draw.rect(screen, "Grey", rect, 1)

        #Draws the blockers
        for blocker in blockerList:
            pygame.draw.rect(screen, "Grey", blocker)

        #list of shape colors
        shape_colors = [(21, 71, 52), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128), (200,0,40), (150,60,80)]

        #Draws the shapes
        for box in shapeList:
            pygame.draw.rect(screen, shape_colors[shapeList.index(box)] , box)

        #Displays the title and instructions
        screen.blit(displayText, (165, 10))
        screen.blit(instrucText, (115, 50))

        #Updates the screen
        pygame.display.update()
        pygame.display.flip()


pygame.display.update()
pygame.display.flip()

main(screen)


clock.tick(60)  # limits FPS to 60

pygame.quit()