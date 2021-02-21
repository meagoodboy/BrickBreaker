


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

    nxcor = xcor + xvel
    
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
    
    xval = abs(xvel)
    yval = abs(yvel)
    
    yval = int(yvel/yval)
    xval = int(xvel/xval) 
    
    nycor = ycor + yval
    nxcor = xcor + xval
    
    pxcor, pycor = paddle.getloc()
    pwidth, pheight = paddle.getpaddledetails()
    
    if nycor == pycor:
        if nxcor > pxcor + 1 and nxcor < pxcor + (pwidth/2):
            yvel = -1
            xvel = -1
        elif nxcor < pxcor + pwidth - 1 and nxcor > pxcor + (pwidth/2) + 1:
            yvel = -1
            xvel = 1
        elif nxcor == pxcor + (pwidth/2) + 1 or nxcor == pxcor + (pwidth/2):
            yvel = -1
        elif nxcor == pxcor or nxcor == pxcor + 1:
            yvel = -2
            xvel = -2
        elif nxcor == pxcor + pwidth or nxcor == pxcor + pwidth -1:
            yvel = -2
            xvel = 2
        
    ball.setvel( xvel, yvel)
    
    
    if xvel != ixvel or yvel != iyvel :
        return 1
    
    if abs(xvel) > 1:
        nycor = nycor + yval
        nxcor = nxcor + xval
        
    if nycor == pycor:
        if nxcor > pxcor + 1 and nxcor < pxcor + (pwidth/2):
            yvel = -1
            xvel = -1
        elif nxcor < pxcor + pwidth - 1 and nxcor > pxcor + (pwidth/2) + 1:
            yvel = -1
            xvel = 1
        elif nxcor == pxcor + (pwidth/2) + 1 or nxcor == pxcor + (pwidth/2):
            yvel = -1
        elif nxcor == pxcor or nxcor == pxcor + 1:
            yvel = -2
            xvel = -2
        elif nxcor == pxcor + pwidth or nxcor == pxcor + pwidth -1:
            yvel = -2
            xvel = 2

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
    
    xval = abs(xvel)
    yval = abs(yvel)
    
    yval = int(yvel/yval)
    xval = int(xvel/xval) 
    
    nycor = ycor + yval
    nxcor = xcor + xval
    
    power = ball.getpower()
    
    if board[nycor][nxcor] != None and board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            board[nycor][nxcor].diewithahit(power)
            board[ycor][nxcor].diewithahit(power)
            board[nycor][xcor].diewithahit(power)
    elif board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            board[ycor][nxcor].diewithahit(power)
            board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            board[nycor][nxcor].diewithahit(power)
            board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[ycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            board[nycor][nxcor].diewithahit(power)
            board[ycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None:
        if board[nycor][nxcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            board[nycor][nxcor].diewithahit(power)
    elif board[ycor][nxcor] != None:
        if board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            board[ycor][nxcor].diewithahit(power)
    elif board[nycor][xcor] != None:
        if board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            board[nycor][xcor].diewithahit(power)
     
    if power == 0:    
        ball.setvel( xvel, yvel)
          
    if xvel != ixvel or yvel != iyvel :
        return 1
    
    if abs(xvel) > 1:
        nycor = nycor + yval
        nxcor = nxcor + xval
        
    if board[nycor][nxcor] != None and board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            board[nycor][nxcor].diewithahit(power)
            board[ycor][nxcor].diewithahit(power)
            board[nycor][xcor].diewithahit(power)
    elif board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            board[ycor][nxcor].diewithahit(power)
            board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            board[nycor][nxcor].diewithahit(power)
            board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[ycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            board[nycor][nxcor].diewithahit(power)
            board[ycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None:
        if board[nycor][nxcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            board[nycor][nxcor].diewithahit(power)
    elif board[ycor][nxcor] != None:
        if board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            board[ycor][nxcor].diewithahit(power)
    elif board[nycor][xcor] != None:
        if board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            board[nycor][xcor].diewithahit(power)
    
    
    if power == 0:    
        ball.setvel( xvel, yvel)
    
    
    
    
    
    if xvel == ixvel and yvel == iyvel :
        return 0
    else :
        return 1