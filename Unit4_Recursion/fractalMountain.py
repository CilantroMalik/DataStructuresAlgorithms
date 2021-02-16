import turtle
import math
import random

"""
--- Fractal Mountain ---
Creates a modified version of a Sierpinski triangle fractal that has random horizontal and vertical noise
for each point, yielding a fractal-mountain-esque image but in the shape and style of Sierpinski's triangle.
"""


# --- helper functions ---

# quasi-bisect a segment with given endpoints --> returns midpoint with some vertical noise
def getMid(endpts, noise):
    # use midpoint formula from coordinate geometry then add the noise to the y-coordinate
    return [(endpts[0][0] + endpts[1][0]) / 2,
            (endpts[0][1] + endpts[1][1]) / 2 + (random.random() * noise - (noise / 2))]


# given a list of points and a turtle, draw the polygon connecting those points
def draw(points, my_turtle):
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])  # go to the first point
    my_turtle.down()
    color = random.randint(150, 230)  # randomly fill a shade of gray
    my_turtle.fillcolor(color, color, color)
    my_turtle.begin_fill()
    for point in points:
        my_turtle.goto(point[0], point[1])  # go to each point in the figure with pen down
    my_turtle.goto(points[0][0], points[0][1])  # then come back to the first, to complete the shape
    my_turtle.up()
    my_turtle.end_fill()


# --- main code ---
# recursive function that draws the mountain
# takes in the degree (used to reach the base case), a turtle to use for drawing,
# the points that make up the triangle it is to work on, and the noise amount
def mountain(degree, turtle, tri, noise):
    if degree == 0:
        draw(tri, turtle)  # simply draw the polygon defined by the points above
    else:  # recursive case
        # find the midpoints (with noise) of the sides of the triangle
        midpts = [getMid(tri[:2], noise), getMid(tri[1:], noise), getMid(tri[0::2], noise)]
        # make a list out of the full polygon: the original corners of the triangle with the midpoints
        newPoints = [tri[0], midpts[0], tri[1], midpts[1], tri[2], midpts[2]]
        # make three new mountains of one lower degree using the corresponding points for three sub-triangles
        # and also decrease the noise by some factor because the scale is going down so noise should scale as well
        mountain(degree - 1, turtle, [newPoints[0], newPoints[1], newPoints[5]], noise * 0.75)
        mountain(degree - 1, turtle, [newPoints[1], newPoints[2], newPoints[3]], noise * 0.75)
        mountain(degree - 1, turtle, [newPoints[5], newPoints[3], newPoints[4]], noise * 0.75)


# create a turtle and a screen, and set the pen speed to some ridiculous number
t = turtle.Turtle()
window = turtle.Screen()
t.speed(10 ** 30)
# create starting points of an equilateral triangle using math
# (altitude of equilateral triangle starts at the middle of the side and its length is √3 times the side length)
startingPoints = [[-200, -200], [200, -200], [0, -200 + 200 * math.sqrt(3)]]
# then call mountain() with those points. the noise is arbitrary but this value was found to create a nice image
mountain(4, t, startingPoints, 40)
window.exitonclick()
