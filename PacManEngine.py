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

        #Creates a clock object to manage the framerate of the game.
        self.clock = pygame.time.Clock()

    def getPlayerInput(self):
        #Get a dictionary with each key and a boolean value of whether it has been pressed this tick.
        keysPressed = pygame.key.get_pressed()

        #If one of the arrow keys has been pressed, get the player object to move in the associated direction.
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

        #Check to see if the player wants to move.
        self.getPlayerInput()

        #Draw the board and the player using the functions from the graphics files.
        PacManGraphics.drawboard(self.display, self.background)
        print("PLAYERX", self.player.x)
        PacManGraphics.drawSprite(self.display, self.player.x, self.player.y, self.gameSprites, self.player.spriteLoc)

        #Sets the maximum framerate to 40 fps.
        self.clock.tick(40)

        #Update the display so the changes are shown.
        pygame.display.update()
