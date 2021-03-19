


def checkdead(ball, window):
    xvel , yvel = ball.getvel()
    board = window.getboard()
    xcor , ycor = ball.getloc()
    
    nycor = ycor + yvel

    nxcor = xcor + yvel
    
    width, height = window.getwindowcor()

    if nycor >= height - 3:
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
    a = 0
    b = 0
    c = 0
    
    
    if board[nycor][nxcor] != None and board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][xcor].diewithahit(power)
            # b = board[ycor][nxcor].diewithahit(power)
            # c = board[nycor][nxcor].diewithahit(power)
    elif board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            a = board[ycor][nxcor].diewithahit(power)
            # b =  board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            a = board[nycor][nxcor].diewithahit(power)
            # b = board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[ycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            a = board[nycor][nxcor].diewithahit(power)
            # b = board[ycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None:
        if board[nycor][nxcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][nxcor].diewithahit(power)
    elif board[ycor][nxcor] != None:
        if board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            a = board[ycor][nxcor].diewithahit(power)
    elif board[nycor][xcor] != None:
        if board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            a = board[nycor][xcor].diewithahit(power)
     
    if power == 0:    
        ball.setvel( xvel, yvel)
    
    if b > a:
        a = b
          
    if xvel != ixvel or yvel != iyvel :
        return a
    
    if abs(xvel) > 1:
        nycor = nycor + yval
        nxcor = nxcor + xval
        
    if board[nycor][nxcor] != None and board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][nxcor].diewithahit(power)
            # b = board[ycor][nxcor].diewithahit(power)
            # c = board[nycor][xcor].diewithahit(power)
    elif board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[ycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            a = board[ycor][nxcor].diewithahit(power)
            # b = board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            a = board[nycor][nxcor].diewithahit(power)
            # a = board[nycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None and board[ycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'B' and board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            a = board[nycor][nxcor].diewithahit(power)
            # a = board[ycor][xcor].diewithahit(power)
    elif board[nycor][nxcor] != None:
        if board[nycor][nxcor].idtag == 'B':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][nxcor].diewithahit(power)
    elif board[ycor][nxcor] != None:
        if board[ycor][nxcor].idtag == 'B':
            xvel = -xvel
            a = board[ycor][nxcor].diewithahit(power)
    elif board[nycor][xcor] != None:
        if board[nycor][xcor].idtag == 'B':
            yvel = -yvel
            a = board[nycor][xcor].diewithahit(power)
    
    
    if power == 0:    
        ball.setvel( xvel, yvel)
    
    if b > a :
        a = b
    
    
    
    if xvel == ixvel and yvel == iyvel :
        return 0
    else :
        return a
    
    
def blastit(xcc, ycc, bricks):
    blastlist = [(x,y)]
    lx = xcc - 15
    ly = ycc - 10
    ux = xcc + 15
    uy = ycc + 10
    for i in bricks:
        xc, yc = i.getloc()
        if xc >= lx and xc <=ux and yc >= ly and yc <= uy:
            test = 4
            i.health = 0
            
    return bricks


def checkbricks(bricks, ll):
    for i in bricks:
        x, y = i.getloc()
        if y >= ll - 1 and i.health != 0:
            return 1
    return 0
def collisionbulletpaddle(bullet, paddle):
    bx, by = bullet.getloc()
    px, py = paddle.getloc()
    w, h = paddle.getpaddledetails()
    if bx >= px and bx <= px + w and by == py:
        return 1
    return 0

def collisionballboss(ball, window):
     
     
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
    a = 0
    b = 0
    c = 0
    
    
    if board[nycor][nxcor] != None and board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'D' and board[ycor][nxcor].idtag == 'D' and board[nycor][xcor].idtag == 'D':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][xcor].diewithahitboss(power)
            # b = board[ycor][nxcor].diewithahitboss(power)
            # c = board[nycor][nxcor].diewithahitboss(power)
    elif board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[ycor][nxcor].idtag == 'D' and board[nycor][xcor].idtag == 'D':
            xvel = -xvel
            yvel = -yvel
            a = board[ycor][nxcor].diewithahitboss(power)
            # b =  board[nycor][xcor].diewithahitboss(power)
    elif board[nycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'D' and board[nycor][xcor].idtag == 'D':
            yvel = -yvel
            a = board[nycor][nxcor].diewithahitboss(power)
            # b = board[nycor][xcor].diewithahitboss(power)
    elif board[nycor][nxcor] != None and board[ycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'D' and board[ycor][nxcor].idtag == 'D':
            xvel = -xvel
            a = board[nycor][nxcor].diewithahitboss(power)
            # b = board[ycor][xcor].diewithahitboss(power)
    elif board[nycor][nxcor] != None:
        if board[nycor][nxcor].idtag == 'D':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][nxcor].diewithahitboss(power)
    elif board[ycor][nxcor] != None:
        if board[ycor][nxcor].idtag == 'D':
            xvel = -xvel
            a = board[ycor][nxcor].diewithahitboss(power)
    elif board[nycor][xcor] != None:
        if board[nycor][xcor].idtag == 'D':
            yvel = -yvel
            a = board[nycor][xcor].diewithahitboss(power)
     
    if power == 0:    
        ball.setvel( xvel, yvel)
    
    if b > a:
        a = b
          
    if xvel != ixvel or yvel != iyvel :
        return a
    
    if abs(xvel) > 1:
        nycor = nycor + yval
        nxcor = nxcor + xval
        
    if board[nycor][nxcor] != None and board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'D' and board[ycor][nxcor].idtag == 'D' and board[nycor][xcor].idtag == 'D':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][nxcor].diewithahitboss(power)
            # b = board[ycor][nxcor].diewithahitboss(power)
            # c = board[nycor][xcor].diewithahitboss(power)
    elif board[ycor][nxcor] != None and board[nycor][xcor] != None:
        if board[ycor][nxcor].idtag == 'D' and board[nycor][xcor].idtag == 'D':
            xvel = -xvel
            yvel = -yvel
            a = board[ycor][nxcor].diewithahitboss(power)
            # b = board[nycor][xcor].diewithahitboss(power)
    elif board[nycor][nxcor] != None and board[nycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'D' and board[nycor][xcor].idtag == 'D':
            yvel = -yvel
            a = board[nycor][nxcor].diewithahitboss(power)
            # a = board[nycor][xcor].diewithahitboss(power)
    elif board[nycor][nxcor] != None and board[ycor][xcor] != None:
        if board[nycor][nxcor].idtag == 'D' and board[ycor][nxcor].idtag == 'D':
            xvel = -xvel
            a = board[nycor][nxcor].diewithahitboss(power)
            # a = board[ycor][xcor].diewithahitboss(power)
    elif board[nycor][nxcor] != None:
        if board[nycor][nxcor].idtag == 'D':
            xvel = -xvel
            yvel = -yvel
            a = board[nycor][nxcor].diewithahitboss(power)
    elif board[ycor][nxcor] != None:
        if board[ycor][nxcor].idtag == 'D':
            xvel = -xvel
            a = board[ycor][nxcor].diewithahitboss(power)
    elif board[nycor][xcor] != None:
        if board[nycor][xcor].idtag == 'D':
            yvel = -yvel
            a = board[nycor][xcor].diewithahitboss(power)
    
    
    if power == 0:    
        ball.setvel( xvel, yvel)
    
    if b > a :
        a = b
    
    
    
    if xvel == ixvel and yvel == iyvel :
        return 0
    else :
        return a