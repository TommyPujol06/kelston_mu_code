import turtle as t

def polygon(n_sides):
    for i in range(n_sides):
        t.forward(50)
        t.left(360.0 / n_sides)

polygon(5)