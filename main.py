import os
import signal
import sys
import time
import random
from colorama import Fore
from gamewindow import Window
from objects import Objects, Paddle, Ball, Brick, Powerupimg
from Input import manageinput
from dynamics import collitionballborder, collisionballpaddle, collisionballbrick, checkdead, blastit
from levels import level1ini, printallbricks, checklevelover, level2ini, level3ini
from powerup import  powerupmove, powerupaddtoboard, powerupcollide, activatepowerup, terminatepowerups, terminateallpowerups
import config as config

def alarmHandler(*arg):
    raise Exception




if __name__ == "__main__":
    
    
    
    loopvar = 1
    countloop = 0
    level = 1
    lives = config.livess
    score = 0
    timecount = 0
    won = 0
    poweruplist = []
    activepowerups = []
    randvelocity = [ -1, 1]
    window = Window()
    window.initgameborder()
    wxcor, wycor = window.getwindowcor()
    velocityoverride = 0
    grabbingoverride = 0
    multiplieroverride = 0
    #throws error is window is small
    if wxcor < 140 or wycor < 40:
        print("terminal size is too small")
        time.sleep(3)
        loopvar = 0
    print("welcome to BRICK BREAKER 1.0")
    print("press x to exit")
    print("press c to continue paused game")
    print("press a and d to move paddle")
    #give paddlewidth as a multiple of 2 everytime
    paddle = Paddle(int(wxcor/2) - 5, wycor-5, 30, 4, 1)
    ball = Ball(int(wxcor/2), wycor-6, 0, 1)
    randomvar = random.choice(randvelocity)
    ball.setvel( randomvar ,-1)
    # randomloc = random.randint( int(wxcor/2) - 5, wycor-5)
    # ball.setloc(randomloc, wycor - 6)
    # print(randomvar)
    # window.addpaddletoboard(paddle)
    # window.rendergame()
    timeout = config.timeouts
    keyinput = manageinput()
    time.sleep(4)    
    #test variable 
    test = 0
    bricks = level1ini(window)    
    window.modifylevel(level)    
     #   HELP fix fps
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()  
    
    while loopvar:
        countloop = countloop + 1
        if countloop == 20:
            timecount = timecount + 1
            countloop = 0
        try:
            signal.signal(signal.SIGALRM, alarmHandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            
            
            ballvelx, ballvely = ball.getvel()
            if ballvelx == 0 and keyinput.returninput == 'c':
                randomvar = random.choice(randvelocity)
                ball.setvel( randomvar ,-1)
                grabbingoverride = 0
            
            #collisionball(ball, window)
            if ballvelx != 0:
                ball.ballmovement()
                powerupmove(poweruplist, wycor - 4)
                dead = checkdead(ball, window)
                ballborder = collitionballborder(ball, window)
                ballpaddle = collisionballpaddle(ball, window, paddle)
                if velocityoverride == 1:
                    xvi, yvi = ball.getvel()
                    xvi = xvi/abs(xvi)
                    yvi = yvi/abs(yvi)
                    xvi = int(2*xvi)
                    yvi = int(2*yvi)
                    ball.setvel(xvi, yvi)
                ballbrick = collisionballbrick(ball, window)
                powerupval = powerupcollide(paddle, poweruplist)
                if powerupval != 'N' :
                    # test = 9
                    activepowerups.append((powerupval, timecount))
                    check = activatepowerup(ball, paddle, powerupval)
                    if check == 5:
                        velocityoverride = 1
                    if check == 6:
                        grabbingoverride = 1
                
                if ballbrick != 0:
                    test = ballbrick
                if ballbrick == 2:
                    xcc , ycc = ball.getloc()
                    test = 3
                    # blastit(xcc, ycc, bricks, window)
                    bllist = [(xcc,ycc)]
                    for k in bllist:
                        lx = k[0] - 15
                        ly = k[1] - 10
                        ux = k[0] + 15
                        uy = k[1] + 10
                        for i in bricks:
                            xc, yc = i.getloc()
                            if i.bproperty == 'E' and i.health != 0:
                                bllist.append(i.getloc())
                            if xc >= lx and xc <=ux and yc >= ly and yc <= uy:
                                test = 4
                                i.health = 0
                        blllist.remove(k)
                            
                            
                    # test = 8
                elif ballbrick > 2:
                    xc, yc = ball.getloc()
                    #make paddle small
                    if ballbrick == 3:
                        poweruplist.append(Powerupimg(xc, yc, 'S', 'S'))
                    elif ballbrick == 4:
                        poweruplist.append(Powerupimg(xc, yc, 'L', 'L'))
                    elif ballbrick == 5:
                        poweruplist.append(Powerupimg(xc, yc, 'M', 'M'))
                    elif ballbrick == 6:
                        poweruplist.append(Powerupimg(xc, yc, 'F', 'F'))
                    elif ballbrick == 7:
                        poweruplist.append(Powerupimg(xc, yc, 'T', 'T'))
                    elif ballbrick == 8:
                        poweruplist.append(Powerupimg(xc, yc, 'G', 'G'))
                        
                elif ballbrick == 1:
                    pass
                else:
                    pass
            
            
            #collisionballpaddle(ball, window)
            score = score + ballbrick
            # if not poweruplist:
            #     test = 9
            # else :
            #     test = 2
            
            if dead:
                if lives == 1:
                    break
                else:
                    lives = lives - 1
                    ball.setvel( 0, 0)
                    ball.setloc(int(wxcor/2), wycor-6)
                    paddle.setloc(int(wxcor/2) - 5, wycor-5)
                dead = 0
                    
            levelover = checklevelover(bricks)
            
            if levelover:
                bricks.clear()
                terminateallpowerups(ball, paddle)
                velocityoverride = 0
                grabbingoverride = 0
                poweruplist.clear()
                activepowerups.clear()
                if level == 1:
                    level = level + 1
                    bricks = level2ini(window)
                elif level == 2:
                    level = level + 1
                    bricks = level3ini(window)
                elif level == 3:
                    won = 1
                    break
                
                
                ball.setvel( 0, 0)
                ball.setloc(int(wxcor/2), wycor-6)
                paddle.setloc(int(wxcor/2) - 5, wycor-5)
                levelover = 0
                    
            # modify gamestats here
            window.modifylevel(level)
            window.modifylives(lives)
            window.modifytime(timecount)
            window.modifyscore(score)
            window.modifytest(test)
            check2 = terminatepowerups(ball, paddle, activepowerups, timecount, 10)
            if check2 == 5:
                velocityoverride = 0
            elif check2 == 6:
                grabbingoverride = 0
            #render everything
            if ballvelx != 0:
                window.clearinnerboard()
                window.addpaddletoboard(paddle)
                window.addballtoboard(ball)
                powerupaddtoboard(window, poweruplist)
                printallbricks(window ,bricks)
            os.system('clear')
            window.rendergame()    
            #getting input and filtering them
            
            
            
            
            
            keyinput.filterchar()
            if ballvelx != 0:
                paddle.paddlemovement(keyinput.returninput)
            
            
            
            
            
            if keyinput.returninput == 'X' or keyinput.returninput == 'x':
                break
                
        except :
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            pass
    
    
    
    os.system('clear')  
    print("*********************************GAME OVER*************************" + Fore.LIGHTYELLOW_EX)
    print("score  : " , score )
    print("time  : " , timecount )
    if won:
        print("you won")
    else:
        print("you lost, better luck next time")
        
    # print(levelover)
    # print(activepowerups)Fbo
    # print(lx , ux, ly, uy)