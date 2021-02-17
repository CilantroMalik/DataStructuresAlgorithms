import turtle
from random import randint

"""
--- Recursive Tree with Turtle ---
Program that draws a fractal tree with a simple recursive algorithm that calls itself to draw branches off of each branch,
subtracting the length each time, until the branch length is too short, at which point the base case is reached.
The program makes some modifications to the "pure" algorithm, including randomizing the angle of turn at each branch
and randomizing the decrease in length at each recursive call (in order to add some variety to the tree structure, as it
would be in nature, so it is not perfectly symmetrical every time) and changing the color so it gets lighter as the branches
are further away from the root (so the ones farthest away look like "leaves").
"""


# main function, generates the tree with the given branch length and color, using a turtle that gets passed forward
def tree(branchLen, t, currentColor):
    if branchLen > 5:  # so we have a base case
        if currentColor > 155:
            currentColor = 155  # make sure that the color never goes over 155 so the calculated values never exceed 255
        t.color((currentColor, currentColor+100, currentColor))
        t.forward(branchLen)  # create one branch
        angle = randint(15, 45)  # randomly pick the branch angle
        t.right(angle/2)  # go half that angle first and then make a new tree
        tree(branchLen-randint(13, 17), t, currentColor+20)  # randomly smaller branch length, and lighter color
        t.left(angle)  # go left the full angle to prepare to make the other side's tree
        tree(branchLen-randint(13, 17), t, currentColor+20)  # similar to above
        t.right(angle/2)  # go back to facing the center
        t.color((currentColor, currentColor+100, currentColor))
        t.backward(branchLen)  # retrace the steps


# setup: create turtle and screen
t = turtle.Turtle()
myWin = turtle.Screen()
myWin.colormode(255)  # set RGB color
t.left(90)  # face upward (default orientation for a newly created turtle is facing right)
t.up()
t.backward(100)  # go backwards without drawing so we start in a suitable position
t.down()
t.color((0, 100, 0))  # start at a dark green, progressively get lighter
tree(100, t, 0)  # now set an initial branch length (first parameter; larger means more branches) and create the tree
myWin.exitonclick()  # so the program exits once the turtle is done drawing if we click on the screen
