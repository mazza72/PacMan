"""Class & methods that define the board and allow it to be used"""

#Tunnels are at y 140
#Gate and start are at x 139


class Board():
    def __init__(self):
        self.bonuses = 2
        """Create a list of Pac-Dot objects and their locations, as well
        as sectioning each section of the board."""
        self.edges = [Edge(110,250,15,8)]

    def checkValidPosition(self,objx, objy, objwidth, objlen):
        for edge in self.edges:
            if edge.checkCollision(objx, objy, objwidth, objlen):
                return False
        return True

class Edge():
    def __init__(self, x, y, width, length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    #Function to check if a rectangular object has collided with the edge.
    def checkCollision(self, objx, objy, objwidth, objlen):
        #Calculate the second coordinates of the object.
        objx2 = objx + objwidth
        objy2 = objy + objlen

        #Check if any of the objects coordinates place it over the edge.
        if (objx >= self.x and objx <= self.x + self.width or objx2 >= self.x and objx2 <= self.x + self.width or objx <= self.x and objx2 >= self.x + self.width) \
        and (objy >= self.y and objy <= self.y + self.length or objy2 >= self.y and objy2 <= self.y + self.length or objy <= self.y and objy2 >= self.y + self.length):
            return True
