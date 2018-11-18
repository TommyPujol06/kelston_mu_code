import turtle

def fizzbuzz(n):
    results = []
    if n % 5 == 0:
        results.append("fizz")
    if n % 7 == 0:
        results.append("buzz")
    return results

def square(size, left_or_right, edge_colour, fill_colour):
    turn = turtle.left if left_or_right == "left" else turtle.right
    turtle.color(edge_colour, fill_colour)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turn(90)
    turtle.end_fill()
    turtle.color("black", "white")

turtle.shape("turtle")
turtle.up()
turtle.setpos(-300, 0)
turtle.down()
for i in range(1, 100):
    fb = fizzbuzz(i)
    if "fizz" in fb:
        square(10, "left", "yellow", "blue")
    if "buzz" in fb:
        square(10, "right", "orange", "green")
    turtle.forward(10)
    turtle.up()
    turtle.forward(1)
    turtle.down()