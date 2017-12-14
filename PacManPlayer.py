#Pac-Man is 16 by 16.

#Locations of Pac-Man movement sprites in the spritesheet.
START = (488,0,17,16)
RIGHT1 = (454,0,17,16)
RIGHT2 = (471,0,17,16)
LEFT1 = (454,16,17,16)
LEFT2 = (471,16,17,16)
UP1 = (471,32,17,16)
UP2 = (471,32,17,16)
DOWN1 = (471,48,17,16)
DOWN2 = (471,48,17,16)

class Player():
    def __init__(self):
        self.y = 125
        self.x = 130
        self.spriteLoc = START

    def move(self, direction):
        if direction == "right":
            self.x += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "up":
            self.y -= 1
        else:
            self.y += 1
