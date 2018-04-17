"""Brings together the components of the game and allows functionality"""

#import required files
import PacManBoard
import PacManGraphics
import PacManPlayer
import PacManGhosts
import PacManAI

#import required modules
import sys, pygame, random, time, math

#Constants for updating score.
DOTSCORE = 10
PELLETSCORE = 50
GHOSTSCORE = 200
FRUITSCORES = [100, 300, 500, 700, 1000, 2000, 3000, 5000]

#Tiles over which bonus fruit is placed
FRUITTILES = [(17,14),(17,13)]

class PacManEngine:
    def __init__(self):
        #Setup pygame
        pygame.init()
        pygame.font.init()

        #Create the player, board and ghost objects from their respective files.
        self.player = PacManPlayer.Player()
        self.board = PacManBoard.Board()
        self.ghosts = [PacManGhosts.Blinky(), PacManGhosts.Pinky(), PacManGhosts.Inky(), PacManGhosts.Clyde()]

        #Call the graphics function that creates the window and font.
        self.display, self.font, self.backgrounds, self.gameSprites = PacManGraphics.setupDisplay()

        #Creates a clock object to manage the framerate of the game.
        self.clock = pygame.time.Clock()

        #Create an empty score and a counter for the number of dots eaten.
        self.score = 0
        self.dotCount = 0
        self.eatenGhosts = 0

        #Create variables for whether there is active fruit and what the current level is.
        self.fruit = False
        self.level = 1


    def playLevels(self, user = True):
        #Load the starting screen and set default settings for the first level.
        self.setSpeeds()
        self.getReady()
        self.user = user

        #Load the AI if there is no one playing.
        if not user:
            self.ai = PacManAI.Agent()

        #While the player is able to continue playing.
        while self.gameloop():
            if self.dotCount == 240 and self.board.pelletList == []:
                for i in range(100):
                    #Draw all of the constants except the ghosts.
                    PacManGraphics.drawboard(self.display, self.backgrounds[(i // 7) % 2])
                    PacManGraphics.drawInfo(self.display, self.score, self.player.lives, self.gameSprites, self.font)
                    PacManGraphics.drawSprite(self.display, self.player.x - 7, self.player.y - 6, self.gameSprites, self.player.spriteLoc)
                    PacManGraphics.drawFruitsRow(self.display, self.gameSprites, self.fruitIndex())
                    #Limit the framerate to 60 frames per second.
                    self.clock.tick(60)
                    pygame.display.update()

                #Once one level finishes, update settings and reset the board.
                self.level += 1
                self.board = PacManBoard.Board()
                self.dotCount = 0
                self.setSpeeds()
                self.getReady()

        #Once the game is finished.
        while True:
            #Get the events that have occurred, and check to see if the user wants to quit.
            for event in pygame.event.get():
                keysPressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keysPressed[pygame.K_ESCAPE]:
                    pygame.quit()
                    return self.score
                #If the player presses 'r', reset the game without exiting the window.
                elif keysPressed[pygame.K_r]:
                    self.resetGame()
                    self.playLevels(user)
                    return self.score

            #Keep drawing all of the required objects, as well as the game over font.
            self.drawObjects()
            PacManGraphics.gameOver(self.display, self.font)
            pygame.display.update()


    def movePlayer(self):
        #Check if the user is playing, and if so get the input from the arrow keys.
        if self.user:
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
                if self.checkMove(direction, self.player):
                    self.player.move(direction)
                    self.player.tile = self.board.findTile(self.player.x, self.player.y)

        #If the game is not being controlled manually.
        else:
            #Store the current score for the AI to use for learning.
            self.ai.recordScore(self.score)
            #Get the desired move from the AI given the current state information and available moves.
            direction = self.ai.generateMove(self.generateState(), self.findAvailableMoves())
            #Move the player in the given direction and update the player information accordingly.
            self.player.move(direction)
            self.player.tile = self.board.findTile(self.player.x, self.player.y)

    def checkMove(self, direction, entity):
        #Check that the move is valid using the board's checkValidPosition function.
        if direction == "right":
            return self.board.checkValidPosition(entity.x + entity.speed, entity.y)
        elif direction == "left":
            return self.board.checkValidPosition(entity.x - entity.speed, entity.y)
        elif direction == "up":
            return self.board.checkValidPosition(entity.x, entity.y - entity.speed)
        else:
            return self.board.checkValidPosition(entity.x, entity.y + entity.speed)


    def gameloop(self):
        #Get the events that have occurred, and check to see if the user wants to quit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        #Check if a ghost has died and call getReady function
        if self.player.checkDying():
            #If the death sequence is just completing, return the ghosts and player to start conditions.
            if self.player.deathSequence():
                self.getReady()
        else:
            self.takePlayerTurn()
            self.takeGhostTurn()

        #Check if enough dots have been eaten to generate fruit.
        if self.dotCount == 70 or self.dotCount == 170:
            self.fruit = True
            #Create a time limit between 9 and 10 seconds for the fruit to exist for.
            self.fruitLimit = 9 + random.uniform(0,1)
            #Find the time the fruit was created at.
            self.fruitTime = time.time()

        #Sets the maximum framerate to 60 fps.
        self.clock.tick(60)

        #Draw the constant objects.
        self.drawObjects()

        #Check if there is currently fruit on the board.
        if self.fruit:
            #If the player is on the fruit tile, remove it and add to the score.
            if self.player.tile in FRUITTILES:
                self.fruit = False
                self.score += FRUITSCORES[self.fruitIndex()]
            #Otherwise, if more time has elapsed than the limit set at creation, remove the fruit.
            elif (time.time() - self.fruitTime) > self.fruitLimit:
                self.fruit = False
            #Draw the fruit if nothing has happened to it.
            else:
                PacManGraphics.drawFruit(self.display, self.gameSprites, self.fruitIndex())

        #Update the display so the changes are shown.
        pygame.display.update()

        #Use the expected reward vs achieved reward to update the AI weights if it is playing.
        if not self.user:
            self.ai.updateWeights(self.score, self.generateState(), self.findAvailableMoves())

        #Check if the player still has lives to continue with, and if so return True.
        if self.player.lives < 0 and self.player.deathCount == 12:
            return False
        else:
            return True


    def takePlayerTurn(self):
        if not self.player.checkEating():
            #Move the player in the desired direction.
            self.movePlayer()

            #Check to see if the player has moved through a tunnel.
            self.board.checkTunnel(self.player)

            #Check to see if the player has eaten any Pac-Dots. Returns True if it has.
            if self.board.eatDot(self.player.tile):
                self.score += DOTSCORE
                self.dotCount += 1
                self.player.pauseToEat(0)

            #Does the same for Power Pellets and puts the ghosts into frightened mode if so.
            elif self.board.eatPellet(self.player.tile):
                self.score += PELLETSCORE
                for ghost in self.ghosts:
                    self.eatenGhosts = 0
                    ghost.updateMode(2)
                self.player.pauseToEat(1)


    def takeGhostTurn(self):
        #Ensure the ghosts are travelling at the correct speed for their current mode and level.
        self.setSpeeds()

        for ghost in self.ghosts:
            #Check for a collision between the ghost and player.
            if ghost.checkEaten(self.player):
                #Either start the ghost's death or the player's death depending on the ghost mode.
                if ghost.mode == 2:
                    self.score += GHOSTSCORE * (2 ** self.eatenGhosts)
                    ghost.startDeath()
                elif ghost.mode != 3:
                    #Increase the AI's expected value in order to create a negative difference in reward.
                    if not self.user:
                        self.ai.expectedVal += 50
                    self.player.startDeath()

            #Check if the ghost is centred on a tile.
            if self.board.checkTileCentre(ghost.x, ghost.y):
                #Check if the ghost has changed tiles since the last junction.
                if ghost.leftTile():
                    #Find whether the ghost is at a junction, and where the free tiles are.
                    atJunction, freeTiles = self.board.checkJunction(ghost.tile)
                    if atJunction:
                        #Update the ghost's target in order to decide the direction.
                        ghost.getTarget(self.player, self.ghosts[0].tile)
                        #Choose the direction that gives the best outcome.
                        ghost.useJunction(freeTiles)

            #Check if the ghost is in the ghost house, and if so make it follow the set course of action.
            if ghost.ghostHouse == True:
                ghost.houseAction()

            #Otherwise move the ghost in the direction based on its target location.
            elif ghost.direction == [-1, 0] and self.checkMove("left", ghost) \
            or ghost.direction == [1, 0] and self.checkMove("right", ghost) \
            or ghost.direction == [0, -1] and self.checkMove("up", ghost) \
            or ghost.direction == [0, 1] and self.checkMove("down", ghost):
                #Move the ghost in the set direction and animate it.
                ghost.move()
                #Update the ghost's tile.
                ghost.tile = self.board.findTile(ghost.x, ghost.y)

            #Animate the ghost's movement and check if it needs to change level.
            ghost.updateSprite()
            ghost.checkModeChange(self.level)


    def setSpeeds(self):
        #Assign object speeds based on the current level.
        if self.ghosts[0].mode != 2:
            if self.level == 1:
                self.player.setSpeed(0.8)
                for ghost in self.ghosts:
                    ghost.setSpeed(0.75)
            elif self.level <= 4:
                self.player.setSpeed(0.9)
                for ghost in self.ghosts:
                    ghost.setSpeed(0.85)
            elif self.level <= 20:
                self.player.setSpeed(1)
                for ghost in self.ghosts:
                    ghost.setSpeed(0.95)
            else:
                self.player.setSpeed(0.9)
                for ghost in self.ghosts:
                    ghost.setSpeed(0.95)

            for ghost in self.ghosts:
                if self.board.checkTunnel(ghost):
                    self.ghostTunnel(ghost)
            self.ghosts[0].elroySpeed(self.dotCount, self.level)

        else:
            if self.level == 1:
                self.player.setSpeed(0.9)
                for ghost in self.ghosts:
                    ghost.setSpeed(0.5)
            elif self.level <= 4:
                self.player.setSpeed(0.95)
                for ghost in self.ghosts:
                    ghost.setSpeed(0.55)
            elif self.level <= 20:
                self.player.setSpeed(1)
                for ghost in self.ghosts:
                    ghost.setSpeed(0.6)

            for ghost in self.ghosts:
                self.board.checkTunnel(ghost)

    #Return the correct speed percentage for a ghost in the tunnel.
    def ghostTunnel(self, ghost):
        if self.level == 1:
            ghost.setSpeed(0.4)
        elif self.level <= 4:
            ghost.setSpeed(0.45)
        elif self.level <= 20:
            ghost.setSpeed(0.5)
        else:
            ghost.setSpeed(0.5)


    #Return the index of the current level's fruit in the constant list.
    def fruitIndex(self):
        if self.level < 2:
            return self.level - 1
        elif self.level < 13:
            return math.ceil(self.level / 2)
        else:
            return 7


    def drawObjects(self):
        #Calls the required draw functions for objects that always exist.

        #Draw the board.
        PacManGraphics.drawboard(self.display, self.backgrounds[0])
        #Add labels to the edge of the board - lives, score etc.
        PacManGraphics.drawInfo(self.display, self.score, self.player.lives, self.gameSprites, self.font)

        #Use the board tiles to draw the PacDots.
        PacManGraphics.drawPacDots(self.display, self.board.tiles)
        PacManGraphics.drawPellets(self.display, self.gameSprites, self.board.pelletList)

        #Draw the player.
        PacManGraphics.drawSprite(self.display, self.player.x - 7, self.player.y - 6, self.gameSprites, self.player.spriteLoc)

        #Draw the ghosts.
        for ghost in self.ghosts:
            PacManGraphics.drawSprite(self.display, ghost.x - 7, ghost.y - 7, self.gameSprites, ghost.spriteLoc)

        #Draw fruit along the bottom of the board according to the current level.
        PacManGraphics.drawFruitsRow(self.display, self.gameSprites, self.fruitIndex())


    #Reset the conditions of the level.
    def getReady(self):
        self.player.startConditions()
        #Remove the bonus fruit.
        self.fruit = False

        for ghost in self.ghosts:
            ghost.startConditions()

        #Pause the game with the 'get ready' text.
        for i in range(150):
            self.drawObjects()
            PacManGraphics.newLevel(self.display, self.font)
            pygame.display.update()
            self.clock.tick(60)

    #Reset the whole game back to the first level. Create a new player and board.
    def resetGame(self):
        self.score = 0
        self.dotCount = 0
        self.level = 1
        self.board = PacManBoard.Board()
        self.player = PacManPlayer.Player()


    #Wrapper function to create the list of information for the AI to use.
    def generateState(self):
        chasingGhosts = []
        frightenedGhosts = []

        #Add the ghost's distance to different lists depending on the mode, since this affects the behaviour towards it.
        for ghost in self.ghosts:
            if ghost.mode == 0:
                chasingGhosts.append(ghost.tile)
                frightenedGhosts.append(None)
            elif ghost.mode == 1:
                chasingGhosts.append(None)
                frightenedGhosts.append(ghost.tile)

        state = [self.player.tile, chasingGhosts, frightenedGhosts, self.board.tiles, self.board.pelletList, self.fruit]
        return state


    #Check the tiles around the player for ones that can be moved to, to be considered by the AI.
    def findAvailableMoves(self):
        availableMoves = []
        if self.board.checkTile((self.player.tile[0] - 1, self.player.tile[1])):
            availableMoves.append("up")
        if self.board.checkTile((self.player.tile[0] + 1, self.player.tile[1])):
            availableMoves.append("down")
        if self.board.checkTile((self.player.tile[0], self.player.tile[1] - 1)):
            availableMoves.append("left")
        if self.board.checkTile((self.player.tile[0], self.player.tile[1] + 1)):
            availableMoves.append("right")
        return availableMoves
