# xs at 123, 153, 139
#ys at 138 and 114

#Blinky's first sprite at 457, 65 - all 14,14
#16 pixels between 2 starts of sprites.
#order of sprites is blinky, pinky, inky, clyde

#possibly create a scatterCount frightenedTime and frightenedTarget attribute when implementing modes.

BLINKYRIGHT1 = (457, 65, 14, 14)
BLINKYRIGHT2 = (473, 65, 14, 14)
BLINKYLEFT1 = (489, 65, 14, 14)
BLINKYLEFT2 = (505, 65, 14, 14)
BLINKYUP1 = (521, 65, 14, 14)
BLINKYUP2 = (537, 65, 14, 14)
BLINKYDOWN1 = (553, 65, 14, 14)
BLINKYDOWN2 = (569, 65, 14, 14)

class Ghost():
    def __init__(self):
        #Set the mode of the ghost to chase mode. 1 is scatter and 2 is frightened modes.
        self.mode = 0
        self.speed = 0.5
        #Default sprite is blinky's right movement.
        self.spriteLoc = BLINKYRIGHT1
        self.x = 139
        self.y = 114

    def getTarget(self, player):
        self.targetPos = (player.x, player.y)
        return self.targetPos
