"""Brings together the components of the game and allows functionality"""

#import required files
import PacManBoard
import PacManGraphics
import PacManPlayer
import PacManGhosts

#import required modules
import sys, pygame, random, time

DOTSCORE = 10
PELLETSCORE = 50
GHOSTSCORE = 200
FRUITSCORES = [100, 300, 500, 700, 1000, 2000, 3000, 5000]

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

        #Create an empty score and a counter for the number of dots eaten.
        self.score = 0
        self.dotCount = 0

        """Testing"""
        self.fruit = False
        self.level = 1

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

            #Check to see if the player has eaten any Pac-Dots. Returns True if it has.
            if self.board.eatDot(self.player.tile):
                self.score += DOTSCORE
                self.dotCount += 1

                #Check if enough dots have been eaten to generate fruit.
                if self.dotCount == 70 or self.dotCount == 170:
                    self.fruit = True
                    #Create a time limit between 9 and 10 seconds for the fruit to exist for.
                    self.fruitLimit = 9 + random.uniform(0,1)
                    #Find the time the fruit was created at.
                    self.fruitTime = time.time()

            """Testing"""
            if self.ghost.checkEaten(self.player):
                self.player.startDeath()

        #Sets the maximum framerate to 60 fps.
        self.clock.tick(60)

        #Draw the constant objects.
        self.drawObjects()

        #Draw fruit along the bottom of the board according to the current level.
        PacManGraphics.drawFruitsRow(self.display, self.gameSprites, self.level)

        #Check if there is currently fruit on the board.
        if self.fruit:
            #If the player is on the fruit tile, remove it and add to the score.
            if self.player.tile == (17,14):
                self.fruit = False
                self.score += FRUITSCORES[((self.level - 1) % 8)]
            #Otherwise, if more time has elapsed than the limit set at creation, remove the fruit.
            elif (time.time() - self.fruitTime) > self.fruitLimit:
                self.fruit = False
            #Draw the fruit if nothing has happened to it.
            else:
                PacManGraphics.drawFruit(self.display, self.gameSprites, self.level)

        #Update the display so the changes are shown.
        pygame.display.update()

    def drawObjects(self):
        #Calls the required draw functions for objects that always exist.

        #Draw the board and the player.
        PacManGraphics.drawboard(self.display, self.background)
        PacManGraphics.drawSprite(self.display, self.player.x - 7, self.player.y - 6, self.gameSprites, self.player.spriteLoc)

        #Draw the ghosts.
        PacManGraphics.drawSprite(self.display, self.ghost.x - 7, self.ghost.y - 7, self.gameSprites, self.ghost.spriteLoc)

        #Add labels to the edge of the board - lives, score etc.
        PacManGraphics.drawInfo(self.display, self.score, self.player.lives, self.gameSprites, self.font)

        #Use the board tiles to draw the PacDots.
        PacManGraphics.drawPacDots(self.display, self.board.tiles)
