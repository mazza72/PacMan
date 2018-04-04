import random
import copy
"""Remove later"""
import sys

DIRECTIONS = ["up", "down", "left", "right"]

class Agent():
    def __init__(self):
        self.weights = []
        for i in range(5):
            self.weights.append(1)
        self.expectedVal = 0
        #How much the agent learns.
        self.alpha = 0.2
        self.startScore = 0
        #The discount value for 'past values'.
        self.gamma = 0.08
        #How much the agent explores.
        self.epsilon = 0.05
        self.currentTile = None
        self.currentAction = None

    def calculateQValue(self, features):
        QVal = 0
        newQVal = 0
        print(self.weights)
        print("Length",len(features))
        for i in range(len(features)):
            newQVal += features[i] * self.weights[i]
            if float('-Inf') < float(newQVal) < float('Inf'):
                QVal = newQVal
        if not float('-Inf') < float(QVal) < float('Inf'):
            print("calculation broke")
            sys.exit()
        return QVal


    def updateWeights(self, score, state, newActions):
        if state[0] != self.currentTile:
            print("updating")
            reward = score - self.startScore
            maxVal = float('-Inf')
            for action in newActions:
                stateFeatures = self.generateFeatures(state, action)
                QVal = self.calculateQValue(stateFeatures)
                print("updating with:", QVal)
                if QVal > maxVal:
                    maxVal = QVal
            print("MaxVal", maxVal)
            if not float('-Inf') < float(maxVal) < float('Inf'):
                print("maxval broke")
                sys.exit()
            difference = reward + self.gamma * maxVal - self.expectedVal
            if not float('-Inf') < float(difference) < float('Inf'):
                print("difference broke")
                print("difference", difference)
                sys.exit()
            print("Difference is:", difference)
            for i in range(len(self.currentFeatures)):
                self.weights[i] = self.weights[i] + self.alpha * self.currentFeatures[i] * difference


    def generateMove(self, state, possibleActions):
        if state[0] != self.currentTile:
            self.currentTile = state[0]
            print(possibleActions)
            self.currentAction = None
            self.currentFeatures = []
            exploreChance = random.uniform(0,1)

            if exploreChance >= self.epsilon:
                self.expectedVal = float('-Inf')
                for action in possibleActions:
                    stateFeatures = self.generateFeatures(state, action)
                    QVal = self.calculateQValue(stateFeatures)
                    print("QVal comparing", QVal)
                    if QVal > self.expectedVal:
                        print("Updating action")
                        self.currentAction = action
                        self.currentFeatures = stateFeatures
                        self.expectedVal = QVal
            else:
                print("Random action")
                actionNo = random.randint(0, len(possibleActions) - 1)
                self.currentAction = possibleActions[actionNo]
                self.currentFeatures = self.generateFeatures(state, self.currentAction)
                self.expectedVal = self.calculateQValue(self.currentFeatures)

        print(self.currentAction)
        return self.currentAction

    def generateFeatures(self, state, action):
        playerTile = state[0]
        stateFeatures = []
        nextTile = self.destinationTile(playerTile, action)
        dotDist = self.closestDot(state, action)
        stateFeatures.append(dotDist)

        """
        blinkyPos = state[1][0]
        if blinkyPos:
            blinkyDist = self.calculateDistance(nextTile, blinkyPos)
        else:
            blinkyDist = 0
        stateFeatures.append(blinkyDist)


        pinkyPos = state[1][0]
        if pinkyPos:
            pinkyDist = self.calculateDistance(nextTile, pinkyPos)
        else:
            pinkyDist = 0
        stateFeatures.append(pinkyDist)"""


        for ghostPos in state[1]:
            if ghostPos:
                ghostDist = self.calculateDistance(nextTile, ghostPos)
                stateFeatures.append(ghostDist)
                if not float('-Inf') < float(ghostDist) < float('Inf'):
                    print("ghosts broke")
                    sys.exit()

        print(stateFeatures)
        return stateFeatures

    def destinationTile(self, playerTile, direction):
        if direction == "right":
            return (playerTile[0] + 1, playerTile[1])
        elif direction == "left":
            return (playerTile[0] - 1, playerTile[1])
        elif direction == "up":
            return (playerTile[0], playerTile[1] - 1)
        else:
            return (playerTile[0], playerTile[1] + 1)

    def calculateDistance(self, tile1, tile2):
        #Calculate the distance between two board tiles using pythagoras.
        xdist = abs(tile1[0] - tile2[0])
        ydist = abs(tile1[1] - tile2[1])
        distance = (xdist ** 2 + ydist ** 2) ** 0.5
        return distance

    def recordScore(self, score):
        self.startScore = score

    def closestDot(self, state, action):
        destinationTile = self.destinationTile(state[0], action)
        tile = self.destinationTile(state[0], action)
        board = state[3]
        closestDepth = self.breadthFirstSearch(tile, board, 5)
        return closestDepth

    def breadthFirstSearch(self, tile, boardTiles, maxDepth):
        fringe = []
        explored = []
        grid = copy.deepcopy(boardTiles)
        currentTile = tile
        currentDepth = 0
        while not grid[currentTile[0]][currentTile[1]][1] and currentDepth < maxDepth:
            explored.append(currentTile)
            for direction in DIRECTIONS:
                nextTile = self.destinationTile(currentTile, direction)
                if nextTile[0] < len(grid) and nextTile[1] < len(grid[0]):
                    if grid[nextTile[0]][nextTile[1]][0] and not nextTile in explored:
                        fringe.append((nextTile, currentDepth + 1))
                        print(fringe)
            currentTile, currentDepth = fringe[0]
            fringe = fringe[1::]
        print(currentDepth)
        return currentDepth
