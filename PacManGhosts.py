# xs at 123, 153, 139
#ys at 138 and 114

#Blinky's first sprite at 457, 65 - all 14,14
#16 pixels between 2 starts of sprites.
#order of sprites is blinky, pinky, inky, clyde

#possibly create a scatterCount frightenedTime and frightenedTarget attribute when implementing modes.

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

"""Possibly split into separate lists that are stored within the object itself?"""
FOURLEG = [BLINKYRIGHT1, BLINKYLEFT1, BLINKYDOWN1, BLINKYUP1, PINKYRIGHT1, PINKYLEFT1, PINKYDOWN1, PINKYUP1, INKYRIGHT1, INKYLEFT1, INKYDOWN1, INKYUP1, CLYDERIGHT1, CLYDELEFT1, CLYDEDOWN1, CLYDEUP1]
THREELEG = [BLINKYRIGHT2, BLINKYLEFT2, BLINKYDOWN2, BLINKYUP2, PINKYRIGHT2, PINKYLEFT2, PINKYDOWN2, PINKYUP2, INKYRIGHT2, INKYLEFT2, INKYDOWN2, INKYUP2, CLYDERIGHT2, CLYDELEFT2, CLYDEDOWN2, CLYDEUP2]

#Constant for the number of dots left when blnky increases his speed.
ELROYDOTS = [10,15,20,20,20,25,25,25,30,30,30,40,40,40,50,50,50,50,60]
ELROYPROP = [0.85,0.95,0.95,0.95,1.05]

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
        #Store a counter for the number of ticks between animations.
        self.updateCount = 0
        #Store a counter for the delay when cornering.
        self.cornerCount = 3
        self.speed = 0
        """Testing"""
        self.ghostHouse = False

    def getTarget(self, player):
        """Currently returns blinky's target, following the player."""
        if self.mode == 0:
            self.targetPos = player.tile
        elif self.mode == 1:
            self.targetPos = (-2, 3)

    def checkEaten(self, player):
        #Check for a collision with the player.
        if player.tile == self.tile:
            return True
        else:
            return False

    def startDeath(self):
        self.mode = 3
        """Add transition to death sprite???"""

    def updateMode(self, mode):
        #Store the current mode in case the ghost needs to return to it.
        self.lastmode = self.mode
        #Update the ghost's mode to the one it is switching to.
        self.mode = mode
        #Reverse the direction of the ghost unless it is leaving frightened mode.
        if self.lastmode != 2:
            self.direction = list(map((lambda x: -1 * x), self.direction))

    def useJunction(self, freeTiles):
        valueTest = list(map(lambda x: abs(x), self.direction))
        if valueTest != self.direction:
            entryTile = 2 + abs(self.direction[0])
        else:
            entryTile = self.direction[0]
        freeTiles[entryTile] = None
        distances = []
        for tile in freeTiles:
            if tile != None:
                distances.append(self.calculateDistance(tile, self.targetPos))
            else:
                distances.append(100000)
        #Return the index of the minimum value in the list.
        index = distances.index(min(distances))
        if index == 0:
            self.direction = [0, -1]
        elif index == 1:
            self.direction = [-1, 0]
        elif index == 2:
            self.direction = [0, 1]
        elif index == 3:
            self.direction = [1, 0]
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
        if self.ghostHouse:
            self.leaveHouse()
        else:
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
        if self.tile != self.oldTile:
            self.oldTile = self.tile
            return True
        else:
            return False

    def setSpeed(self, proportion):
        self.speed = 1.46 * proportion


    def leaveHouse(self):
        if self.x < 161:
            self.x += 1
        elif self.x > 161:
            self.x -= 1
        elif self.y > 136:
            self.y -= 1
        else:
            self.ghostHouse = False

class Blinky(Ghost):
    def elroySpeed(self, dotCount, level):
        if level >= 19:
            if dotCount >= 120:
                self.setSpeed(1)
            elif dotCount >= 180:
                self.setSpeed(1.05)
            self.setSpeed(1.05)
        else:
            if dotCount > 240 - 2 * ELROYDOTS[level - 1]:
                self.setSpeed(ELROYPROP[level - 1] - 0.05)
            elif dotCount > 240 - ELROYDOTS[level - 1]:
                self.setSpeed(ELROYPROP[level - 1])

class Pinky(Ghost):
    def __init__(self):
        super(Pinky, self).__init__()
        #Default sprite is blinky's right movement.
        self.spriteLoc = PINKYRIGHT1
        #Stores the number of the ghost to be used for generating sprites etc.
        self.ghostNo = 1
        #Store Pinky's hard-coded start location.
        self.x = 161
        self.y = 144
        self.tile = (12,13)
        self.oldTile = (12,13)
        self.ghostHouse = True
        
    def getTarget(self, player):
        if player.direction == 0:
            self.targetPos = (player.tile[0], player.tile[1] + 2)
        elif player.direction == 1:
            self.targetPos = (player.tile[0], player.tile[1] - 2)
        elif player.direction == 2:
            self.targetPos = (player.tile[0] - 1, player.tile[1])
        else:
            self.targetPos = (player.tile[0] + 1, player.tile[1])
        return self.targetPos

class Inky(Ghost):
    def __init__(self):
        super(Inky, self).__init__()
        #Default sprite is blinky's right movement.
        self.spriteLoc = INKYRIGHT1
        #Stores the number of the ghost to be used for generating sprites etc.
        self.ghostNo = 2
        #Store Inky's hard-coded start location.
        self.x = 169
        self.y = 144
        self.tile = (12,14)
        self.oldTile = (12,14)

class Clyde(Ghost):
    def __init__(self):
        super(Clyde, self).__init__()
        #Default sprite is blinky's right movement.
        self.spriteLoc = CLYDERIGHT1
        #Stores the number of the ghost to be used for generating sprites etc.
        self.ghostNo = 3
        #Store Clyde's hard-coded start location.
        self.x = 153
        self.y = 144
        self.tile = (12,13)
        self.oldTile = (12,13)
