from colorama import init, Fore 

init()


#class for all objects that are printed in the terminal
class Objects:
    def __init__(self, xcor, ycor, xvel = 0, yvel = 0, sprite = None, colour = Fore.WHITE):
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = xvel
        self.yvel = yvel
        self.sprite = sprite
        self.colour = colour
        self.multiplier = 2
        
    def getloc(self):
        return self.xcor, self.ycor
    
    def getsprite(self):
        return self.colour + self.sprite
        
    def setloc(self, x, y):
        self.xcor = x
        self.ycor = y
        
        
#class for the paddle inherited fron Object
class Paddle(Objects):
    def __init__(self, xcor, ycor, width, xvel = 0, yvel = 0, sprite = "▒", colour = Fore.GREEN):
        super().__init__(xcor, ycor, xvel, yvel, sprite, colour)
        self.height = 1
        self.width = width
        
    def getpaddledetails(self):
        return self.width, self.height
        
        
    # function to change coordinates based on keystrokes    
    def paddlemovement(self, keystroke):
        self.xvel = 1
        if keystroke == 'a' or keystroke == 'A':
            self.xcor = self.xcor - self.xvel*self.multiplier
        if keystroke == 'd' or keystroke == 'D':
            self.xcor = self.xcor + self.xvel*self.multiplier
            
        
        
#class foe all the balls inherited from Object
class Ball(Objects):
    def __init__(self, xcor, ycor, xvel = 0, yvel = 0, radius= None, sprite = "⬤", colour = Fore.WHITE):
        super().__init__(xcor, ycor, xvel, yvel, sprite, colour)
        self.radius = radius
        self.vel = 0
        self.Nd = 0
        self.Ed = 0
        self.NEd = 0
        self.SEd = 0

        
    def setvel(self, velocity):
        self.vel = velocity
        
    def setdir(self, a, b, c, d):
        self.Nd = a
        self.Ed = b
        self.NEd = c
        self.SEd = d

    def getvel(self):
        return self.vel, self.Nd, self.Ed, self.NEd, self.SEd