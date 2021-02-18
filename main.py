import os
import signal
import sys
from gamewindow import Window
from objects import Objects, Paddle, Ball
from Input import manageinput
from dynamics import collitionball


def alarmHandler(*arg):
    raise Exception




if __name__ == "__main__":
    
    
    
    
    window = Window()
    window.initgameborder()
    wxcor, wycor = window.getwindowcor()
    
    
    paddle = Paddle(int(wxcor/2) - 5, wycor-5, 20, 2, 1)
    ball = Ball(int(wxcor/2), wycor-6, 0, 1)
    ball.setvel( -1, -1)
    # window.addpaddletoboard(paddle)
    # window.rendergame()
    timeout = 0.05
    keyinput = manageinput()
        
        
        
     #   HELP fix fps
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()  
    while True:
        
        try:
            signal.signal(signal.SIGALRM, alarmHandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            
            
            ball.ballmovement()
            collitionball(ball, window)
            #collisionball(ball, window)
            
            window.clearinnerboard()
            window.addpaddletoboard(paddle)
            window.addballtoboard(ball)
            os.system('clear')
            window.rendergame()
            #getting input and filtering them
            
            
            
            
            
            keyinput.filterchar()
            paddle.paddlemovement(keyinput.returninput)
            
            
            
            
            
            if keyinput.returninput == 'X' or keyinput.returninput == 'x':
                break
                
        except :
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            pass