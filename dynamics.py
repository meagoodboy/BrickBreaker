


def checkdead(ball, window):
    xvel , yvel = ball.getvel()
    board = window.getboard()
    xcor , ycor = ball.getloc()
    
    nycor = ycor + yvel

    nxcor = xcor + yvel
    
    width, height = window.getwindowcor()

    if nycor >= height - 4:
        return 1
    else:
        return 0

# working with no problems
def collitionballborder(ball, window):
    
    xvel , yvel = ball.getvel()
    board = window.getboard()
    xcor , ycor = ball.getloc()
    
    ixvel = xvel
    iyvel = yvel
    
    nycor = ycor + yvel

    nxcor = xcor + yvel
    
    width, height = window.getwindowcor()
    
    
    if nycor <= 3:
      yvel = abs(yvel)
    if nycor >= height - 3:
      yvel = -abs(yvel)
    if nxcor <= 4:
      xvel = abs(xvel)
    if nxcor >= width - 5:
      xvel = -abs(xvel)
    
    ball.setvel( xvel, yvel)
    
    if xvel == ixvel and yvel == iyvel :
        return 0
    else :
        return 1
    
# working with no problems    
def collisionballpaddle(ball, window, paddle):
    
    xvel , yvel = ball.getvel()
    board = window.getboard()
    xcor , ycor = ball.getloc()
    
    ixvel = xvel
    iyvel = yvel
    
    nycor = ycor + yvel
    nxcor = xcor + yvel
    
    pxcor, pycor = paddle.getloc()
    pwidth, pheight = paddle.getpaddledetails()
    
    if nycor == pycor:
        if nxcor >= pxcor and nxcor < pxcor + (pwidth/2):
            yvel = -abs(yvel)
            xvel = -abs(xvel)
        elif nxcor <= pxcor + pwidth and nxcor > pxcor + (pwidth/2) + 1:
            yvel = -abs(yvel)
            xvel = abs(xvel)
        elif nxcor == pxcor + (pwidth/2) + 1 or nxcor == pxcor + (pwidth/2):
            yvel = -yvel
        
        
    ball.setvel( xvel, yvel)

    if xvel == ixvel and yvel == iyvel :
        return 0
    else :
        return 1

def collisionballbrick(ball, window):
     
     
    xvel , yvel = ball.getvel()
    board = window.getboard()
    xcor , ycor = ball.getloc()
    
    ixvel = xvel
    iyvel = yvel
    
    nycor = ycor + yvel

    nxcor = xcor + yvel
    
    
    if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
        xvel = -xvel
        yvel = -yvel
    elif board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
        xvel = -xvel
        yvel = -yvel
    elif board[nycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
        yvel = -yvel
    elif board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B':
        xvel = -xvel
    elif board[nycor][nxcor].idtag == 'B':
        xvel = -xvel
        yvel = -yvel
    elif board[ycor][nxcor].idtag == 'B':
        xvel = -xvel
    elif board[nycor][xcor].idtag == 'B':
        yvel = -yvel
        
    ball.setvel( xvel, yvel)
    
    if xvel == ixvel and yvel == iyvel :
        return 0
    else :
        return 1