"""Class & methods that define the board and allow it to be used"""

import copy

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
        self.tiles = copy.deepcopy(BOARDTEMPLATE)
        self.pelletList = [((3,26), True), ((3,1), True), ((23,26), True), ((23,1), True)]


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
        #Check if the ghost or player is within the tunnel.
        if objToCheck.tile[0] == 14:
            if objToCheck.tile[1] < 5 or objToCheck.tile[1] > 21:
                #Check if a ghost or the player has passed through a tunnel to the other side of the board.
                #Compare the x coordinate of the object to the left side of the board.
                if objToCheck.x <= 58:
                    objToCheck.x = 265
                #Compare the x coordinate of the object to the right side of the board.
                elif objToCheck.x >= 265:
                    objToCheck.x = 58
                return True
        return False


    def eatDot(self, playerTile):
        #Use the playerTile tuple to access the relevent tile, and look at it's value for whether there is a PacDot there.
        if self.tiles[playerTile[0]][playerTile[1]][1]:
            canMove = self.tiles[playerTile[0]][playerTile[1]][0]
            self.tiles[playerTile[0]][playerTile[1]] = (canMove, False)
            return True
        else:
            return False


    def eatPellet(self, playerTile):
        for pellet in range(len(self.pelletList)):
            if playerTile == self.pelletList[pellet][0]:
                del self.pelletList[pellet]
                return True
        return False


    def checkTileCentre(self, objx, objy):
        #Calculate the distance of the object from the 4x4 centre of a tile.
        tilePosx = (objx - 50) % 8
        tilePosy = (objy - 47) % 8

        #Check if the object is within the centre.
        if tilePosx < 5 and tilePosy < 5:
            return True
        else:
            return False


    def checkJunction(self, tile):
        #Check if there is a junction based on whether there is at least one tile free both horizontally and vertically.
        #Create an array for the tiles that are available in the order up, left, down, right (priority order).
        availableTiles = [None, None, None, None]

        #Check if a tile above or below can be moved to.
        if self.tiles[tile[0] - 1][tile[1]][0] or self.tiles[tile[0] + 1][tile[1]][0]:
            #Check if a tile left or right can be moved to.
            if self.tiles[tile[0]][tile[1] - 1][0] or self.tiles[tile[0]][tile[1] + 1][0]:
                #Update the values in the array according to whether each tile can be moved to.
                #Upwards checks for some hard coded values the ghosts cannot turn into.
                if self.tiles[tile[0] - 1][tile[1]][0] and tile[0] != 11 and not (tile[0] == 23 and 11 < tile[1] < 17):
                    availableTiles[0] = (tile[0] - 1, tile[1])
                if self.tiles[tile[0]][tile[1] - 1][0]:
                    availableTiles[1] = (tile[0], tile[1] - 1)
                if self.tiles[tile[0] + 1][tile[1]][0]:
                    availableTiles[2] = (tile[0] + 1, tile[1])
                if self.tiles[tile[0]][tile[1] + 1][0]:
                    availableTiles[3] = (tile[0], tile[1] + 1)
                return (True, availableTiles)

        return (False, availableTiles)
