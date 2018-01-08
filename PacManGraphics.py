"""Functions for the drawing of the game"""

#import spritesheet file
import spritesheet

#import pygame module
import pygame

#Set constant values for the program.
BACKGROUNDFILE = "Background.png"
IMAGEHEIGHT = 249
IMAGEWIDTH = 231
FONTSIZE = 15
"""Change to 45???"""
OUTLINESPACING = 30

#Colour constants
BLACK  = (0,0,0)
DOTCOLOUR = (88,83,87)
WHITE = (255,255,255)
"""Testing"""
RED = (255, 0, 0)

#Window height and width for the pygame display, using the size of the background image and a space for an outline.
WINDOWWIDTH= IMAGEWIDTH + 2 * OUTLINESPACING
WINDOWHEIGHT = IMAGEHEIGHT + 2 * OUTLINESPACING +15

def setupDisplay():

    #Create a window of the speicified height and width.
    display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pac-Man demonstration')
    background = pygame.image.load(BACKGROUNDFILE).convert()

    #Create the spritesheet using the spritesheet class.
    gameSprites = spritesheet.spritesheet("GeneralSprites.png")

    #Create a new font object of the default pygame font, and with the specified font size.
    gamefont = pygame.font.Font(None, FONTSIZE)
    return (display, gamefont, background, gameSprites)

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

def drawPacDots(display, dotTable):
    for dotList in dotTable:
        for dot in dotList:
            pygame.draw.rect(display, DOTCOLOUR, (dot.x, dot.y, 2, 2), 0)

def drawInfo(display, score, lives, spriteSheet, font):
    y = 279
    sprite = spriteSheet.image_at((473,17,14,14))
    for life in range(lives):
        x = 46 + life * 16
        display.blit(sprite, (x,y))
    label1 = font.render("1UP    HIGH SCORE", 1, WHITE)
    label2 = font.render(str(score), 1, WHITE)
    """Change to 102,15?"""
    display.blit(label1, (54, 0))
    display.blit(label2, (78 - 8 * len(str(score)), 8))


"""Testing"""
def drawEdge(display, edge):
    pygame.draw.rect(display, RED, (edge.x, edge.y, edge.width, edge.length), 0)
