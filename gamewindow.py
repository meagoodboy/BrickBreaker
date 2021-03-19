import os
import time
from colorama import init, Fore
from objects import Objects

init()


def converttochar(number):
    if number == 0:
        return '0'
    elif number == 1:
        return '1'
    elif number == 2:
        return '2'
    elif number == 3:
        return '3'
    elif number == 4:
        return '4'
    elif number == 5:
        return '5'
    elif number == 6:
        return '6'
    elif number == 7:
        return '7'   
    elif number == 8:
        return '8'
    elif number == 9:
        return '9'
    




# A class for the game window
class Window:
    def __init__(self):
        terminal_dimentions = os.get_terminal_size()
        self.height = terminal_dimentions.lines - 4
        self.width = terminal_dimentions.columns
        self.ball = None
        self.paddle = None
        if self.height > 40:
            self.height = 40
        if self.width > 140:
            self.width = 140
        
        
        
        
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
            
                        
        self.Board[2][5] = Objects(0,0,0,0,'L',Fore.GREEN)
        self.Board[2][6] = Objects(0,0,0,0,'E',Fore.GREEN)
        self.Board[2][7] = Objects(0,0,0,0,'V',Fore.GREEN)
        self.Board[2][8] = Objects(0,0,0,0,'E',Fore.GREEN)
        self.Board[2][9] = Objects(0,0,0,0,'L',Fore.GREEN)
        self.Board[2][10] = Objects(0,0,0,0,':',Fore.GREEN)    
             
        
        self.Board[2][25] = Objects(0,0,0,0,'L',Fore.GREEN)
        self.Board[2][26] = Objects(0,0,0,0,'I',Fore.GREEN)
        self.Board[2][27] = Objects(0,0,0,0,'V',Fore.GREEN)
        self.Board[2][28] = Objects(0,0,0,0,'E',Fore.GREEN)
        self.Board[2][29] = Objects(0,0,0,0,'S',Fore.GREEN)
        self.Board[2][30] = Objects(0,0,0,0,':',Fore.GREEN)
        
        
        self.Board[2][45] = Objects(0,0,0,0,'T',Fore.GREEN)
        self.Board[2][46] = Objects(0,0,0,0,'I',Fore.GREEN)
        self.Board[2][47] = Objects(0,0,0,0,'M',Fore.GREEN)
        self.Board[2][48] = Objects(0,0,0,0,'E',Fore.GREEN)
        self.Board[2][49] = Objects(0,0,0,0,':',Fore.GREEN)
        self.Board[2][50] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][51] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][52] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][53] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][54] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][55] = Objects(0,0,0,0,'0',Fore.GREEN)
        
        
        self.Board[2][95] = Objects(0,0,0,0,'S',Fore.GREEN)
        self.Board[2][96] = Objects(0,0,0,0,'C',Fore.GREEN)
        self.Board[2][97] = Objects(0,0,0,0,'O',Fore.GREEN)
        self.Board[2][98] = Objects(0,0,0,0,'R',Fore.GREEN)
        self.Board[2][99] = Objects(0,0,0,0,'E',Fore.GREEN)
        self.Board[2][100] = Objects(0,0,0,0,':',Fore.GREEN)
        self.Board[2][101] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][102] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][103] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][104] = Objects(0,0,0,0,'0',Fore.GREEN)
        self.Board[2][105] = Objects(0,0,0,0,'0',Fore.GREEN)
        
        
                       
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
        xv, yv = Item.getvel()
        
        self.Board[y][x] = Item
        
        
    def getboard(self):
        return self.Board
    
    def addbricktoboard(self, Item):
        x,y = Item.getloc()
        # width = 8 for a standard brick
        Item.setcolour()
        for i in range(0,8,1):            
            self.Board[y][x + i] = Item
            
    def addpoweruptoboard(self, Item):
        x,y = Item.getloc()
        if y > self.height - 4:
            pass
        else:
            self.Board[y][x] = Item
        
    def modifytime(self, time):
        a = time % 10
        time = int(time/10)
        b = time % 10
        time = int(time/10)
        c = time % 10
        time = int(time/10)
        d = time % 10
        time = int(time/10)
        e = time % 10
        
        a = converttochar(a)
        b = converttochar(b)
        c = converttochar(c)
        d = converttochar(d)
        e = converttochar(e)
        
        self.Board[2][51] = Objects(0,0,0,0,e,Fore.GREEN)
        self.Board[2][52] = Objects(0,0,0,0,d,Fore.GREEN)
        self.Board[2][53] = Objects(0,0,0,0,c,Fore.GREEN)
        self.Board[2][54] = Objects(0,0,0,0,b,Fore.GREEN)
        self.Board[2][55] = Objects(0,0,0,0,a,Fore.GREEN)
    #2, 50- 55
    
    def modifyscore(self, score):
        a = score % 10
        score= int(score/10)
        b = score % 10
        score= int(score/10)
        c = score % 10
        score= int(score/10)
        d = score % 10
        score= int(score/10)
        e = score % 10
        
        a = converttochar(a)
        b = converttochar(b)
        c = converttochar(c)
        d = converttochar(d)
        e = converttochar(e)
        
        self.Board[2][101] = Objects(0,0,0,0,e,Fore.GREEN)
        self.Board[2][102] = Objects(0,0,0,0,d,Fore.GREEN)
        self.Board[2][103] = Objects(0,0,0,0,c,Fore.GREEN)
        self.Board[2][104] = Objects(0,0,0,0,b,Fore.GREEN)
        self.Board[2][105] = Objects(0,0,0,0,a,Fore.GREEN)
    #2, 101 -105
    
    
    def modifylevel(self, level):
        lvl = converttochar(level)
        
        
        self.Board[2][11] = Objects(0,0,0,0,lvl,Fore.GREEN)
        #2,11
    
    def modifylives(self, lives):
        liv = converttochar(lives)
        
        
        self.Board[2][31] = Objects(0,0,0,0,liv,Fore.GREEN)
        #2,31
    def modifytest(self, test):
        tes = converttochar(test)
        self.Board[2][110] = Objects(0,0,0,0,tes,Fore.GREEN)
        
    
    def addbosstoboard(self, item):
        bx, by = item.getloc()
        # self.Board[by + 0][bx + 0] = item
        # self.Board[by + 1][bx + 0] = item
        # self.Board[by + 2][bx + 0] = item
        # self.Board[by + 3][bx + 0] = item
        self.Board[by + 4][bx + 0] = item
        # self.Board[by + 5][bx + 0] = item
        # self.Board[by + 6][bx + 0] = item
        # self.Board[by + 0][bx + 1] = item
        # self.Board[by + 1][bx + 1] = item
        # self.Board[by + 2][bx + 1] = item
        # self.Board[by + 3][bx + 1] = item
        self.Board[by + 4][bx + 1] = item
        # self.Board[by + 5][bx + 1] = item
        # self.Board[by + 6][bx + 1] = item
        # self.Board[by + 0][bx + 2] = item
        # self.Board[by + 1][bx + 2] = item
        # self.Board[by + 2][bx + 2] = item
        # self.Board[by + 3][bx + 2] = item
        self.Board[by + 4][bx + 2] = item
        # self.Board[by + 5][bx + 2] = item
        # self.Board[by + 6][bx + 2] = item
        # self.Board[by + 0][bx + 3] = item
        # self.Board[by + 1][bx + 3] = item
        # self.Board[by + 2][bx + 3] = item
        self.Board[by + 3][bx + 3] = item
        self.Board[by + 4][bx + 3] = item
        self.Board[by + 5][bx + 3] = item
        # self.Board[by + 6][bx + 3] = item
        # self.Board[by + 0][bx + 4] = item
        # self.Board[by + 1][bx + 4] = item
        # self.Board[by + 2][bx + 4] = item
        self.Board[by + 3][bx + 4] = item
        self.Board[by + 4][bx + 4] = item
        self.Board[by + 5][bx + 4] = item
        # self.Board[by + 6][bx + 4] = item
        # self.Board[by + 0][bx + 5] = item
        # self.Board[by + 1][bx + 5] = item
        self.Board[by + 2][bx + 5] = item
        self.Board[by + 3][bx + 5] = item
        self.Board[by + 4][bx + 5] = item
        self.Board[by + 5][bx + 5] = item
        self.Board[by + 6][bx + 5] = item
        # self.Board[by + 0][bx + 6] = item
        # self.Board[by + 1][bx + 6] = item
        self.Board[by + 2][bx + 6] = item
        self.Board[by + 3][bx + 6] = item
        self.Board[by + 4][bx + 6] = item
        self.Board[by + 5][bx + 6] = item
        self.Board[by + 6][bx + 6] = item
        # self.Board[by + 0][bx + 7] = item
        self.Board[by + 1][bx + 7] = item
        self.Board[by + 2][bx + 7] = item
        self.Board[by + 3][bx + 7] = item
        self.Board[by + 4][bx + 7] = item
        self.Board[by + 5][bx + 7] = item
        self.Board[by + 6][bx + 7] = item
        self.Board[by + 0][bx + 8] = item
        self.Board[by + 1][bx + 8] = item
        # self.Board[by + 2][bx + 8] = item
        # self.Board[by + 3][bx + 8] = item
        self.Board[by + 4][bx + 8] = item
        self.Board[by + 5][bx + 8] = item
        self.Board[by + 6][bx + 8] = item
        self.Board[by + 0][bx + 9] = item
        self.Board[by + 1][bx + 9] = item
        # self.Board[by + 2][bx + 9] = item
        # self.Board[by + 3][bx + 9] = item
        self.Board[by + 4][bx + 9] = item
        self.Board[by + 5][bx + 9] = item
        # self.Board[by + 6][bx + 9] = item
        self.Board[by + 0][bx + 10] = item
        self.Board[by + 1][bx + 10] = item
        # self.Board[by + 2][bx + 10] = item
        # self.Board[by + 3][bx + 10] = item
        self.Board[by + 4][bx + 10] = item
        self.Board[by + 5][bx + 10] = item
        self.Board[by + 6][bx + 10] = item
        # self.Board[by + 0][bx + 11] = item
        self.Board[by + 1][bx + 11] = item
        self.Board[by + 2][bx + 11] = item
        self.Board[by + 3][bx + 11] = item
        self.Board[by + 4][bx + 11] = item
        self.Board[by + 5][bx + 11] = item
        self.Board[by + 6][bx + 11] = item
        # self.Board[by + 0][bx + 12] = item
        # self.Board[by + 1][bx + 12] = item
        self.Board[by + 2][bx + 12] = item
        self.Board[by + 3][bx + 12] = item
        self.Board[by + 4][bx + 12] = item
        self.Board[by + 5][bx + 12] = item
        self.Board[by + 6][bx + 12] = item
        # self.Board[by + 0][bx + 13] = item
        # self.Board[by + 1][bx + 13] = item
        self.Board[by + 2][bx + 13] = item
        self.Board[by + 3][bx + 13] = item
        self.Board[by + 4][bx + 13] = item
        self.Board[by + 5][bx + 13] = item
        self.Board[by + 6][bx + 13] = item
        # self.Board[by + 0][bx + 14] = item
        # self.Board[by + 1][bx + 14] = item
        # self.Board[by + 2][bx + 14] = item
        self.Board[by + 3][bx + 14] = item
        self.Board[by + 4][bx + 14] = item
        self.Board[by + 5][bx + 14] = item
        # self.Board[by + 6][bx + 14] = item
        # self.Board[by + 0][bx + 15] = item
        # self.Board[by + 1][bx + 15] = item
        # self.Board[by + 2][bx + 15] = item
        self.Board[by + 3][bx + 15] = item
        self.Board[by + 4][bx + 15] = item
        self.Board[by + 5][bx + 15] = item
        # self.Board[by + 6][bx + 15] = item
        # self.Board[by + 0][bx + 16] = item
        # self.Board[by + 1][bx + 16] = item
        # self.Board[by + 2][bx + 16] = item
        # self.Board[by + 3][bx + 16] = item
        self.Board[by + 4][bx + 16] = item
        # self.Board[by + 5][bx + 16] = item
        # self.Board[by + 6][bx + 16] = item
        # self.Board[by + 0][bx + 17] = item
        # self.Board[by + 1][bx + 17] = item
        # self.Board[by + 2][bx + 17] = item
        # self.Board[by + 3][bx + 17] = item
        self.Board[by + 4][bx + 17] = item
        # self.Board[by + 5][bx + 17] = item
        # self.Board[by + 6][bx + 17] = item
        # self.Board[by + 0][bx + 18] = item
        # self.Board[by + 1][bx + 18] = item
        # self.Board[by + 2][bx + 18] = item
        # self.Board[by + 3][bx + 18] = item
        self.Board[by + 4][bx + 18] = item
        # self.Board[by + 5][bx + 18] = item
        # self.Board[by + 6][bx + 18] = item
        
       

    def addbullettoboard(self, item):
        bx, by = item.getloc()
        self.Board[by][bx] = Objects(0,0,0,0,'O',Fore.GREEN)