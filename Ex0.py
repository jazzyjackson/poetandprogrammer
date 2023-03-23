#write a program that runs in full screen mode, and displays a random color in the background every second

import random
import time
import tkinter

def randomColor():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def main():
    root = tkinter.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background=randomColor())
    root.mainloop()



while True:
    main()
    time.sleep(1)






