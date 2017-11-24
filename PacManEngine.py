"""Brings together the components of the game and allows functionality"""

#import required files
import PacManBoard
import PacManGraphics

#import required modules
import sys, pygame

class PacMan:
    def __init__(self):
        self.board = PacManBoard.Board()

        #Setup pygame
        pygame.init()
        pygame.font.init()

        #Call the graphics function that creates the window and font.
        self.display, self.font, self.background = PacManGraphics.setup()

    def gameloop(self):
        PacManGraphics.drawboard(self.display, self.background)

        #get the events that have occurred.
        events = PacManGraphics.getEvents()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)