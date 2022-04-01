import turtle


def draw_petal():
    """a function that draws a petal"""
    turtle.circle(100, 90)  # draws half of the petal
    turtle.left(90)
    turtle.circle(100, 90)  # draws the other half of the petal


def draw_flower():
    """a function that draws a flower"""
    turtle.setheading(0)
    draw_petal()  # first petal
    turtle.setheading(90)
    draw_petal()  # second petal
    turtle.setheading(180)
    draw_petal()  # third petal
    turtle.setheading(270)
    draw_petal()  # forth petal
    turtle.setheading(270)
    turtle.forward(250)  # draws the stem


def draw_flower_advance():
    """a function that draws a flower and then moves to the left
    to a position ready to draw another flower"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """a function that draws a garden of 3 flowers"""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advance()  # first flower
    draw_flower_advance()  # second flower
    draw_flower_advance()  # third flower


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()
