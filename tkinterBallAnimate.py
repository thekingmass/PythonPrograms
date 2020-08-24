from tkinter import *
import time
import random

root = Tk()
root.title("Moving Balls")
#root.geometry("1000x100+20+50")
# root.geometry("800x600+565+10")
can = Canvas(root, height=600, width=1200, bg="cyan")
can.pack()

class Ball:

    def __init__(self, color, size):
        self.ball = can.create_oval(2, 5, size, size, fill=color)
        self.xdir = random.randrange(1, 10)
        self.ydir = random.randrange(1, 10)

    def animate(self):
        can.move(self.ball, self.xdir, self.ydir)
        pos = can.coords(self.ball)  # coords gives the co ordinates of the ball as - left top right bottom

        # making the ball to move only in the canvas window
        if pos[1] <= 0 or pos[3] >= 600:
            self.ydir = -self.ydir

        if pos[0] <= 0 or pos[2] >= 1200:
            self.xdir = -self.xdir

'''ball1 = Ball("red", 100)
ball2 = Ball("orange", 120)
ball3 = Ball("green", 70)'''

color = ["red", "green", "blue", "yellow", "gold", "orange", "cyan"]
movingball = []
for i in range(50):
    movingball.append(Ball(random.choice(color), random.randrange(50, 100)))


while True:

    for j in movingball:
        j.animate()

    root.update()
    time.sleep(0.000005)

    ''' ball1.animate()
     ball2.animate()
     ball3.animate()'''


root.mainloop()