import random
import copy


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

        #For each of the features passed in.
        for i in range(len(features)):
            #Update the Q-Value based on the feature's weighting.
            newQVal += features[i] * self.weights[i]

            #Keep the update if the Q-Value has not rounded to infinity or negative infinity, to avoid errors.
            if float('-Inf') < float(newQVal) < float('Inf'):
                QVal = newQVal

        #Return the calculated value.
        return QVal


    def updateWeights(self, score, state, newActions):
        #Check the agent has changed state before updating the weights.
        if state[0] != self.currentTile:
            #Calculate the amount the score changed from the action just taken.
            reward = score - self.startScore
            maxVal = float('-Inf')

            #Loop through each possible action from the new state, and find the maximum expected utility.
            for action in newActions:
                stateFeatures = self.generateFeatures(state, action)
                QVal = self.calculateQValue(stateFeatures)
                if QVal > maxVal:
                    maxVal = QVal

            #Calculate the difference between the expected gain and the actual gain from that action.
            difference = reward + self.gamma * maxVal - self.expectedVal

            #Update the weights according to the value the feature had during this action and the difference in reward.
            for i in range(len(self.currentFeatures)):
                self.weights[i] = self.weights[i] + self.alpha * self.currentFeatures[i] * difference

        #Decrease the value of alpha to slow learning over time.
        self.alpha *= 0.99


    def generateMove(self, state, possibleActions):
        #Check the agent has changed state since the last move generation.
        if state[0] != self.currentTile:
            #Extract required information from the state.
            self.currentTile = state[0]
            self.currentAction = None
            self.currentFeatures = []

            #Generate a random float between 0 and 1 to decide whether to explore or follow the best known policy.
            exploreChance = random.uniform(0,1)

            #If the float is above the agent's explore value, follow the best policy.
            if exploreChance >= self.epsilon:
                self.expectedVal = float('-Inf')

                #Loop through the possible actions and store the one with the highest Q-Value.
                for action in possibleActions:
                    stateFeatures = self.generateFeatures(state, action)
                    QVal = self.calculateQValue(stateFeatures)
                    if QVal > self.expectedVal:
                        self.currentAction = action
                        self.currentFeatures = stateFeatures
                        self.expectedVal = QVal

            #Otherwise choose a random action from those possible.
            else:
                actionNo = random.randint(0, len(possibleActions) - 1)
                self.currentAction = possibleActions[actionNo]
                self.currentFeatures = self.generateFeatures(state, self.currentAction)
                self.expectedVal = self.calculateQValue(self.currentFeatures)

        return self.currentAction


    def generateFeatures(self, state, action):
        stateFeatures = []
        playerTile = state[0]
        nextTile = self.destinationTile(playerTile, action)
        #Calculate the shortest distance to a Pac-Dot.
        dotDist = self.closestDot(state, action)
        stateFeatures.append(dotDist)

        #Loop through each ghost in chase mode and calculate their distance to the destination.
        for ghostPos in state[1]:
            if ghostPos:
                ghostDist = self.calculateDistance(nextTile, ghostPos)
                stateFeatures.append(ghostDist)

        #Return the features to calculate the Q-Value.
        return stateFeatures


    def destinationTile(self, playerTile, direction):
        #Calculate the tile being moved to based on the direction.
        if direction == "right":
            return (playerTile[0] + 1, playerTile[1])
        elif direction == "left":
            return (playerTile[0] - 1, playerTile[1])
        elif direction == "up":
            return (playerTile[0], playerTile[1] - 1)
        else:
            return (playerTile[0], playerTile[1] + 1)


    def calculateDistance(self, tile1, tile2):
        #If the second tile does not exist, set the distance to 0.
        if tile2 == None:
            distance = 0
        else:
            #Calculate the distance between two board tiles using pythagoras.
            xdist = abs(tile1[0] - tile2[0])
            ydist = abs(tile1[1] - tile2[1])
            distance = (xdist ** 2 + ydist ** 2) ** 0.5
        return distance


    def recordScore(self, score):
        #Updates the stored score attribute.
        self.startScore = score


    def closestDot(self, state, action):
        #Calls a breadth first search from the destination tile to get the distance to the closest dot.
        tile = self.destinationTile(state[0], action)
        board = state[3]
        closestDepth = self.breadthFirstSearch(tile, board, 3)
        return closestDepth


    def breadthFirstSearch(self, tile, boardTiles, maxDepth):
        #Create a circular queue object to manage the positions to explore.
        fringe = CircularQueue()
        #Store a list of the positions that have been explored already.
        explored = []
        #Copy the state of the board to search through.
        grid = copy.deepcopy(boardTiles)
        #Store the tile and depth currently being searched from.
        currentTile = tile
        currentDepth = 0

        #Loop as long as a dot has not been found and the maximum depth has not been exceeded.
        while not grid[currentTile[0]][currentTile[1]][1] and currentDepth < maxDepth:
            #Add the current tile to the fringe.
            explored.append(currentTile)
            #Check the tile in each possible direction from the current one.
            for direction in DIRECTIONS:
                nextTile = self.destinationTile(currentTile, direction)

                #Check that tile being considered is within the grid.
                if nextTile[0] < len(grid) and nextTile[1] < len(grid[0]):
                    #Check the tile being considered can be moved to and has not been considered already.
                    if grid[nextTile[0]][nextTile[1]][0] and not nextTile in explored:
                        #Add the tile to the queue with its associated depth.
                        fringe.enQueue((nextTile, currentDepth + 1))
            #Get the next tile to consider and its associated depth from the queue.
            currentTile, currentDepth = fringe.deQueue()

        #Return the depth of the first dot.
        return currentDepth



class CircularQueue():
    def __init__(self):
        #Create the queue as an empty array of size 30.
        self.currentSize = 0
        self.maxSize = 30
        self.queue = []

        for i in range(self.maxSize):
            self.queue.append(None)

        #Set the front of the queue to the first element in the array, so elements will be removed from here.
        self.front = 0
        #Set the rear of the queue to -1 so elements will be removed from the front.
        self.rear = -1
        #Set the size of the queue to 0 to show it is empty.
        self.size = 0


    def enQueue(self, item):
        #Check there is space to add an item to.
        if not self.isFull():
            #Move the rear of the queue backwards so items will be added to the end. If the rear goes past the end, circle back to the front.
            self.rear += 1
            self.rear %= self.maxSize
            #Add the new item to the end of the queue.
            self.queue[self.rear] = item
            #Increase the current size of the list.
            self.size += 1
        else:
            print("Queue full, item not added.")


    def deQueue(self):
        #Check there is an item to take from the queue.
        if not self.isEmpty():
            #Store the item at the front of the queue.
            item = self.queue[self.front]
            #Move the front of the queue backwards one item, and circle back to the start if it goes past the end.
            self.front += 1
            self.front %= self.maxSize
            #Decrease the current size of the list.
            self.size -= 1
            return item
        else:
            print("Nothing to return")

    def isEmpty(self):
        #Check if the number of elements in the list is currently 0.
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self):
        #Check if the number of elements in the list is currently the maximum available.
        if self.size == self.maxSize:
            return True
        else:
            return False
