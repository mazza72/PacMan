"""Functions for the drawing of the game"""

#import spritesheet file
import spritesheet

#import pygame module
import pygame

#Set constant values for the program.
BACKGROUNDFILE1 = "Background.png"
BACKGROUNDFILE2 = "BackgroundWhite.png"
IMAGEHEIGHT = 249
IMAGEWIDTH = 231
FONTSIZE = 20
OUTLINESPACING = 45

#List containing the locations of each fruit.
FRUITS = [(489,49,14,14), (505,49,14,14), (521,49,14,14), (537,49,14,14), (553,49,14,14), (569,49,14,14), (585,49,14,14), (601,49,14,14)]
PELLET = (8,184,8,8)

#Colour constants
BLACK  = (0,0,0)
DOTCOLOUR = (250,185,176)
WHITE = (255,255,255)
RED = (255,0,0)

#Window height and width for the pygame display, using the size of the background image and a space for an outline.
WINDOWWIDTH = IMAGEWIDTH + 2 * OUTLINESPACING
WINDOWHEIGHT = IMAGEHEIGHT + 2 * OUTLINESPACING

def setupDisplay():
    #Create a window of the speicified height and width.
    display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pac-Man demonstration')
    background1 = pygame.image.load(BACKGROUNDFILE1).convert()
    background2 = pygame.image.load(BACKGROUNDFILE2).convert()

    #Create the spritesheet using the spritesheet class.
    gameSprites = spritesheet.spritesheet("GeneralSprites.png")

    #Create a new font object of the default pygame font, and with the specified font size.
    gamefont = pygame.font.Font(None, FONTSIZE)
    return (display, gamefont, (background1, background2), gameSprites)

def drawboard(display, backgroundimage):
    display.fill(BLACK)
    display.blit(backgroundimage, (OUTLINESPACING, OUTLINESPACING))

def mousepos(display):
    """probably pass in a list of button objects that you can check the coordinates of vs the mousepos"""
    (mouseX, mouseY) = pygame.mouse.get_pos()
    return mouseX, mouseY

def drawSprite(display, x, y, spriteSheet, spriteLocation):
    sprite = spriteSheet.image_at(spriteLocation)
    display.blit(sprite, (x,y))

def drawPacDots(display, Tiles):
    #Check each tile in the array.
    for row in range(len(Tiles)):
        doty = 48 + row * 8
        for col in range(len(Tiles[row])):
            #If the Tile has a PacDot in it.
            if Tiles[row][col][1]:
                dotx = 52 + col * 8
                #Draw the dot.
                pygame.draw.rect(display, DOTCOLOUR, (dotx, doty, 2, 2), 0)

def drawInfo(display, score, lives, spriteSheet, font):
    #Set a constant height for the bottom of the board.
    y = 294
    #Load the life sprite.
    sprite = spriteSheet.image_at((473,17,14,14))
    #Draw as many lives as the player has at 16 pixel intervals along the bottom of the screen.
    for life in range(lives):
        x = 46 + life * 16
        display.blit(sprite, (x,y))

    #Write the high score and current score to the screen.
    """Need to add a high score loaded from file"""
    label1 = font.render("1UP    HIGH SCORE", 1, WHITE)
    label2 = font.render(str(score), 1, WHITE)
    display.blit(label1, (54, 0))
    #Change the starting position of the score label according to the number of digits it has, so it remains in place.
    display.blit(label2, (78 - 8 * len(str(score)), 12))

def drawFruitsRow(display, spriteSheet, fruitIndex):
    #Draw a row of fruit along the bottom of the board according to the level.
    for fruit in range(fruitIndex + 1):
        sprite = spriteSheet.image_at(FRUITS[fruit])
        #Decrease the x coordinate by 16 pixel intervals for each fruit.
        display.blit(sprite, (250 - fruit * 16,294))

def drawPellets(display, spriteSheet, pelletList):
    sprite = spriteSheet.image_at(PELLET)
    for pellet in pelletList:
        if pellet[1]:
            display.blit(sprite, (49 + 8 * pellet[0][1], 45 + 8 * pellet[0][0]))

def drawFruit(display, spritesSheet, fruitIndex):
    #Draw the fruit associated with the current level at a constant position.
    sprite = spritesSheet.image_at(FRUITS[fruitIndex])
    display.blit(sprite, (154, 178))

def gameOver(display, font):
    overLabel = font.render("GAME   OVER", 1, RED)
    display.blit(overLabel, (116,177))

def newLevel(display, font):
    readyLabel = font.render("READY", 1, RED)
    display.blit(readyLabel, (137,177))
