"""Class & methods that define the board and allow it to be used"""

#Tunnels are at y 140
#Gate and start are at x 139


class Board():
    def __init__(self):
        self.bonuses = 2
        """Create a list of Pac-Dot objects and their locations, as well
        as sectioning each section of the board."""
        self.edges = [Edge(54,251,70,6), Edge(54,203,22,6), Edge(70,209,6,24), Edge(94,227,6,24), Edge(94,203,30,6), Edge(33,227,19,6),
        Edge(33,183,3,92), Edge(33,155,43,30), Edge(33,275,224,3), Edge(142,227,6,30), Edge(118,227,54,6), Edge(142,185,6,24), Edge(118,179,54,6), Edge(94,155,6,30),
        Edge(166,251,70,6), Edge(214,203,22,6), Edge(214,209,6,24), Edge(190,227,6,24), Edge(167,203,30,6), Edge(238,227,19,6),
        Edge(254,183,3,92), Edge(214,155,43,30), Edge(190,155,6,30),
        Edge(54,51,22,14), Edge(94,51,30,14), Edge(54,83,22,6), Edge(94,83,6,54), Edge(100,107,24,6),
        Edge(214,51,22,14), Edge(166,51,30,14), Edge(214,83,22,6), Edge(190,83,6,54), Edge(166,107,24,6),
        Edge(33,30,224,3), Edge(33,33,3,77), Edge(254,33,3,77), Edge(214,107,43,30), Edge(33,107,43,30),
        Edge(142,83,6,30), Edge(118,83,54,6), Edge(142,33,6,32), Edge(118,131,18,2), Edge(154,131,18,2), Edge(118,133,2,28), Edge(120,159,52,2), Edge(170,133,2,28)]

    def checkValidPosition(self,objx, objy, objwidth, objlen):
        for edge in self.edges:
            if edge.checkCollision(objx, objy, objwidth, objlen):
                return False
        return True

    def checkTunnel(self, objToCheck):
        #Check if a ghost or the player has passed through a tunnel to the other side of the board.
        #Compare the x coordinate of the object to the left side of the board.
        if objToCheck.x < 33:
            objToCheck.x = 248
        #Compare the x coordinate of the object to the right side of the board.
        elif objToCheck.x > 248:
            objToCheck.x = 33

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
