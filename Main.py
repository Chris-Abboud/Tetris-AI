#%%
import pygame
import copy
import numpy as np
from pygame import mixer
from Helper import *
from Shapes import *
from Grid import *
import random
import time

pygame.init() # Initialize Pygame modules
Outlines = Grid() # Generates Grid Outlines
Grid = [[0]*10 for pos in range(20)] # Generates Grid 10x20
GameOver = False

screen = pygame.display.set_mode((401, 870))

pygame.display.set_caption("Tetris - Developed by Christopher Abboud")
icon = pygame.image.load('Assets\TetrisIcon.png')
pygame.display.set_icon(icon)

FPS = 144
clock = pygame.time.Clock()
status = "Ready"
running = True

timer = time.time()
levelTime = time.time()

Level = 1

AllShapes = []

#Background Music
mixer.music.load('Assets\Tetris Main Theme.mp3')
mixer.music.play(-1)#Loop
level = 1

# Score
font = pygame.font.Font('freesansbold.ttf', 32)
Score = 0
textX = 10
textY = 820


ShapeNumber = -1

while running:
    clock.tick(FPS)

    if abs(levelTime - time.time()) > 10 and level <= 13:
        level+=1
        levelTime = time.time()

    screen.fill((0,0,0)) #RGB - Anything you want to be persistant in game must be in this loop
    
    # Shape Picker Formula
    if status == "Ready":
        Score+=3
        status = "Waiting"

        for i in range(len(Grid)): ##Checks for Tetris
            count = 0
            if canRemove(Grid[i]):
                count+=1
                Grid = DeleteRow(Grid, i)
                if count == 1:
                    TetrisSound =  pygame.mixer.Sound('Assets\TetrisSound.wav')
                Score+=30
                TetrisSound.play()

        shapePicker = random.randint(0,6) # Choosen Random
        dataTypes = [Square(), LongPiece(), TeePiece(), LeftEl(), RightEl(), ZigZagRight(), ZigZagLeft()]
        Chosen = dataTypes[shapePicker]
        AllShapes.append(Chosen)

        ShapeNumber+=1
        oldCords = AllShapes[ShapeNumber].cordinates

        if not canMoveDown(Grid, FindBottomCords(AllShapes[ShapeNumber].cordinates)):
            GameOver = True

        Grid = fillWithNum(Grid, AllShapes[ShapeNumber].cordinates, AllShapes[ShapeNumber].number)

    #Automatic Move Down
    if abs(timer - time.time()) > .78 - (level - 1) * .05 and canMoveDown(Grid, FindBottomCords(AllShapes[ShapeNumber].cordinates)):
        oldCords = AllShapes[ShapeNumber].cordinates
        Grid = fillWithNum(Grid, oldCords, 0)
        AllShapes[ShapeNumber].moveDown()
        Grid = fillWithNum(Grid, AllShapes[ShapeNumber].cordinates, AllShapes[ShapeNumber].number)
        timer = time.time()
        StagTimer = time.time()
    
    if canMoveDown(Grid, FindBottomCords(AllShapes[ShapeNumber].cordinates)) == False:
        if time.time() - StagTimer > .5:
            status = "Ready"

    #If Close button is pressed
    for event in pygame.event.get(): #Loops in all events
        if event.type == pygame.QUIT: #Close event
            running = False 

        
        if event.type == pygame.KEYDOWN:
            #LEFT MOVEMENT
            if event.key == pygame.K_DOWN and canMoveDown(Grid, FindBottomCords(AllShapes[ShapeNumber].cordinates)):
                oldCords = AllShapes[ShapeNumber].cordinates
                Grid = fillWithNum(Grid, oldCords, 0)
                AllShapes[ShapeNumber].moveDown()
                timer = time.time()
                StagTimer = time.time()

            #RIGHT MOVEMENT
            if event.key == pygame.K_RIGHT and canMoveRight(Grid, FindRightCords(AllShapes[ShapeNumber].cordinates)):
                oldCords = AllShapes[ShapeNumber].cordinates
                Grid = fillWithNum(Grid, oldCords, 0)
                AllShapes[ShapeNumber].moveRight()
                if canMoveDown(Grid, FindBottomCords(AllShapes[ShapeNumber].cordinates)):
                    StagTimer = time.time()

            #LEFT MOVEMENT
            if event.key == pygame.K_LEFT and canMoveLeft(Grid, FindLeftCords(AllShapes[ShapeNumber].cordinates)):
                oldCords = AllShapes[ShapeNumber].cordinates
                Grid = fillWithNum(Grid, oldCords, 0)
                AllShapes[ShapeNumber].moveLeft()
                if canMoveDown(Grid, FindBottomCords(AllShapes[ShapeNumber].cordinates)):
                    StagTimer = time.time()

            #ROTATION
            if event.key == pygame.K_UP:
                oldCords = AllShapes[ShapeNumber].cordinates
                Grid = fillWithNum(Grid, oldCords, 0)

                AllShapes[ShapeNumber].rotate()
                RotatedCords = AllShapes[ShapeNumber].rotationCordinates

                if canRotate(RotatedCords, Grid):
                    Grid = fillWithNum(Grid, oldCords, 0)
                    AllShapes[ShapeNumber].updateCords(RotatedCords)
                else:
                    AllShapes[ShapeNumber].rotationNumber-=1

                if canMoveDown(Grid, FindBottomCords(AllShapes[ShapeNumber].cordinates)):
                    StagTimer = time.time()

    #Draws grid   
    if not GameOver:
        drawGrid(Grid, screen)
        Outlines.draw(screen) #Will Draw Grid
        Grid = fillWithNum(Grid, AllShapes[ShapeNumber].cordinates, AllShapes[ShapeNumber].number)

        show_score(textX, textY, screen, Score, font)
        show_level(textX + 225, textY, screen, level, font)
        pygame.display.update()
    else:
        Grid = [[0]*10 for pos in range(20)]
        show_GameOver(80, 400, screen, font)
        show_score(textX, textY, screen, Score, font)
        show_level(textX + 225, textY, screen, level, font)
        pygame.display.update()
        time.sleep(5)
        break


# %%
