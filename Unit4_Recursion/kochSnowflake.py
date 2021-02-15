import turtle

"""
--- Koch Snowflake with Turtle ---
Program that draws the Koch snowflake, a recursively generated fractal that starts with an equilateral triangle,
and replaces the middle third of each segment with another equilateral triangle (just without the base). Then this
is recursively applied to each of the newly created segments (there will be four segments after the partition) and
so on infinitely, or as far as one is willing to go. The product is a sort of snowflake whose edges are self-similar.
Here, Python's turtle module is used to draw the shape through a relatively straightforward recursive algorithm.
"""


# helper function: draw a segment defined by two endpoints
def draw(points, turtle):
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.goto(points[1][0], points[1][1])
    turtle.up()


# main function: draw one side of the Koch snowflake (i.e. a Koch curve)
def snowflake(deg, turt, distance):
    if deg == 0:  # base case: just draw a line
        turt.forward(distance)
    else:  # recursive case: draw four more Koch curves, each scaled down by 3
        snowflake(deg - 1, turt, distance / 3)  # first segment
        turt.left(60)  # make the "hump"; equilateral triangle angles are 60º
        snowflake(deg - 1, turt, distance / 3)
        turt.right(120)  # go down the "hump"; -60º = 120º
        snowflake(deg - 1, turt, distance / 3)
        turt.left(60)  # go back to straight
        snowflake(deg - 1, turt, distance / 3)


# setup: create and configure turtle
t = turtle.Turtle()
t.speed(0)  # max speed so execution does not take minutes
t.up()
t.goto(-160, 100)  # move it to the starting point (it defaults to the center)
t.down()
window = turtle.Screen()  # create the graphics window

# the recursive function only draws one side of the "snowflake" each time, so we have to call it thrice
# and in order to create 3 Koch curves at 60º interior angles (i.e. in a triangle) --> 120º exterior angles
for i in range(3):
    snowflake(4, t, 340)
    t.right(120)

window.exitonclick()  # program will exit if the user clicks the window when the drawing is finished
