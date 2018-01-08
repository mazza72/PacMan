"""Class & methods that define the board and allow it to be used"""

#Tunnels are at y 140
#Gate and start are at x 139

#26 pac dots
#8 Pixels between each pac dot

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
                    colx = i * 8 + 45
                    if objx > colx and objx <= colx + 8:
                        #Use the row and columnn to return the objects current tile.
                        print("i", i)
                        print("j", j)
                        return self.tiles[j][i]

    def checkValidPosition(self, objx, objy):
        #Find the tile the object would lie on if they moved.
        tile = self.findTile(objx, objy)
        #Return whether that tile can be moved to.
        return tile[0]

    def checkTunnel(self, objToCheck):
        #Check if a ghost or the player has passed through a tunnel to the other side of the board.
        print("Testing")

    def eatDot(self, playerTile):
        #Use the playerTile tuple to access the relevent tile, and look at it's value for whether there is a PacDot there.
        if self.tiles[playerTile[0]][playerTile[1]][1]:
            self.tiles[playerTile[0]][playerTile[1]][1] = False
            return True
        else:
            return False
