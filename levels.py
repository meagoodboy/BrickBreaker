from objects import Brick
from gamewindow import Window

def printallbricks( window , bricklist):
    for i in bricklist:
        if i.health > 0:
            window.addbricktoboard(i)


def level1ini(window):
    bricklist = []
    
    bricklist.append(Brick(1, 10,10,4))
    bricklist.append(Brick(2, 19,10,1,'L'))
    bricklist.append(Brick(3, 28,10,4,'R'))
    bricklist.append(Brick(4, 10,12,4))
    bricklist.append(Brick(5, 19,12,4))
    bricklist.append(Brick(6, 28,12,4))
    # bricklist.append(Brick(7, 10,14,4))
    # bricklist.append(Brick(8, 19,14,4))
    # bricklist.append(Brick(9, 28,14,4))
    
    # bricklist.append(Brick(10, 55,10,4))
    # bricklist.append(Brick(11, 64,10,4))
    # bricklist.append(Brick(12, 73,10,4))
    # bricklist.append(Brick(13, 55,12,4))
    # bricklist.append(Brick(14, 64,12,4))
    # bricklist.append(Brick(15, 73,12,4))
    # bricklist.append(Brick(16, 55,14,4))
    # bricklist.append(Brick(17, 64,14,4))
    # bricklist.append(Brick(18, 73,14,4))
    
    bricklist.append(Brick(19, 100,10,4))
    bricklist.append(Brick(20, 109,10,4,'L'))
    bricklist.append(Brick(21, 118,10,4))
    bricklist.append(Brick(22, 100,12,4,'R'))
    bricklist.append(Brick(23, 109,12,4))
    bricklist.append(Brick(24, 118,12,4,'S'))
    # bricklist.append(Brick(25, 100,14,4))
    # bricklist.append(Brick(26, 109,14,4))
    # bricklist.append(Brick(27, 118,14,4))
    
    printallbricks(window, bricklist)
    
    return bricklist


def level2ini(window):
    bricklist = []
    
    bricklist.append(Brick(1, 10,10,4))
    bricklist.append(Brick(2, 19,10,4))
    bricklist.append(Brick(3, 28,10,4,'R'))
    bricklist.append(Brick(4, 10,12,1,'E'))
    bricklist.append(Brick(5, 19,12,1,'E'))
    bricklist.append(Brick(6, 28,12,1,'E'))
    bricklist.append(Brick(7, 10,14,4,'U'))
    bricklist.append(Brick(8, 19,14,4,'U'))
    bricklist.append(Brick(9, 28,14,1))
    
    bricklist.append(Brick(10, 37,10,4))
    bricklist.append(Brick(11, 46,10,4))
    bricklist.append(Brick(12, 55,10,1,'E'))
    bricklist.append(Brick(13, 37,12,1,'E'))
    bricklist.append(Brick(14, 46,12,1,'E'))
    bricklist.append(Brick(15, 55,12,1,'E'))
    bricklist.append(Brick(16, 37,14,2))
    bricklist.append(Brick(17, 46,14,2))
    bricklist.append(Brick(18, 55,14,1,'E'))

    # bricklist.append(Brick(19, 55,10,4))
    # bricklist.append(Brick(20, 55,10,4))
    bricklist.append(Brick(21, 64,10,4))
    bricklist.append(Brick(22, 73,10,4))
    bricklist.append(Brick(23, 55,12,1,'E'))
    bricklist.append(Brick(24, 64,12,4,'S'))
    bricklist.append(Brick(25, 73,12,4))
    bricklist.append(Brick(26, 55,14,1,'E'))
    bricklist.append(Brick(27, 64,14,4))
    bricklist.append(Brick(28, 73,14,4))
    
    bricklist.append(Brick(29, 100,10,4))
    bricklist.append(Brick(30, 109,10,4,'S'))
    bricklist.append(Brick(31, 118,10,4))
    bricklist.append(Brick(32, 100,12,4))
    bricklist.append(Brick(33, 109,12,4,'T'))
    bricklist.append(Brick(34, 118,12,4))
    bricklist.append(Brick(35, 100,14,4))
    bricklist.append(Brick(36, 109,14,4,'L'))
    bricklist.append(Brick(37, 118,14,4))
    
    printallbricks(window, bricklist)
    
    return bricklist



def level3ini(window):
    bricklist = []
    

    
    bricklist.append(Brick(10, 55,10,4,'U'))
    bricklist.append(Brick(11, 64,10,4,'U'))
    bricklist.append(Brick(12, 73,10,4))
    bricklist.append(Brick(13, 55,12,4))
    bricklist.append(Brick(14, 64,12,4,'L'))
    bricklist.append(Brick(15, 73,12,4))
    bricklist.append(Brick(16, 55,14,4,'T'))
    bricklist.append(Brick(17, 64,14,4))
    bricklist.append(Brick(18, 73,14,4,'T'))
    
    bricklist.append(Brick(19, 100,10,4))
    bricklist.append(Brick(20, 109,10,4))
    bricklist.append(Brick(21, 118,10,4,'S'))
    bricklist.append(Brick(22, 100,12,4))
    bricklist.append(Brick(23, 109,12,4))
    bricklist.append(Brick(24, 118,12,4))
    bricklist.append(Brick(25, 100,14,4,'T'))
    bricklist.append(Brick(26, 109,14,4))
    bricklist.append(Brick(27, 118,14,4))
    
    printallbricks(window, bricklist)
    
    return bricklist

def level4ini(window):
    bricklist = []
    
    bricklist.append(Brick(22, 10,14,4))
    bricklist.append(Brick(21, 19,14,4))
    bricklist.append(Brick(20, 28,14,4))
    bricklist.append(Brick(25, 100,14,4))
    bricklist.append(Brick(26, 109,14,4))
    bricklist.append(Brick(27, 118,14,4))
    
    printallbricks(window, bricklist)
    
    return bricklist

def checklevelover(bricks):
    for i in bricks:
        if i.health != 0:
            return 0
    
    return 1