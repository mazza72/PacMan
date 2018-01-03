"""Brings together the components of the game and allows functionality"""

#import required files
import PacManBoard
import PacManGraphics
import PacManPlayer
import PacManGhosts

#import required modules
import sys, pygame

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
        #Create an empty direction variable.
        direction = None

        #Get a dictionary with each key and a boolean value of whether it has been pressed this tick.
        keysPressed = pygame.key.get_pressed()

        #If one of the arrow keys has been pressed, update a direction variable to the associated direction.
        if keysPressed[pygame.K_RIGHT]:
            direction = "right"
        elif keysPressed[pygame.K_LEFT]:
            direction = "left"
        elif keysPressed[pygame.K_UP]:
            direction = "up"
        elif keysPressed[pygame.K_DOWN]:
            direction = "down"

        #Check if the move in the required direction is valid, and if it is then make it.
        if direction is not None:
            if self.checkPlayerMove(direction):
                self.player.move(direction)

        #Code for testing player coordinates. Remove later.
        if keysPressed[pygame.K_RETURN]:
            print("""x %s
            y %s""" %(self.player.x, self.player.y))

    def checkPlayerMove(self, direction):
        #Check that the move is valid using the board's checkValidPosition function.
        if direction == "right":
            return self.board.checkValidPosition(self.player.x + 1, self.player.y, 14, 14)
        elif direction == "left":
            return self.board.checkValidPosition(self.player.x - 1, self.player.y, 14, 14)
        elif direction == "up":
            return self.board.checkValidPosition(self.player.x, self.player.y - 1, 14, 14)
        else:
            return self.board.checkValidPosition(self.player.x, self.player.y + 1, 14, 14)

    def gameloop(self):
        #Get the events that have occurred, and check to see if the user wants to quit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        """Will need to be checked to see if the user is playing"""
        #Check to see if the player wants to move.
        self.getPlayerInput()

        #Check to see if the player has moved through a tunnel.
        self.board.checkTunnel(self.player)

        #Check to see if the player has eaten any Pac-Dots.
        self.board.eatDots(self.player.x, self.player.y)

        #Draw the board and the player using the functions from the graphics file.
        PacManGraphics.drawboard(self.display, self.background)
        PacManGraphics.drawSprite(self.display, self.player.x, self.player.y, self.gameSprites, self.player.spriteLoc)

        #Sets the maximum framerate to 40 fps.
        self.clock.tick(40)

        """Testing - draw all the edges."""
        for edge in range(len(self.board.edges)):
            PacManGraphics.drawEdge(self.display, self.board.edges[edge])

        PacManGraphics.drawPacDots(self.display, self.board.dots)

        #Draw the ghosts
        PacManGraphics.drawSprite(self.display, self.ghost.x, self.ghost.y, self.gameSprites, self.ghost.spriteLoc)

        #Update the display so the changes are shown.
        pygame.display.update()
