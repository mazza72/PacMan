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
        """Testing"""
        difficultySelector = QInputDialog(self)
        something, easy = difficultySelector.getText(self, 'Difficulty selection', 'Select desired difficulty')
        game = PacManEngine.PacManEngine()
        score = game.playLevels()
        """Add a dialog with an easy/hard selection to launch the engine with more lives"""
        name, ok = QInputDialog.getText(self, 'ScoreForm',
            'Enter your name to store your score:')

        if ok:
            with open("playerHighscores.txt", 'a') as f:
                """Run binary search to insert the score?"""
                f.write(name + ',' + str(score) + "\n")

    def AIPlayer(self):
        game = PacManEngine.PacManEngine()
        game.playLevels(False)

    def displayScores(self):
        self.AIBtn.hide()
        self.scoresScreen.show()
        """Load second window? or dialog to display scores"""

class ScoreDisplay(QWidget):
    def __init__(self):
        #Initialise the Q Widget itself.
        super().__init__()

        #Set the layout of the menu with 10 pixels between widgets.
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        self.inputTest = QLineEdit(self)
        self.grid.addWidget(self.inputTest, 0, 0, 2, 10)
        self.inputTest.textChanged[str].connect(self.textChange)

        self.playerBtn = QPushButton("1 Player", self)
        self.grid.addWidget(self.playerBtn, 3, 3, 2, 4)
        self.AIBtn = QPushButton("AI", self)
        self.grid.addWidget(self.AIBtn, 6, 3, 2, 4)
        self.HiScoresBtn = QPushButton("High Scores", self)
        self.grid.addWidget(self.HiScoresBtn, 9, 3, 2, 4)

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
                        "QLineEdit { border-style: outset;"
                        "border-width: 2px;"
                        "border-radius: 10px;"
                        "border-color: blue;"
                        "font: bold 30px;"
                        "color: blue;"
                        "min-width: 10em;"
                        "padding: 6px; "
                        "height: 50px}"
                        "QWidget {background-color: black; }")

        #Make it so the menu is created at coordinates (300,300) with a length of 1000 and width of 1200.
        self.setGeometry(500, 500, 500, 600)
        self.setWindowTitle('Second window')

    def textChange(self):
        print("Text changed", self.inputTest.text())

def runMenu():
    #Create an application object for pyQt5.
    app = QApplication(sys.argv)
    menu = MainMenu()
    #This ends the application if the user closes the window.
    sys.exit(app.exec_())
