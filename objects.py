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
        
        
#class for the paddle inherited fron Object
class Paddle(Objects):
    def __init__(self, xcor, ycor, height,  width, xvel = 0, yvel = 0, sprite = None, colour = Fore.WHITE):
        super().__init__(self, xcor, ycor, xvel, yvel, sprite, colour)
        self.height = height
        self.width = width
        
        
        
#class foe all the balls inherited from Object
class Ball(Objects):
    def __init__(self, xcor, ycor, radius, xvel = 0, yvel = 0, sprite = None, colour = Fore.WHITE):
        super().__init__(self, xcor, ycor, xvel, yvel, sprite, colour)
        self.radius = radius
