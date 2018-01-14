"""Brings together the components of the game and allows functionality"""

#import required files
import PacManBoard
import PacManGraphics
import PacManPlayer
import PacManGhosts

#import required modules
import sys, pygame

DOTSCORE = 10
PELLETSCORE = 50
GHOSTSCORE = 200

class PacManEngine:
    def __init__(self):
        #Setup pygame
        pygame.init()
        pygame.font.init()

        #Create the player object and board object.
        self.player = PacManPlayer.Player()

        self.board = PacManBoard.Board()

        """Testing for ghosts"""
        self.ghost = PacManGhosts.Ghost()

        #Call the graphics function that creates the window and font.
        self.display, self.font, self.background, self.gameSprites = PacManGraphics.setupDisplay()

        #Creates a clock object to manage the framerate of the game.
        self.clock = pygame.time.Clock()

    def getPlayerInput(self):
        #Create an empty list of attempted moves.
        directions = []

        #Get a dictionary with each key and a boolean value of whether it has been pressed this tick.
        keysPressed = pygame.key.get_pressed()

        #If one of the arrow keys has been pressed, update a direction variable to the associated direction.
        #Allows for movement in more than one direction, as long as these directions are not opposing, to avoid bugs.
        if keysPressed[pygame.K_RIGHT]:
            directions.append("right")
        elif keysPressed[pygame.K_LEFT]:
            directions.append("left")
        if keysPressed[pygame.K_UP]:
            directions.append("up")
        elif keysPressed[pygame.K_DOWN]:
            directions.append("down")

        #Check if each move in the required direction is valid, and if it is then make it.
        for direction in directions:
            if self.checkPlayerMove(direction):
                self.player.move(direction)
                self.player.tile = self.board.findTile(self.player.x, self.player.y)

        #Code for testing player coordinates. Remove later.
        if keysPressed[pygame.K_RETURN]:
            print("""x %s
            y %s""" %(self.player.x, self.player.y))

    def checkPlayerMove(self, direction):
        #Check that the move is valid using the board's checkValidPosition function.
        if direction == "right":
            return self.board.checkValidPosition(self.player.x + 1, self.player.y)
        elif direction == "left":
            return self.board.checkValidPosition(self.player.x - 1, self.player.y)
        elif direction == "up":
            return self.board.checkValidPosition(self.player.x, self.player.y - 1)
        else:
            return self.board.checkValidPosition(self.player.x, self.player.y + 1)

    def gameloop(self):
        #Get the events that have occurred, and check to see if the user wants to quit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        #If the player is carrying out the death animation the checks for actions may be skipped.
        if self.player.checkDying():
            self.player.deathSequence()
        else:
            """Will need to be checked to see if the user is playing"""
            #Check to see if the player wants to move.
            self.getPlayerInput()

            #Check to see if the player has moved through a tunnel.
            self.board.checkTunnel(self.player)

            """Removed temporarily
            #Check to see if the player has eaten any Pac-Dots.
            self.board.eatDot(self.player.x, self.player.y)
            """

            """Testing"""
            if self.ghost.checkEaten(self.player):
                self.player.startDeath()

        #Draw the board and the player using the functions from the graphics file.
        PacManGraphics.drawboard(self.display, self.background)
        PacManGraphics.drawSprite(self.display, self.player.x - 7, self.player.y - 6, self.gameSprites, self.player.spriteLoc)

        """Testing"""
        PacManGraphics.drawRects(self.display, self.player.x, self.player.y)
        PacManGraphics.drawRects(self.display, self.player.x - 1, self.player.y + 1)
        PacManGraphics.drawRects(self.display, self.player.x - 7, self.player.y - 6)
        #PacManGraphics.drawGrid(self.display)

        #Sets the maximum framerate to 60 fps.
        self.clock.tick(60)

        """Removed temporarily
        PacManGraphics.drawPacDots(self.display, self.board.dots)
        """

        #Draw the ghosts
        PacManGraphics.drawSprite(self.display, self.ghost.x - 7, self.ghost.y - 7, self.gameSprites, self.ghost.spriteLoc)

        """Testing"""
        PacManGraphics.drawInfo(self.display, 0, self.player.lives, self.gameSprites, self.font)
        #Update the display so the changes are shown.
        pygame.display.update()
