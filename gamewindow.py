import os
from colorama import init, Fore
from objects import Objects

init()

# A class for the game window
class Window:
    def __init__(self):
        terminal_dimentions = os.get_terminal_size()
        self.height = terminal_dimentions.lines -1
        self.width = terminal_dimentions.columns
        self.ball = None
        self.paddle = None
        
    def initgameborder(self):
        self.Board = [[None for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width - 1 or j == 2 or j == self.width - 3:
                    self.Board[i][j] = '┃'

                if i == 0:
                    if j == 0:
                        self.Board[i][j] = '┏'
                    elif j == self.width - 1:
                        self.Board[i][j] = '┓'
                    else:
                        self.Board[i][j] = '━'

                if i == self.height - 1:
                    if j == 0:
                        self.Board[i][j] = '┗'
                    elif j == self.width - 1:
                        self.Board[i][j] = '┛'
                    else:
                        self.Board[i][j] = '━'
                        
                if i == 1:
                    if j == 2:
                        self.Board[i][j] = '┏'
                    elif j == self.width - 3:
                        self.Board[i][j] = '┓'
                    elif j == 1 or j == self.width-2:
                        pass
                    elif j == 0 or j == self.width -1:
                        pass
                    else:
                        self.Board[i][j] = '━'
                        
                if i == self.height - 2:
                    if j == 2:
                        self.Board[i][j] = '┗'
                    elif j == self.width - 3:
                        self.Board[i][j] = '┛'
                    elif j == 1 or j == self.width-2:
                        pass
                    elif j == 0 or j == self.width -1:
                        pass
                    else:
                        self.Board[i][j] = '━'
                        
                        
    def rendergameborder(self):
        for i in range(self.height):
                for j in range(self.width):

                    if(self.Board[i][j] != None):
                        pixel = self.Board[i][j]

                        print(pixel, sep="", end="")

                    else:
                        pixel = ' '
                        print(pixel, sep="", end="")

                print()
        