#Pac-Man is 16 by 16.

#Locations of Pac-Man movement sprites in the spritesheet.
START = (489,1,14,14)
RIGHT1 = (457,1,14,14)
RIGHT2 = (473,1,14,14)
LEFT1 = (457,17,14,14)
LEFT2 = (473,17,14,14)
UP1 = (457,33,14,14)
UP2 = (473,33,14,14)
DOWN1 = (457,49,14,14)
DOWN2 = (473,49,14,14)

#Creates lists of sprites according to whether they have their mouth open or closed.
OPENSPRITES = [RIGHT1, LEFT1, UP1, DOWN1]
CLOSEDSPRITES = [RIGHT2, LEFT2, UP2, DOWN2]

class Player():
    def __init__(self):
        #Set the starting position of the player
        self.y = 211
        self.x = 139
        self.spriteLoc = START
        self.updateCount = 0

    def move(self, direction):
        if direction == "right":
            self.x += 1
            self.updateSprite(0)

        elif direction == "left":
            self.x -= 1
            self.updateSprite(1)

        elif direction == "up":
            self.y -= 1
            self.updateSprite(2)

        else:
            self.y += 1
            self.updateSprite(3)

    def updateSprite(self, direction):
        self.updateCount += 1
        if self.updateCount == 5:
            if self.spriteLoc in OPENSPRITES:
                self.spriteLoc = CLOSEDSPRITES[direction]
            else:
                self.spriteLoc = OPENSPRITES[direction]
            self.updateCount = 0
