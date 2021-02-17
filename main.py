

from gamewindow import Window
from Input import manageinput

if __name__ == "__main__":
    # window = Window()
    # window.initgameborder()
    # window.rendergameborder()
    while True:
        lol = manageinput()
        lol.filterchar()
        if lol.returninput == 'X' or lol.returninput == 'x':
            break