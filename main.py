import os
from gamewindow import Window
from objects import Objects, Paddle
from Input import manageinput

if __name__ == "__main__":
    window = Window()
    window.initgameborder()
    wxcor, wycor = window.getwindowcor()
    
    
    paddle = Paddle(int(wxcor/2) - 5, wycor-5, 10, 1, 1)
    
    
    # window.addpaddletoboard(paddle)
    # window.rendergame()
    
    fps_a = 1
    fps_b = 0
    fps_c = 0
    while True:
        
        #for managing time and frames
        fps_a = fps_a + 1
        if fps_a == 1000:
            fps_b = fps_b + 1
            fps_a = 0
        if fps_b == 1000:
            fps_c = fps_b + 1
            fps_c = 0 
        
        
        #getting input and filtering them
        keyinput = manageinput()
        keyinput.filterchar()
        
        paddle.paddlemovement(keyinput.returninput)
        window.clearinnerboard()
        window.addpaddletoboard(paddle)
        window.rendergame()
        
        
        
        
        if keyinput.returninput == 'X' or keyinput.returninput == 'x':
            break