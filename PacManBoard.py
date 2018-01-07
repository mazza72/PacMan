"""Class & methods that define the board and allow it to be used"""

#Tunnels are at y 140
#Gate and start are at x 139

#26 pac dots
#8 Pixels between each pac dot

class Board():
    def __init__(self):
        self.bonuses = 2
        """Create a list of Pac-Dot objects and their locations"""
        self.dots = [[PacDot(45, 42), PacDot(53, 42), PacDot(61, 42), PacDot(69, 42), PacDot(77, 42), PacDot(85, 42), PacDot(93, 42), PacDot(101, 42), PacDot(109, 42), PacDot(117, 42), PacDot(125, 42), PacDot(133, 42), PacDot(157, 42), PacDot(165, 42), PacDot(173, 42), PacDot(181, 42), PacDot(189, 42), PacDot(197, 42), PacDot(205, 42), PacDot(213, 42), PacDot(221, 42), PacDot(229, 42), PacDot(237, 42), PacDot(245, 42)],
        [PacDot(45, 50), PacDot(85, 50), PacDot(133, 50), PacDot(157, 50), PacDot(205, 50), PacDot(245, 50)],
        [PacDot(85, 58), PacDot(133, 58), PacDot(157, 58), PacDot(205, 58)],
        [PacDot(45, 66), PacDot(85, 66), PacDot(133, 66), PacDot(157, 66), PacDot(205, 66), PacDot(245, 66)],
        [PacDot(45, 74), PacDot(53, 74), PacDot(61, 74), PacDot(69, 74), PacDot(77, 74), PacDot(85, 74), PacDot(93, 74), PacDot(101, 74), PacDot(109, 74), PacDot(117, 74), PacDot(125, 74), PacDot(133, 74), PacDot(141, 74), PacDot(149, 74), PacDot(157, 74), PacDot(165, 74), PacDot(173, 74), PacDot(181, 74), PacDot(189, 74), PacDot(197, 74), PacDot(205, 74), PacDot(213, 74), PacDot(221, 74), PacDot(229, 74), PacDot(237, 74), PacDot(245, 74)],
        [PacDot(45, 82), PacDot(85, 82), PacDot(109, 82), PacDot(181, 82), PacDot(205, 82), PacDot(245, 82)],
        [PacDot(45, 90), PacDot(85, 90), PacDot(109, 90), PacDot(181, 90), PacDot(205, 90), PacDot(245, 90)],
        [PacDot(45, 98), PacDot(53, 98), PacDot(61, 98), PacDot(69, 98), PacDot(77, 98), PacDot(85, 98), PacDot(109, 98), PacDot(117, 98), PacDot(125, 98), PacDot(133, 98), PacDot(157, 98), PacDot(165, 98), PacDot(173, 98), PacDot(181, 98), PacDot(205, 98), PacDot(213, 98), PacDot(221, 98), PacDot(229, 98), PacDot(237, 98), PacDot(245, 98)],
        [PacDot(85, 106), PacDot(205, 106)],
        [PacDot(85, 114), PacDot(205, 114)],
        [PacDot(85, 122), PacDot(205, 122)],
        [PacDot(85, 130), PacDot(205, 130)],
        [PacDot(85, 138), PacDot(205, 138)],
        [PacDot(85, 146), PacDot(205, 146)],
        [PacDot(85, 154), PacDot(205, 154)],
        [PacDot(85, 162), PacDot(205, 162)],
        [PacDot(85, 170), PacDot(205, 170)],
        [PacDot(85, 178), PacDot(205, 178)],
        [PacDot(85, 186), PacDot(205, 186)],
        [PacDot(45, 194), PacDot(53, 194), PacDot(61, 194), PacDot(69, 194), PacDot(77, 194), PacDot(85, 194), PacDot(93, 194), PacDot(101, 194), PacDot(109, 194), PacDot(117, 194), PacDot(125, 194), PacDot(133, 194), PacDot(157, 194), PacDot(165, 194), PacDot(173, 194), PacDot(181, 194), PacDot(189, 194), PacDot(197, 194), PacDot(205, 194), PacDot(213, 194), PacDot(221, 194), PacDot(229, 194), PacDot(237, 194), PacDot(245, 194)],
        [PacDot(45, 202), PacDot(85, 202), PacDot(133, 202), PacDot(157, 202), PacDot(205,202), PacDot(245, 202)],
        [PacDot(45, 210), PacDot(85, 210), PacDot(133, 210), PacDot(157, 210), PacDot(205,210), PacDot(245, 210)],
        [PacDot(53, 218), PacDot(61, 218), PacDot(85, 218), PacDot(93, 218), PacDot(101, 218), PacDot(109, 218), PacDot(117, 218), PacDot(125, 218), PacDot(133, 218), PacDot(157, 218), PacDot(165, 218), PacDot(173, 218), PacDot(181, 218), PacDot(189, 218), PacDot(197, 218), PacDot(205, 218), PacDot(229, 218), PacDot(237, 218)],
        [PacDot(61, 226), PacDot(85, 226), PacDot(109, 226), PacDot(181, 226), PacDot(205, 226), PacDot(229, 226)],
        [PacDot(61, 234), PacDot(85, 234), PacDot(109, 234), PacDot(181, 234), PacDot(205, 234), PacDot(229, 234)],
        [PacDot(45, 242), PacDot(53, 242), PacDot(61, 242), PacDot(69, 242), PacDot(77, 242), PacDot(85, 242), PacDot(109, 242), PacDot(117, 242), PacDot(125, 242), PacDot(133, 242), PacDot(157, 242), PacDot(165, 242), PacDot(173, 242), PacDot(181, 242), PacDot(205, 242), PacDot(213, 242), PacDot(221, 242), PacDot(229, 242), PacDot(237, 242), PacDot(245, 242)],
        [PacDot(45, 250), PacDot(133, 250), PacDot(157, 250), PacDot(245, 250)],
        [PacDot(45, 258), PacDot(133, 258), PacDot(157, 258), PacDot(245, 258)],
        [PacDot(45, 266), PacDot(53, 266), PacDot(61, 266), PacDot(69, 266), PacDot(77, 266), PacDot(85, 266), PacDot(93, 266), PacDot(101, 266), PacDot(109, 266), PacDot(117, 266), PacDot(125, 266), PacDot(133, 266), PacDot(141, 266), PacDot(149, 266), PacDot(157, 266), PacDot(165, 266), PacDot(173, 266), PacDot(181, 266), PacDot(189, 266), PacDot(197, 266), PacDot(205, 266), PacDot(213, 266), PacDot(221, 266), PacDot(229, 266), PacDot(237, 266), PacDot(245, 266)]]
        self.edges = [Edge(54,251,70,6), Edge(54,203,22,6), Edge(70,209,6,24), Edge(94,227,6,24), Edge(94,203,30,6), Edge(33,227,19,6),
        Edge(33,183,3,92), Edge(33,155,43,30), Edge(33,275,224,3), Edge(142,227,6,30), Edge(118,227,54,6), Edge(142,185,6,24), Edge(118,179,54,6), Edge(94,155,6,30),
        Edge(166,251,70,6), Edge(214,203,22,6), Edge(214,209,6,24), Edge(190,227,6,24), Edge(166,203,30,6), Edge(238,227,19,6),
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
            objToCheck.x = 245
        #Compare the x coordinate of the object to the right side of the board.
        elif objToCheck.x > 245:
            objToCheck.x = 33

    def eatDots(self, playerx, playery):
        playerendy = playery + 14
        #Compare the players y coordinates to those of the row rather than comparing to every dot.
        for row in range(len(self.dots)):
            rowCoord = 42 + row * 8
            #If the player is within that row, loop through each dot.
            if playery > rowCoord - 8 and playery < rowCoord + 8 or playerendy > rowCoord - 8 and playerendy < rowCoord + 8:
                for dot in range(len(self.dots[row])):
                    #Remove the dot if the player is on top of it.
                    if self.dots[row][dot].checkEaten(playerx,playery):
                        del self.dots[row][dot]
                        #Exits the function to prevent list index out of range error and because the player cannot simultaneously eat 2 dots.
                        return

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
        else:
            return False

class PacDot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def checkEaten(self, playerx, playery):
        #Calculate the coordinates of where the player object ends.
        playerendx = playerx + 14
        playerendy = playery + 14
        #Check if the player coords surround those of the dot. If yes return true for being eaten.
        if playerx < self.x and playerendx > self.x + 2 and playery < self.y and playerendy > self.y + 2:
            return True
        else:
            return False
