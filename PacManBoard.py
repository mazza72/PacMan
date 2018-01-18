"""Class & methods that define the board and allow it to be used"""

#Array with the state of each tile in the grid. (Possible to move to, PacDot existence)
BOARDTEMPLATE = [[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),
(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),
(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),
(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, False),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),
(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),
(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),
(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(True, False),(False, False),(False, False),(True, False),
(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(True, False),(False, False),(False, False),(True, False),
(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(True, False),(True, False),(True, False),(True, False),(True, False),(True, False),
(True, False),(True, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(True, False),(True, False),(True, False),(True, False),(True, False),(True, False),(True, True),(True, False),(True, False),(True, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, False),(True, False),(True, False),(True, True),(True, False),(True, False),(True, False),(True, False),(True, False),(True, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(True, False),(True, False),(True, False),(True, False),(True, False),(True, False),
(True, False),(True, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)],
[(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),
(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),
(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),
(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, False),(True, True),(True, True),(False, False),(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, False),(True, False),(True, True),
(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),(True, True),(True, False),(False, False)],
[(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False)],
[(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),(False, False),(False, False),(False, False)],
[(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),
(True, True),(True, True),(True, True),(False, False),(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),
(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, True),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False),(False, False),(True, True),
(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(True, True),(False, False)],
[(False, False),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),
(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(True, True),(False, False)],
[(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),
(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False),(False, False)]]

class Board():
    def __init__(self):
        self.bonuses = 2
        self.tiles = BOARDTEMPLATE

    def findTile(self, objx, objy):
        #Check if the object's centre lies in a specific row.
        for j in range(len(self.tiles)):
            rowy = j * 8 + 45
            if objy > rowy and objy <= rowy + 8:
                #Check which column the object's centre lies in.
                for i in range(len(self.tiles[j])):
                    colx = i * 8 + 48
                    if objx > colx and objx <= colx + 8:
                        #Return the row and column of the objects current tile.
                        return (j,i)

    def checkValidPosition(self, objx, objy):
        #Check that the 2x2 centre of the sprite doesn't lie over a tile that cannot be moved to.
        j, i = self.findTile(objx, objy)
        tile = self.tiles[j][i]
        j, i = self.findTile(objx - 1, objy + 1)
        tile2 = self.tiles[j][i]
        #Return whether that tile can be moved to.
        if tile[0] and tile2[0]:
            return True
        else:
            return False

    def checkTunnel(self, objToCheck):
        #Check if a ghost or the player has passed through a tunnel to the other side of the board.
        #Compare the x coordinate of the object to the left side of the board.
        if objToCheck.x == 57:
            objToCheck.x = 266
        #Compare the x coordinate of the object to the right side of the board.
        elif objToCheck.x == 266:
            objToCheck.x = 57

    def eatDot(self, playerTile):
        #Use the playerTile tuple to access the relevent tile, and look at it's value for whether there is a PacDot there.
        if self.tiles[playerTile[0]][playerTile[1]][1]:
            canMove = self.tiles[playerTile[0]][playerTile[1]][0]
            self.tiles[playerTile[0]][playerTile[1]] = (canMove, False)
            return True
        else:
            return False

    def calculateDistance(self, tile1, tile2):
        #Calculate the distance between two board tiles.
        xdist = abs(tile1[0] - tile2[0])
        ydist = abs(tile1[1] - tile2[1])
        distance = (xdist ** 2 + ydist ** 2) ** 0.5
