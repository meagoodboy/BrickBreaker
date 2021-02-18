import os
from colorama import init, Fore
from objects import Objects

init()

# A class for the game window
class Window:
    def __init__(self):
        terminal_dimentions = os.get_terminal_size()
        self.height = terminal_dimentions.lines - 4
        self.width = terminal_dimentions.columns
        self.ball = None
        self.paddle = None
        
    def getwindowcor(self):
        return self.width, self.height
        
    def initgameborder(self):
        self.Board = [[None for j in range(self.width)] for i in range(self.height)]
        
        sides = Objects(0,0,0,0,'┃',Fore.BLUE)
        upleft = Objects(0,0,0,0,'┏',Fore.BLUE)
        upright = Objects(0,0,0,0,'┓',Fore.BLUE)
        updown = Objects(0,0,0,0,'━',Fore.BLUE)
        downleft = Objects(0,0,0,0,'┗',Fore.BLUE)
        downright = Objects(0,0,0,0,'┛',Fore.BLUE)
        stars = Objects(0,0,0,0,'*',Fore.RED)
        
        
        
        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width - 1 or j == 2 or j == self.width - 3:
                    self.Board[i][j] = sides

                if i == 0:
                    if j == 0:
                        self.Board[i][j] = upleft
                    elif j == self.width - 1:
                        self.Board[i][j] = upright
                    else:
                        self.Board[i][j] = updown

                if i == self.height - 1:
                    if j == 0:
                        self.Board[i][j] = downleft
                    elif j == self.width - 1:
                        self.Board[i][j] = downright
                    else:
                        self.Board[i][j] = updown
                        
                if i == 1:
                    if j == 2:
                        self.Board[i][j] = upleft
                    elif j == self.width - 3:
                        self.Board[i][j] = upright
                    elif j == 1 or j == self.width-2:
                        pass
                    elif j == 0 or j == self.width -1:
                        pass
                    else:
                        self.Board[i][j] = updown
                        
                if i == self.height - 2:
                    if j == 2:
                        self.Board[i][j] = downleft
                    elif j == self.width - 3:
                        self.Board[i][j] = downright
                    elif j == 1 or j == self.width-2:
                        pass
                    elif j == 0 or j == self.width -1:
                        pass
                    else:
                        self.Board[i][j] = updown
                        
                if i == self.height - 3:
                    if j > 2 and j < self.width-3:
                        self.Board[i][j] = stars
                        
                if i == 3 and ( j > 2 and j < self.width - 3 ):
                    self.Board[i][j] = updown
                        
                        
    def rendergame(self):
        for i in range(self.height):
                for j in range(self.width):

                    if(self.Board[i][j] != None):
                        pixel = self.Board[i][j].getsprite()

                        print(pixel, sep="", end="")

                    else:
                        pixel = ' '
                        print(pixel, sep="", end="")

                print()
                
    def clearinnerboard(self):
        for i in range( 4, self.height - 3):
            for j in range( 3, self.width - 3):
                self.Board[i][j] = None
        
        
                
                
    def addpaddletoboard(self, Item):
        x,y = Item.getloc()
        width, height = Item.getpaddledetails()
        j = self.height - 5
        if x + width > self.width - 3 :
            Item.setloc(self.width - width - 3, y)
            x,y = Item.getloc()
        if x < 3 :
            Item.setloc(3, y)
            x,y = Item.getloc()
            
        for i in range(0,width,1):            
            self.Board[j][x + i] = Item
            
    def addballtoboard(self, Item):
        x,y = Item.getloc()
        self.Board[y][x] = Item
        
        
    def getboard(self):
        return self.Board
        
        