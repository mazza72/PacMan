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

SCATTER1 = (617, 65, 14, 14)
SCATTER2 = (617, 65, 14, 14)

FOURLEG = [BLINKYRIGHT1, BLINKYLEFT1, BLINKYDOWN1, BLINKYUP1, PINKYRIGHT1, PINKYLEFT1, PINKYDOWN1, PINKYUP1, INKYRIGHT1, INKYLEFT1, INKYDOWN1, INKYUP1, CLYDERIGHT1, CLYDELEFT1, CLYDEDOWN1, CLYDEUP1]
THREELEG = [BLINKYRIGHT2, BLINKYLEFT2, BLINKYDOWN2, BLINKYUP2, PINKYRIGHT2, PINKYLEFT2, PINKYDOWN2, PINKYUP2, INKYRIGHT2, INKYLEFT2, INKYDOWN2, INKYUP2, CLYDERIGHT2, CLYDELEFT2, CLYDEDOWN2, CLYDEUP2]

class Ghost():
    def __init__(self):
        #Set the mode of the ghost to chase mode. 1 is scatter and 2 is frightened modes. 3 is used when the ghost has been eaten.
        self.mode = 0
        self.speed = 0.5
        #Default sprite is blinky's right movement.
        self.spriteLoc = BLINKYRIGHT1
        self.x = 139
        self.y = 114

    def getTarget(self, player):
        self.targetPos = (player.x, player.y)
        return self.targetPos

    def checkEaten(self, player):
        if (player.x >= self.x and player.x <= self.x + 14 or player.x + 14 >= self.x and player.x + 14 <= self.x + 14 or player.x <= self.x and player.x + 14 >= self.x + 14) \
        and (player.y >= self.y and player.y <= self.y + 14 or player.y + 14 >= self.y and player.y + 14 <= self.y + 14 or player.y <= self.y and player.y + 14 >= self.y + 14):
            return True
        else:
            return False
