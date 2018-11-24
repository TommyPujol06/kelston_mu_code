import turtle as t

def triangle():
    for n_side in range(3):
        t.forward(20)
        t.left(120)

def square():
    for n_side in range(4):
        t.forward(20)
        t.left(90)

def pentagon():
    for n_side in range(5):
        t.forward(20)
        t.left(72)

def hexagon():
    for n_side in range(6):
        t.forward(20)
        t.left(60)

def polygon(n_sides):
    for n_side in range(n_sides):
        t.forward(20)
        t.left(360.0 / n_sides)

def half_polygon(n_sides):
    for n_side in range(n_sides // 2):
        t.forward(20)
        t.left(360.0 / n_sides)

half_polygon(24)