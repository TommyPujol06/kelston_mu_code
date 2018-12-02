"""Working code for the turtle/polygon session
"""
import turtle as t

#
# a) Draw a square
#
t.reset()
t.pencolor("red")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

#
# b) Factor out commonality
#
t.reset()
t.pencolor("blue")
for n_side in range(4):
    t.forward(100)
    t.left(90)

#
# c) Turn it into a function and call it twice
#
def square():
    for n_side in range(4):
        t.forward(100)
        t.left(90)

t.reset()
t.pencolor("green")
square()

t.penup()
t.forward(200)
t.pendown()
square()

#
# d) Do the same for a triangle
#
def triangle():
    for n_side in range(3):
        t.forward(100)
        t.left(120)
    
t.reset()
t.pencolor("orange")
triangle()

#
# e) And now for a pentagon and a hexagon
#
def pentagon():
    for n_side in range(5):
        t.forward(100)
        t.left(72)

def hexagon():
    for n_side in range(6):
        t.forward(100)
        t.left(60)

t.reset()
t.pencolor("blue")
pentagon()

t.penup()
t.forward(200)
t.pendown()
hexagon()

#
# Any regular polygon
#
def polygon(n_sides):
    for n_side in range(n_sides):
        t.forward(100)
        t.left(360 / n_sides)

t.reset()
t.pencolor("blue")

t.penup()
t.setpos(-300, 0)
t.pendown()
polygon(5)

t.penup()
t.forward(100)
t.pendown()
polygon(7)

t.penup()
t.forward(100)
t.pendown()
polygon(10)

#
# Play with length of sides
# How many sides before it looks round?
# Half a polygon?
#

#
# Exercise: construct your initials
# Look at the docs for the turtle module
#