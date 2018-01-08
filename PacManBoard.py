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

    def checkValidPosition(self, objx, objy):

    def checkTunnel(self, objToCheck):
        #Check if a ghost or the player has passed through a tunnel to the other side of the board.

    def eatDots(self, playerx, playery):
