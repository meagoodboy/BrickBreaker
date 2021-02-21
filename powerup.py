

     
def powerupmove(poweruplist, ycor):
    for i in poweruplist:
        i.powerupmovement()
        x, y = i.getloc()
        if y > ycor:
            poweruplist.remove(i)
        
def powerupaddtoboard(window, poweruplist):
    for i in poweruplist:
        x , y = i.getloc()
        window.addpoweruptoboard(i)
        
def powerupcollide(paddle , poweruplist):
    px, py = paddle.getloc()
    w, h = paddle.getpaddledetails()
    for i in poweruplist:
        x, y = i.getloc()
        if y == py:
            if x >= px and x <= px + w:
                l = i.ptype
                poweruplist.remove(i)
                return l
    return 'N'
            
def activatepowerup(ball, paddle, val):
    if val == 'S':
        paddle.changepaddlewidth(20)
    elif val == 'L':
        paddle.changepaddlewidth(40)
    elif val == 'M':
        pass
    elif val == 'F':
        pass
    elif val == 'T':
        ball.setpower(1)
        ball.setcolour(Fore.RED)
    elif val == 'G':
        pass
    
def terminatepowerups(ball, paddle , powerlist, timeouts, expiry):
    for i in powerlist:
        if i[1] + expiry < timeouts:
            if i[0] == 'S':
                paddle.changepaddlewidth(30)
            elif i[0] == 'L':
                paddle.changepaddlewidth(30)
            elif i[0] == 'M':
                pass
            elif i[0] == 'F':
                pass
            elif i[0] == 'T':
                pass
                ball.setpower(0)
                # ball.setcolour(Fore.WHITE)
            elif i[0] == 'G':
                pass        
            powerlist.remove(i)
            
            
def terminateallpowerups(ball, paddle):
    paddle.changepaddlewidth(30)
    ball.setpower(0)
    # ball.setcolour(Fore.WHITE)