import os
import signal
import sys
import time
import random
from colorama import Fore
from gamewindow import Window
from objects import Objects, Paddle, Ball, Brick
from Input import manageinput
from dynamics import collitionballborder, collisionballpaddle, collisionballbrick, checkdead
from levels import level1ini, printallbricks, checklevelover, level2ini, level3ini


def alarmHandler(*arg):
    raise Exception




if __name__ == "__main__":
    
    
    
    loopvar = 1
    countloop = 0
    level = 1
    lives = 3
    score = 0
    timecount = 0
    won = 0
    randvelocity = [ -1, 1]
    window = Window()
    window.initgameborder()
    wxcor, wycor = window.getwindowcor()
    
    
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
    paddle = Paddle(int(wxcor/2) - 5, wycor-5, 20, 4, 1)
    ball = Ball(int(wxcor/2), wycor-6, 0, 1)
    randomvar = random.choice(randvelocity)
    ball.setvel( randomvar ,-1)
    # randomloc = random.randint( int(wxcor/2) - 5, wycor-5)
    # ball.setloc(randomloc, wycor - 6)
    print(randomvar)
    # window.addpaddletoboard(paddle)
    # window.rendergame()
    timeout = 0.05
    keyinput = manageinput()
    time.sleep(4)    
    
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
            
            #collisionball(ball, window)
            if ballvelx != 0:
                ball.ballmovement()
                dead = checkdead(ball, window)
                ballborder = collitionballborder(ball, window)
                ballpaddle = collisionballpaddle(ball, window, paddle)
                ballbrick = collisionballbrick(ball, window)
            #collisionballpaddle(ball, window)
            score = score + ballbrick
            
            
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
               
            #render everything
            if ballvelx != 0:
                window.clearinnerboard()
                window.addpaddletoboard(paddle)
                window.addballtoboard(ball)
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
        
    print(levelover)