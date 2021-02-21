from objects import Brick
from gamewindow import Window

def printallbricks( window , bricklist):
    for i in bricklist:
        if i.health > 0:
            window.addbricktoboard(i)


def level1ini(window):
    bricklist = []
    
    bricklist.append(Brick(1, 10,10,4))
    bricklist.append(Brick(2, 19,10,4))
    bricklist.append(Brick(3, 28,10,4))
    bricklist.append(Brick(4, 10,12,4))
    bricklist.append(Brick(5, 19,12,4))
    bricklist.append(Brick(6, 28,12,4))
    bricklist.append(Brick(7, 10,14,4))
    bricklist.append(Brick(8, 19,14,4))
    bricklist.append(Brick(9, 28,14,4))
    
    bricklist.append(Brick(10, 55,10,4))
    bricklist.append(Brick(11, 64,10,4))
    bricklist.append(Brick(12, 73,10,4))
    bricklist.append(Brick(13, 55,12,4))
    bricklist.append(Brick(14, 64,12,4))
    bricklist.append(Brick(15, 73,12,4))
    bricklist.append(Brick(16, 55,14,4))
    bricklist.append(Brick(17, 64,14,4))
    bricklist.append(Brick(18, 73,14,4))
    
    bricklist.append(Brick(19, 100,10,4))
    bricklist.append(Brick(20, 109,10,4))
    bricklist.append(Brick(21, 118,10,4))
    bricklist.append(Brick(22, 100,12,4))
    bricklist.append(Brick(23, 109,12,4))
    bricklist.append(Brick(24, 118,12,4))
    bricklist.append(Brick(25, 100,14,4))
    bricklist.append(Brick(26, 109,14,4))
    bricklist.append(Brick(27, 118,14,4))
    
    printallbricks(window, bricklist)
    
    return bricklist