import turtle
import math
import random


# --- helper functions ---

# quasi-bisect a segment with given endpoints --> returns midpoint with some vertical noise
def getMid(point1, point2, noise):
    # use midpoint formula from coordinate geometry then add the noise to the y-coordinate
    return [(point1[0] + point2[0]) / 2 + (random.random() * noise - (noise / 2)),
            (point1[1] + point2[1]) / 2 + (random.random() * noise - (noise / 2))]


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


# --- one single mathematical constant that is used in one single instance ---
rt3 = math.sqrt(3)


# --- main code ---
def mountain(deg, turtle, points, noise):
    if deg == 0:
        draw(points, turtle)
    else:
        midpts = [getMid(points[0], points[1], noise), getMid(points[1], points[2], noise),
                  getMid(points[2], points[0], noise)]
        mountain(deg - 1, turtle, [points[0], midpts[0], midpts[2]], noise * 0.8)
        mountain(deg - 1, turtle, [midpts[1], midpts[2], midpts[0]], noise * 0.8)
        mountain(deg - 1, turtle, [midpts[0], points[1], midpts[1]], noise * 0.8)
        mountain(deg - 1, turtle, [midpts[2], midpts[1], points[2]], noise * 0.8)


# create a turtle and a screen, and set the pen speed to some ridiculous number
t = turtle.Turtle()
window = turtle.Screen()
t.speed(10 ** 30)
# create starting points of an equilateral triangle using math
startingPoints = [[-200, -200], [200, -200], [0, -200 + 200 * rt3]]
# then call mountain() with those points. the degree and noise can be changed as desired but these values look kind of nice.
mountain(3, t, startingPoints, 35)
window.exitonclick()
