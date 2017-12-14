"""Brings together the components of the game and allows functionality"""

#import required files
import PacManBoard
import PacManGraphics
import PacManPlayer

#import required modules
import sys, pygame

class PacManEngine:
    def __init__(self):
        #Setup pygame
        pygame.init()
        pygame.font.init()

        #Create the player object.
        self.player = PacManPlayer.Player()

        self.playerx = 0 #Remove later

        #Call the graphics function that creates the window and font.
        self.display, self.font, self.background, self.gameSprites = PacManGraphics.setupDisplay()

    def getPlayerInput(self):
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_RIGHT]:
            self.player.move("right")
        elif keysPressed[pygame.K_LEFT]:
            self.player.move("left")
        elif keysPressed[pygame.K_UP]:
            self.player.move("up")
        elif keysPressed[pygame.K_DOWN]:
            self.player.move("down")

    def gameloop(self):

        #get the events that have occurred.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        self.getPlayerInput()

        PacManGraphics.drawboard(self.display, self.background)
        PacManGraphics.drawPlayer(self.display, self.player.x, self.player.y)

        pygame.display.update()
