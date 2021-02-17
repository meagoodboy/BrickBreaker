


def collitionball(ball, window):
    
    vel , nvel, evel , nevel, sevel = ball.getvel()
    board = window.getboard()
    xcor , ycor = ball.getloc()
    
    nycor = ycor + (-1*nvel)
    nycor = nycor + (-1*nevel)
    nycor = nycor + (1*sevel)
    
    nxcor = xcor + (1*nevel)
    nxcor = nxcor + (1*evel)
    nxcor = nxcor + (1*sevel)
    
    