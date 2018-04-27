import MergeSort
import random

#Constants for the locations of the ghost sprites in the spritesheet.
BLINKYRIGHT1 = (457, 65, 14, 14)
BLINKYRIGHT2 = (473, 65, 14, 14)
BLINKYLEFT1 = (489, 65, 14, 14)
BLINKYLEFT2 = (505, 65, 14, 14)
BLINKYUP1 = (521, 65, 14, 14)
BLINKYUP2 = (537, 65, 14, 14)
BLINKYDOWN1 = (553, 65, 14, 14)
BLINKYDOWN2 = (569, 65, 14, 14)

PINKYRIGHT1 = (457, 81, 14, 14)
PINKYRIGHT2 = (473, 81, 14, 14)
PINKYLEFT1 = (489, 81, 14, 14)
PINKYLEFT2 = (505, 81, 14, 14)
PINKYUP1 = (521, 81, 14, 14)
PINKYUP2 = (537, 81, 14, 14)
PINKYDOWN1 = (553, 81, 14, 14)
PINKYDOWN2 = (569, 81, 14, 14)

INKYRIGHT1 = (457, 97, 14, 14)
INKYRIGHT2 = (473, 97, 14, 14)
INKYLEFT1 = (489, 97, 14, 14)
INKYLEFT2 = (505, 97, 14, 14)
INKYUP1 = (521, 97, 14, 14)
INKYUP2 = (537, 97, 14, 14)
INKYDOWN1 = (553, 97, 14, 14)
INKYDOWN2 = (569, 97, 14, 14)

CLYDERIGHT1 = (457, 113, 14, 14)
CLYDERIGHT2 = (473, 113, 14, 14)
CLYDELEFT1 = (489, 113, 14, 14)
CLYDELEFT2 = (505, 113, 14, 14)
CLYDEUP1 = (521, 113, 14, 14)
CLYDEUP2 = (537, 113, 14, 14)
CLYDEDOWN1 = (553, 113, 14, 14)
CLYDEDOWN2 = (569, 113, 14, 14)

FRIGHTENED1 = (585, 65, 14, 14)
FRIGHTENED2 = (601, 65, 14, 14)

FRIGHTENED3 = (617, 65, 14, 14)
FRIGHTENED4 = (633, 65, 14, 14)

DEATHSPRITES = [(585, 81, 14, 14),(601, 81, 14, 14),(633, 81, 14, 14),(617, 81, 14, 14)]

FOURLEG = [BLINKYRIGHT1, BLINKYLEFT1, BLINKYDOWN1, BLINKYUP1, PINKYRIGHT1, PINKYLEFT1, PINKYDOWN1, PINKYUP1, INKYRIGHT1, INKYLEFT1, INKYDOWN1, INKYUP1, CLYDERIGHT1, CLYDELEFT1, CLYDEDOWN1, CLYDEUP1]
THREELEG = [BLINKYRIGHT2, BLINKYLEFT2, BLINKYDOWN2, BLINKYUP2, PINKYRIGHT2, PINKYLEFT2, PINKYDOWN2, PINKYUP2, INKYRIGHT2, INKYLEFT2, INKYDOWN2, INKYUP2, CLYDERIGHT2, CLYDELEFT2, CLYDEDOWN2, CLYDEUP2]

#Constant for the number of dots left when blnky increases his speed.
ELROYDOTS = [10,15,20,20,20,25,25,25,30,30,30,40,40,40,50,50,50,50,60]
ELROYPROP = [0.85,0.95,0.95,0.95,1.05]

#List containing the scatter tiles for each of the ghosts.
SCATTERTILES = [(-2, 29), (-2,3), (30,29), (30,1)]

#Lists containing the time the ghosts remain frightened for and the number of flashes during the transition back.
FRIGHTENEDTIME = [6,5,4,3,2,5,2,2,1,5,2,1,1,3,1,1,0,1,0]
TRANSITIONFRAMES = [5,5,5,5,5,5,5,5,3,5,5,3,3,5,3,3,0,3,0]

class Ghost():
    def __init__(self):
        #Set the mode of the ghost to chase mode. 1 is scatter and 2 is frightened modes. 3 is used when the ghost has been eaten.
        self.mode = 0
        self.speed = 0.5
        #Default sprite is blinky's right movement.
        self.spriteLoc = BLINKYRIGHT1
        #Stores the number of the ghost to be used for generating sprites etc.
        self.ghostNo = 0
        #Store Blinky's hard-coded start location.
        self.x = 161
        self.y = 136
        self.tile = (11,13)
        self.oldTile = (11,13)
        #Store the direction as moving left for when the ghost initially moves.
        self.direction = [-1, 0]
        #Store a boolean value for if the direction of the ghost has changed in the last tick.
        self.directionChange = False
        #Store a counter for the number of ticks between animations.
        self.updateCount = 0
        #Store a counter for the delay when cornering.
        self.cornerCount = 3
        self.speed = 0
        self.ghostHouse = False
        self.modeCounter = 0
        self.transitionCount = 0


    def startConditions(self):
        #Return the ghost to default conditions.
        self.mode = 0
        self.spriteLoc = BLINKYRIGHT1
        self.x = 161
        self.y = 136
        self.tile = (11,13)
        self.oldTile = (11,13)
        self.ghostHouse = False
        self.direction = [-1, 0]
        self.directionChange = False
        self.updateCount = 0
        self.cornerCount = 3
        self.speed = 0


    def getTarget(self, player, blinkyPos):
        #Target the player's current tile if in a chase mode.
        if self.mode == 0 or self.mode == 2:
            self.targetPos = player.tile
        #Target the scatter tile if in scatter mode.
        elif self.mode == 1:
            self.targetPos = SCATTERTILES[self.ghostNo]
        #If ghost is dead, check if currently in the ghost house, otherwise aim for it.
        else:
            if self.tile[0] == 11 and self.tile[1] > 11 and self.tile[1] < 15:
                self.ghostHouse = True
            else:
                self.targetPos = (11,13)


    def checkEaten(self, player):
        #Check for a collision with the player.
        if player.tile == self.tile:
            return True
        else:
            return False


    def startDeath(self):
        self.mode = 3
        """Add animation here"""

    def updateMode(self, mode):
        #Store the current mode in case the ghost needs to return to it.
        self.lastmode = self.mode
        #Update the ghost's mode to the one it is switching to.
        self.mode = mode

        #Reverse the direction of the ghost unless it is leaving frightened mode.
        if self.lastmode != 2 and self.lastmode != 3:
            self.direction = list(map((lambda x: -1 * x), self.direction))
            self.directionChange = True
        self.modeCounter = 0


    def useJunction(self, freeTiles):
        #Use the current direciton the player is travelling in to determine the point of entry.
        valueTest = list(map(lambda x: abs(x), self.direction))

        if valueTest != self.direction:
            entryTile = 2 + abs(self.direction[0])
        else:
            entryTile = self.direction[0]
        #Stop the ghost leaving the way it came in.
        freeTiles[entryTile] = None

        #If currently frightened, pick a random tile to leave by.
        if self.mode == 2:
            index = random.randint(0,3)
            #If the random direction is not valid, iterate through them until one is found.
            if not freeTiles[index]:
                index = 0
                while not freeTiles[index]:
                    index += 1

        #If not currently frightened, find the tile closest to the target position and use that direction.
        else:
            distances = []
            for tile in freeTiles:
                if tile != None:
                    distances.append(self.calculateDistance(tile, self.targetPos))
                else:
                    distances.append(100000)
            orderedDistances = MergeSort.mergeSort(distances)
            #Return the index of the minimum value in the list.
            minDistance = orderedDistances[0]
            index = distances.index(minDistance)

        #Update the direction of the ghost based on the tile it is now aiming for.
        if index == 0:
            self.direction = [0, -1]
        elif index == 1:
            self.direction = [-1, 0]
        elif index == 2:
            self.direction = [0, 1]
        elif index == 3:
            self.direction = [1, 0]

        #Reset the delay counter for taking a corner.
        self.cornerCount = 0


    def updateSprite(self):
        #Animates the player sprite.
        if self.checkAnimation():
            #Check if the ghost is in chase mode, and therefore uses a default sprite.
            if self.mode == 0:
                #Generate a location for the position of the sprite within the list.
                spritePos = self.ghostNo * 4 + 2 * abs(self.direction[1])

                #Test whether one of the values within the direction is negative, and if so, use the next location along in the list.
                valueTest = list(map(lambda x: abs(x), self.direction))
                if valueTest != self.direction:
                    spritePos += 1

                #Checks what the existing sprite is, and loads the alternate one.
                if self.spriteLoc in FOURLEG:
                    self.spriteLoc = THREELEG[spritePos]
                else:
                    self.spriteLoc = FOURLEG[spritePos]

            elif self.mode == 2:
                if self.spriteLoc == FRIGHTENED1:
                    self.spriteLoc = FRIGHTENED2
                elif self.spriteLoc == FRIGHTENED4:
                    self.spriteLoc = FRIGHTENED3
                elif self.spriteLoc == FRIGHTENED3:
                    self.spriteLoc = FRIGHTENED4
                else:
                    self.spriteLoc = FRIGHTENED1

            elif self.mode == 3:
                #Generate a location for the position of the sprite within the list.
                spritePos = 2 * abs(self.direction[1])

                #Test whether one of the values within the direction is negative, and if so, use the next location along in the list.
                valueTest = list(map(lambda x: abs(x), self.direction))
                if valueTest != self.direction:
                    spritePos += 1

                #Find the required sprites from the deathsprites list.
                self.spriteLoc = DEATHSPRITES[spritePos]


    def checkModeChange(self, level):
        self.modeCounter += 1
        #If in frightened mode, see if enough time has passed to leave it.
        if self.mode == 2:
            if FRIGHTENEDTIME[level - 1] <= self.modeCounter / 60:
                self.leaveFrightened(level)
        else:
            self.transitionCount = 0


    def leaveFrightened(self, level):
        #Create the flashing blue/white animation to show the ghosts are leaving frightened mode.
        self.transitionCount += 1
        if (self.transitionCount / 10) % 1 == 0:
            if self.spriteLoc == FRIGHTENED3 or self.spriteLoc == FRIGHTENED4:
                self.spriteLoc = FRIGHTENED1
            else:
                self.spriteLoc = FRIGHTENED3

        #Once enough time has passed, return the ghost to chase mode.
        if self.transitionCount >= TRANSITIONFRAMES[level] * 20:
            self.updateMode(0)


    def checkAnimation(self):
        #Checks if 5 ticks have passed since the last sprite change.
        self.updateCount += 1

        #If 5 ticks have passed:
        if self.updateCount == 5:
            #Reset the counter and return true.
            self.updateCount = 0
            return True
        else:
            return False


    def move(self):
        #Check the ghost has finished turning a corner.
        if self.cornerCount == 3:
            self.x += self.direction[0]
            self.y += self.direction[1]
        else:
            self.cornerCount += 1


    def calculateDistance(self, tile1, tile2):
        #Calculate the distance between two board tiles using pythagoras.
        xdist = abs(tile1[0] - tile2[0])
        ydist = abs(tile1[1] - tile2[1])
        distance = (xdist ** 2 + ydist ** 2) ** 0.5
        return distance


    def leftTile(self):
        #Check if the ghost has left the tile it was in yet.
        if self.tile != self.oldTile or self.directionChange:
            self.oldTile = self.tile
            self.directionChange = False
            return True
        else:
            return False


    #Set the speed attribute based on the percentage of the base speed the ghost should currently have.
    def setSpeed(self, proportion):
        self.speed = 1.46 * proportion


    #Set animation for the ghost leaving the ghost house - move to centre then up and out.
    def houseAction(self):
        if self.mode == 0:
            if self.x < 161:
                self.x += 1
            elif self.x > 161:
                self.x -= 1
            elif self.y > 136:
                self.y -= 1
            else:
                self.ghostHouse = False
        else:
            if self.x < 161:
                self.x += 1
            elif self.x > 161:
                self.x -= 1
            elif self.y < 160:
                self.y += 1
            else:
                self.updateMode(0)


class Blinky(Ghost):
    def elroySpeed(self, dotCount, level):
        #Sets the speed to blinky relative to how many dots have been eaten. Uses the constant lists defined previously.
        if level >= 19:
            if dotCount >= 120:
                self.setSpeed(1)
            elif dotCount >= 180:
                self.setSpeed(1.05)
            else:
                self.setSpeed(1.05)
        else:
            if dotCount > 240 - ELROYDOTS[level - 1]:
                self.setSpeed(ELROYPROP[level - 1])
            elif dotCount > 240 - 2 * ELROYDOTS[level - 1]:
                self.setSpeed(ELROYPROP[level - 1] - 0.05)


class Pinky(Ghost):
    def __init__(self):
        super(Pinky, self).__init__()
        #Default sprite is blinky's right movement.
        self.spriteLoc = PINKYRIGHT1
        #Stores the number of the ghost to be used for generating sprites etc.
        self.ghostNo = 1
        #Store Pinky's hard-coded start location.
        self.x = 161
        self.y = 160
        self.ghostHouse = True


    def getTarget(self, player, blinkyPos):
        #If in chase mode, calculate the tile two ahead of where the player is looking.
        if self.mode == 0:
            if player.direction == 0:
                self.targetPos = (player.tile[0], player.tile[1] + 2)
            elif player.direction == 1:
                self.targetPos = (player.tile[0], player.tile[1] - 2)
            elif player.direction == 2:
                self.targetPos = (player.tile[0] - 1, player.tile[1])
            else:
                self.targetPos = (player.tile[0] + 1, player.tile[1])
        #If in scatter mode, use the ghost class version of the getTarget function.
        else:
            super(Pinky, self).getTarget(player, blinkyPos)


    def startConditions(self):
        super(Pinky, self).startConditions()
        self.spriteLoc = PINKYRIGHT1
        self.x = 161
        self.y = 160
        self.ghostHouse = True


class Inky(Ghost):
    def __init__(self):
        super(Inky, self).__init__()
        #Default sprite is blinky's right movement.
        self.spriteLoc = INKYRIGHT1
        #Stores the number of the ghost to be used for generating sprites etc.
        self.ghostNo = 2
        #Store Inky's hard-coded start location.
        self.x = 177
        self.y = 160
        #Values for if the ghost is in the ghost house and how long they have been there.
        self.ghostHouse = True
        self.houseCounter = 0


    def getTarget(self, player, blinkyPos):
        #Returns the specific target for inky based on blinky and the player's positions.
        if self.mode == 0:
            if player.direction == 0:
                pinkyTarget = (player.tile[0], player.tile[1] + 2)
            elif player.direction == 1:
                pinkyTarget = (player.tile[0], player.tile[1] - 2)
            elif player.direction == 2:
                pinkyTarget = (player.tile[0] - 1, player.tile[1])
            else:
                pinkyTarget = (player.tile[0] + 1, player.tile[1])

            targetx = pinkyTarget[1] + 2 * (pinkyTarget[1] - blinkyPos[1])
            targety = pinkyTarget[0] + 2 * (pinkyTarget[0] - blinkyPos[0])
            self.targetPos = (targety, targetx)
        #Returns the generic targets if the ghost is in scatter, frightened or dead modes.
        else:
            super(Inky, self).getTarget(player, blinkyPos)


    def startConditions(self):
        super(Inky, self).startConditions()
        self.spriteLoc = INKYRIGHT1
        self.x = 177
        self.y = 160
        self.ghostHouse = True


class Clyde(Ghost):
    def __init__(self):
        super(Clyde, self).__init__()
        #Default sprite is blinky's right movement.
        self.spriteLoc = CLYDERIGHT1
        #Stores the number of the ghost to be used for generating sprites etc.
        self.ghostNo = 3
        #Store Clyde's hard-coded start location.
        self.x = 145
        self.y = 160
        self.ghostHouse = True


    def getTarget(self, player, blinkyPos):
        #Returns the player's tile as a target if player is more than 8 tiles away.
        if self.mode == 0:
            #Otherwise returns scatter target.
            if self.calculateDistance(player.tile, self.tile) <= 8:
                self.targetPos = (30,1)
            else:
                self.targetPos = player.tile
        #Returns the generic targets if the ghost is in scatter, frightened or dead modes.
        else:
            super(Clyde, self).getTarget(player, blinkyPos)


    def startConditions(self):
        super(Clyde, self).startConditions()
        self.spriteLoc = CLYDERIGHT1
        self.x = 145
        self.y = 160
        self.ghostHouse = True
