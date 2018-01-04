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


#Locations of Pac-Man death sprites.
DEATHSPRITES = [(505,1,14,14),(521,1,14,14),(537,1,14,14),(553,1,14,14),(569,1,14,14),(585,1,14,14),(601,1,14,14),(617,1,14,14),(633,1,14,14),(649,1,14,14)]

#Creates lists of sprites according to whether they have their mouth open or closed.
OPENSPRITES = [RIGHT1, LEFT1, UP1, DOWN1]
CLOSEDSPRITES = [RIGHT2, LEFT2, UP2, DOWN2]

class Player():
    def __init__(self):
        #Set the starting position of the player.
        self.y = 211
        self.x = 139
        #Set the player's sprite to the starting sprite.
        self.spriteLoc = START
        #Counter to delay the changing of sprites to make animations visible.
        self.updateCount = 0
        #Counter for the death sprites.
        self.deathCount = 0

    def move(self, direction):
        #Updates the position of the player based on the direction it is moving.
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
        #Animates the player sprite.
        if self.checkAnimation():
            #Checks what the existing sprite is, and loads the alternate one.
            if self.spriteLoc in OPENSPRITES:
                self.spriteLoc = CLOSEDSPRITES[direction]
            else:
                self.spriteLoc = OPENSPRITES[direction]

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

    def deathSequence(self):
        print("Running sequence")
        #Handles the animation and effects of the player's death.
        #Check if the player has already cycled through all death sprites.
        if self.deathCount < 10:
            print("Death count within range")
            if self.checkAnimation():
                print("Animation counter working")
                #Update the sprite to the next one in the list.
                self.spriteLoc = DEATHSPRITES[self.deathCount]
                #Add to the counter to keep track of the position in the list.
                self.deathCount += 1
        #If the death animation has been completed:
        else:
            #Reset the counter.
            self.deathCount = 0
            #Return the player to starting conditions.
            self.y = 211
            self.x = 139
            self.spriteLoc = START
            self.updateCount = 0

    def startDeath(self):
        #Begins the death animation and resets the animation counter.
        self.updateCount = 0
        self.spriteLoc = DEATHSPRITES[0]
        self.deathCount = 1

    def checkDying(self):
        #Return whether the player is currently carrying out the death animation.
        if self.deathCount > 0:
            return True
        else:
            return False
