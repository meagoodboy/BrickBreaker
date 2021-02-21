from colorama import init, Fore 

init()


#class for all objects that are printed in the terminal
class Objects:
    def __init__(self, xcor, ycor, xvel = 0, yvel = 0, sprite = None, colour = Fore.WHITE, idtag = 'O'):
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.sprite = sprite
        self.colour = colour
        self.multiplier = 4
        self.idtag = idtag 
        
    def getloc(self):
        return self.xcor, self.ycor
    
    def getsprite(self):
        return self.colour + self.sprite
        
    def setloc(self, x, y):
        self.xcor = x
        self.ycor = y
        
    def getvel(self):
        return self.xvel, self.yvel
    
    def setvel(self, x, y):
        self.xvel = x
        self.yvel = y
        
        
#class for the paddle inherited fron Object
class Paddle(Objects):
    def __init__(self, xcor, ycor, width, xvel = 0, yvel = 0, sprite = "▒", colour = Fore.GREEN, idtag = 'P'):
        super().__init__(xcor, ycor, xvel, yvel, sprite, colour, idtag)
        self.height = 1
        self.width = width
        
    def getpaddledetails(self):
        return self.width, self.height
        
    def changepaddlewidth(self, newwidth):
        self.width = newwidth
        
    # function to change coordinates based on keystrokes    
    def paddlemovement(self, keystroke):
        self.xvel = 1
        if keystroke == 'a' or keystroke == 'A':
            self.xcor = self.xcor - self.xvel*self.multiplier
        if keystroke == 'd' or keystroke == 'D':
            self.xcor = self.xcor + self.xvel*self.multiplier
            
        
        
#class foe all the balls inherited from Object
class Ball(Objects):
    def __init__(self, xcor, ycor, xvel = 0, yvel = 0, sprite = "⬤", colour = Fore.WHITE):
        super().__init__(xcor, ycor, xvel, yvel, sprite, colour)
        self.power = 0
    
    
    def ballmovement(self):
        self.xcor = self.xcor + self.xvel
        self.ycor = self.ycor + self.yvel
        
    def getpower(self):
        return self.power
    
    def setpower(self, power):
        self.power = power
        
        
        
        
class Brick(Objects):
    def __init__(self, b_id, xcor, ycor, health, bproperty = 'N', xvel = 0, yvel = 0, colour = Fore.WHITE, sprite = "▒", idtag = 'B'):
        super().__init__(xcor, ycor, xvel, yvel, sprite, colour, idtag)
        self.bproperty = bproperty
        self.health = health
        self.b_id = b_id 


    def setcolour(self):
        if self.bproperty == 'N':
            if self.health == 1:
                self.colour = Fore.BLUE
            elif self.health == 2:
                self.colour = Fore.GREEN
            elif self.health == 3:
                self.colour = Fore.CYAN
            elif self.health == 4:
                self.colour = Fore.RED
        elif self.bproperty == 'E':
            self.colour = Fore.LIGHTYELLOW_EX
        elif self.bproperty == 'U':  
            self.colour = Fore.WHITE
        else:
            if self.health == 1:
                self.colour = Fore.LIGHTBLUE_EX
            elif self.health == 2:
                self.colour = Fore.LIGHTGREEN_EX
            elif self.health == 3:
                self.colour = Fore.LIGHTCYAN_EX
            elif self.health == 4:
                self.colour = Fore.LIGHTRED_EX
            


    def diewithahit(self, power):
        if power == 0 and self.bproperty != 'U':
            self.health = self.health - 1
        elif self.bproperty == 'U':
            pass
        else:
            self.health = 0
        
        
        
    def diewithablast():
        pass