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
        self.multiplier = 1
        
    def getloc(self):
        return self.xcor, self.ycor
    
    def getsprite(self):
        return self.colour + self.sprite
        
        
#class for the paddle inherited fron Object
class Paddle(Objects):
    def __init__(self, xcor, ycor, width, xvel = 0, yvel = 0, sprite = "▒", colour = Fore.WHITE):
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
    def __init__(self, xcor, ycor, radius= None, xvel = 0, yvel = 0, sprite = "⬤", colour = Fore.WHITE):
        super().__init__(self, xcor, ycor, xvel, yvel, sprite, colour)
        self.radius = radius
