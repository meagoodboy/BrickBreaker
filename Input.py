import tty, termios, sys

def getchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class manageinput:
    def __init__(self):
        self.accepted_inputs = ['A','a','D','d','X','x','C','c','s']
        self.returninput = ''
    
    
        
    
    def filterchar(self):
        char = getchar()
        if char == ' ':
            char = 's'
        if char in self.accepted_inputs:
            print(char)
            self.returninput = char
        else:
            self.returninput = ''
