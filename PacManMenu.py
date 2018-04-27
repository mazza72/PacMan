"""Creates the interface for the user to use."""
#import the required files.
import PacManEngine

#Import the required modules for the program to run.
import sys

#Import the required parts of the PyQt module for the menu.
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainMenu(QWidget):

    def __init__(self):
        #Initialise the Q Widget itself.
        super().__init__()

        #Load the main menu screen.
        #Set the layout of the menu with 10 pixels between widgets.
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        #Create a label with a centred picture for the title.
        self.titleLabel = QLabel(self)
        self.logoPic = QPixmap('PacManLogo.png')
        self.titleLabel.setPixmap(self.logoPic)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.titleLabel, 0, 0, 2, 10)

        #Create 3 buttons with connected functions to allow the user to select the option they want to use.
        self.playerBtn = QPushButton("1 Player", self)
        self.playerBtn.clicked.connect(self.onePlayer)
        self.grid.addWidget(self.playerBtn, 3, 3, 2, 4)
        self.AIBtn = QPushButton("AI", self)
        self.AIBtn.clicked.connect(self.AIPlayer)
        self.grid.addWidget(self.AIBtn, 6, 3, 2, 4)
        self.HiScoresBtn = QPushButton("High Scores", self)
        self.grid.addWidget(self.HiScoresBtn, 9, 3, 2, 4)
        self.HiScoresBtn.clicked.connect(self.displayScores)

        #Use a style sheet in order to set the aesthetics of the menu, including attributes such as text size and border colour.
        self.setStyleSheet("QPushButton { border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: blue;"
                        "font: bold 30px;"
                        "color: blue;"
                        "min-width: 10em;"
                        "padding: 6px; "
                        "height: 50px}"
                        "QLineEdit { border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: blue;"
                        "font: bold 30px;"
                        "color: blue;"
                        "min-width: 10em;"
                        "padding: 6px; "
                        "height: 50px}"
                        "QLabel { font: bold 35px;"
                        "color: blue;"
                        "min-width: 10em;"
                        "padding: 6px; "
                        "height: 50px}"
                        "QWidget {background-color: black; }")

        self.scoresScreen = ScoreDisplay()

        #Make it so the menu is created at coordinates (300,300) with a length of 1000 and width of 1200.
        self.setGeometry(300, 300, 1000, 1200)
        self.setWindowTitle('Pac-Man Demonstration')
        #Display the widgets on the screen.
        self.show()

    def onePlayer(self):
        #Initialise PacMan within the PacMan Engine file.
        game = PacManEngine.PacManEngine()
        score = game.playLevels()
        name, ok = QInputDialog.getText(self, 'ScoreForm',
            'Enter your name to store your score:')

        #See if the player wants to save their score.
        if ok:
            currentScores = []
            newScores = currentScores

            #If the scores file exists open it
            try:
                with open("playerHighscores.txt", 'r') as f:

                    #Split the saved lines into 2 element lists by splitting at the comma.
                    for line in f:
                        record = line.split(',')
                        record[1] = int(record[1])
                        currentScores.append(record)

                    #Loop through the loaded scores and see if the player has done better.
                    newScores = currentScores
                    for i in range(len(currentScores)):

                        if score > int(currentScores[i][1]):

                            #If the player has done better insert their score into the appropriate place in the list.
                            if i > 0:
                                newScores = currentScores[::i]
                            else:
                                newScores = []

                            newScores.append([name, score])
                            #Loop through the remaining stored scores, leaving out the last one.
                            for j in range(len(currentScores) - i - 1):
                                newScores.append(currentScores[i+j])
                            #Stop comparing the new score, since we know it will be bigger than the rest from this point.
                            break

            #If the scores file does not exist create a set of placeholder scores to store.
            except FileNotFoundError:
                print("Creating new scores file")
                newScores = [[name, score]]
                for i in range(4):
                    newScores.append(("PlaceHolder", 0))

            #Check if the scores have changed or a new file needs to be created.
            if newScores != currentScores or currentScores == []:
                with open("playerHighscores.txt", 'w') as f:
                    #Write out scores to the file, with each score on a new line.
                    for line in newScores:
                        f.write(str(line[0]) + ', ' + str(line[1]) + '\n')

    def AIPlayer(self):
        #Launch the PacMan engine without a player.
        game = PacManEngine.PacManEngine()
        game.playLevels(False)

    def displayScores(self):
        #Displays the second screen after updating the scores.
        self.scoresScreen.getScores()
        self.scoresScreen.show()

class ScoreDisplay(QWidget):
    def __init__(self):
        #Initialise the Q Widget itself.
        super().__init__()
        self.getScores()

        #Set the layout of the menu with 10 pixels between widgets.
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        #Create the button to hide the second screen again.
        self.playerBtn = QPushButton("Back", self)
        self.grid.addWidget(self.playerBtn, 12, 3, 2, 4)
        self.playerBtn.clicked.connect(self.hideWindow)

        #Create 5 labels from the saved list of scores and add them to the screen.
        self.scoreLabel1 = QLabel(self.currentScores[0], self)
        self.grid.addWidget(self.scoreLabel1, 0, 3, 2, 4)
        self.scoreLabel2 = QLabel(self.currentScores[1], self)
        self.grid.addWidget(self.scoreLabel2, 2, 3, 2, 4)
        self.scoreLabel3 = QLabel(self.currentScores[2], self)
        self.grid.addWidget(self.scoreLabel3, 4, 3, 2, 4)
        self.scoreLabel4 = QLabel(self.currentScores[3], self)
        self.grid.addWidget(self.scoreLabel4, 6, 3, 2, 4)
        self.scoreLabel5 = QLabel(self.currentScores[4], self)
        self.grid.addWidget(self.scoreLabel5, 8, 3, 2, 4)

        #Use a style sheet in order to set the aesthetics of the menu, including attributes such as text size and border colour.
        self.setStyleSheet("QPushButton { border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: blue;"
                        "font: bold 30px;"
                        "color: blue;"
                        "min-width: 10em;"
                        "padding: 6px; "
                        "height: 50px}"
                        "QLabel { font: bold 35px;"
                        "color: blue;"
                        "min-width: 10em;"
                        "padding: 6px; "
                        "height: 50px}"
                        "QWidget {background-color: black; }")

        #Make it so the menu is created at coordinates (300,300) with a length of 1000 and width of 1200.
        self.setGeometry(500, 500, 500, 600)
        self.setWindowTitle('Pac-Man Scores')


    def hideWindow(self):
        self.hide()

    def getScores(self):
        #If the file exists, open it and retrieve the scores.
        try:
            self.currentScores = []
            with open("playerHighscores.txt", 'r') as f:
                for line in f:
                    self.currentScores.append(line)

                #If there are fewer than 5 scores add placeholder scores as required.
                if len(self.currentScores) < 5:
                    for i in range(5-len(self.currentScores)):
                        self.currentScores.append("PlaceHolder, 0")

        #If the file doesn't exist load empty strings to show.
        except FileNotFoundError:
            self.currentScores = ['','','','','']


def runMenu():
    #Create an application object for pyQt5.
    app = QApplication(sys.argv)
    menu = MainMenu()
    #This ends the application if the user closes the window.
    sys.exit(app.exec_())
