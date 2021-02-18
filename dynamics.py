


def collitionball(ball, window):
    
    xvel , yvel = ball.getvel()
    board = window.getboard()
    xcor , ycor = ball.getloc()
    
    ixvel = xvel
    iyvel = yvel
    
    nycor = ycor + yvel

    nxcor = xcor + yvel
    
    # if board[nycor][nxcor].idtag != 'P' or board[nycor][xcor].idtag != 'P' :
    if board[nycor][nxcor] != None and board[ycor][nxcor] != None and board[nycor][xcor] != None:
        xvel = -xvel
        yvel = -yvel
    elif board[ycor][nxcor] != None and board[nycor][xcor] != None:
        xvel = -xvel
        yvel = -yvel
    elif board[nycor][nxcor] != None and board[nycor][xcor] != None:
        yvel = -yvel
    elif board[nycor][nxcor] != None and board[ycor][nxcor] != None:
        xvel = -xvel
    elif board[nycor][nxcor] != None:
        xvel = -xvel
        yvel = -yvel
        
    ball.setvel( xvel, yvel)