from turtle import *


wn = Screen()
wn.title('My Flag My Pride "Tiranga"')
t = Turtle()
wn.bgcolor('cyan')
t.shape("turtle")
t.speed(1)

t.up()

# Going to bottom of the page
t.goto(-50,-250)
t.down()
# now we reached at the bottom

# making the base
t.begin_fill()
t.fillcolor('black')
t.left(90)
t.circle(30, 50)
t.left(40)
t.fd(30)
t.left(40)
t.circle(30, 50)
t.left(90)
t.fd(50)
t.end_fill()
t.left(180)
t.up()
t.fd(25)
t.right(90)
t.fd(25)
t.down()



# making the flag rod
t.pensize(8)
t.fd(500)
t.right(90)

# making the strips
def strip():
    t.pensize(3)
    t.fd(200)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(200)
# making the first strip
t.begin_fill()
t.fillcolor('red')
strip()
t.end_fill()
t.left(90)
# making the second and third strip

t.fd(50)
t.left(90)
t.begin_fill()
t.fillcolor('green')
strip()
t.end_fill()

# giving the last line to the middle strip
t.right(180)
t.fd(200)
t.left(90)
t.fd(100)

# making the 'Ashok Chakra' in the middle strap
t.left(90)
t.fd(117)
t.left(90)
t.up()
t.fd(25)
t.down()
t.circle(17)


# creating te spokes in the Ashok Chakra

t.fd(2)
t.left(90)
for i in range(9):
    t.pensize(1)
    # t.pencolor(color[i % 5])
    t.forward(34)
    t.left(160)

t.hideturtle()
done()