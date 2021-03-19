import os
import signal
import sys
import time
import random
from colorama import Fore
from gamewindow import Window
from objects import Objects, Paddle, Ball, Brick, Powerupimg, Boss, Bossbullet
from Input import manageinput
from dynamics import collitionballborder, collisionballpaddle, collisionballbrick, checkdead, blastit, checkbricks, collisionballboss, collisionbulletpaddle
from levels import level1ini, printallbricks, checklevelover, level2ini, level3ini, level4ini
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
    bulletlist = None
    randvelocity = [ -1, 1]
    window = Window()
    window.initgameborder()
    wxcor, wycor = window.getwindowcor()
    velocityoverride = 0
    grabbingoverride = 0
    multiplieroverride = 0
    gravityactivate = 0
    deadforeternity = 0
    boss = 0
    shoot = 0
    
    #throws error is window is small
    if wxcor < 140 or wycor < 40:
        print("terminal size is too small")
        time.sleep(3)
        loopvar = 0
    print("welcome to BRICK BREAKER 1.0")
    print("press x to exit")
    print("press c to continue paused game")
    print("press a and d to move paddle")
    print("press s to skip levels")
    #give paddlewidth as a multiple of 2 everytime
    paddle = Paddle(int(wxcor/2) - 5, wycor-5, 30, 4, 1)
    ball = Ball(int(wxcor/2), wycor-6, 0, 1)
    bossitem = Boss(int(wxcor/2) - 5, 5, 20)
    # bossitem = 0
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
    bossdead = 0
    bricks = level1ini(window)    
    window.modifylevel(level)  
    moc = 0  
     #   HELP fix fps
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()  
    
    while loopvar:
        countloop = countloop + 1
        if countloop == 20:
            timecount = timecount + 1
            countloop = 0
            
        if timecount % 9 == 0 and timecount != 0:
            gravityactivate = 1
            
        if timecount % 9 == 0 and timecount != 0:
            shoot = 1
        
        try:
            signal.signal(signal.SIGALRM, alarmHandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            
            
            ballvelx, ballvely = ball.getvel()
            if ballvelx == 0 and keyinput.returninput == 'c':
                randomvar = random.choice(randvelocity)
                ball.setvel( randomvar ,-1)
                grabbingoverride = 0
            dead2 = 0
            #collisionball(ball, window)
            yvariable = 0
            bossbulletpaddle = 0
            if ballvelx != 0:
                ball.ballmovement()
                px, py = paddle.getloc()
                bossitem.bossmovement(px)
                if bulletlist != None:
                    yvariable = bulletlist.bulletmovement()
                    bossbulletpaddle = collisionbulletpaddle(bulletlist, paddle)
                    if bossbulletpaddle == 1:
                        dead2 = 1
                        bulletlist = None
                    if yvariable == 1:
                        bulletlist = None
                powerupmove(poweruplist, wycor - 4)
                dead = checkdead(ball, window)
                ballborder = collitionballborder(ball, window)
                ballpaddle = collisionballpaddle(ball, window, paddle)
                ballboss = collisionballboss(ball, window)
                if ballboss == 1 and bossitem.health % 7 == 0:
                    bricks.append(Brick(50, 10,14,1))
                    bricks.append(Brick(50, 20,14,1))
                    bricks.append(Brick(50, 30,14,1))
                    bricks.append(Brick(50, 40,14,1))
                    bricks.append(Brick(50, 50,14,1))
                    bricks.append(Brick(50, 60,14,1))
                    bricks.append(Brick(50, 70,14,1))
                    bricks.append(Brick(50, 80,14,1))
                    bricks.append(Brick(50, 90,14,1))
                    bricks.append(Brick(50, 100,14,1))
                    bricks.append(Brick(50, 110,14,1))
                    bricks.append(Brick(50, 120,14,1))
                    
                if ballboss == 1 and bossitem.health == 0:
                    bossdead = 1
                # print('\a')
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
            
            if ballpaddle == 1 and gravityactivate == 1:
                for b in bricks:
                    b.gravityeffect(1)
                gravityactivate = 0
            deadforeternity = checkbricks(bricks, wycor - 5)
            if deadforeternity == 1:
                lives = 0
                break
            #collisionballpaddle(ball, window)
            score = score + ballbrick
            # if not poweruplist:
            #     test = 9
            # else :
            #     test = 2
            moc = 0
            if shoot == 1 and boss == 1:
                xl, yl = bossitem.getloc()
                bulletlist = Bossbullet(xl + 10, 11)
                shoot = 0
                moc = 5
            
            if dead or dead2:
                if lives == 1:
                    break
                else:
                    lives = lives - 1
                    ball.setvel( 0, 0)
                    ball.setloc(int(wxcor/2), wycor-6)
                    paddle.setloc(int(wxcor/2) - 5, wycor-5)
                dead = 0
                dead2 = 0
            
                   
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
                    level = level + 1
                    # boss = 1
                    bricks = level4ini(window)
                elif level == 4:
                    if bossdead == 1:
                        won = 1
                        break
            
                
                ball.setvel( 0, 0)
                ball.setloc(int(wxcor/2), wycor-6)
                paddle.setloc(int(wxcor/2) - 5, wycor-5)
                levelover = 0
            dx = 0
            for xb in bricks:
                dx = xb.changecolour()
                
            if level == 4:
                boss = 1
                    
            # modify gamestats here
            window.modifylevel(level)
            window.modifylives(lives)
            window.modifytime(timecount)
            window.modifyscore(score)
            lol = 0
            # if bulletlist != None:
            #     lol = 1
            window.modifytest(bossitem.health % 7)
            
            
            
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
                if boss == 1:
                    window.addbosstoboard(bossitem)
                if bulletlist != None:
                    window.addbullettoboard(bulletlist)
                        
                        
            os.system('clear')
            window.rendergame()    
            #getting input and filtering them
            
            
            
            
            
            keyinput.filterchar()
            if ballvelx != 0:
                paddle.paddlemovement(keyinput.returninput)
            
            # to skip levels
            if keyinput.returninput == 's':
                bricks.clear()
                os.system('clear')
            
            
            
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
    # print(bossitem.xcor, bossitem.ycor)
    # print(bulletlist.xcor, bulletlist.ycor)
    # print(moc)    
    # print(levelover)
    # print(activepowerups)Fbo
    # print(lx , ux, ly, uy)