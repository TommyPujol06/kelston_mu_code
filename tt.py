import turtle as t
from turtle import *

Screen().bgcolor("blue")
pencolor("white")
forward(100)
right(45)
setpos(100, 100)
write("Hello", font=("Arial", 24, "normal"))
for s in ["arrow", "turtle", "circle", "square", "triangle", "classic"]:
    shape(s)
    stamp()
    forward(50)
