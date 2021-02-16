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


def tree(branchLen, t, currentColor):
    if branchLen > 5:
        if currentColor > 155:
            currentColor = 155  # make sure that the color never goes over 155 so the calculated values never exceed 255
        t.color((currentColor, currentColor+100, currentColor))
        t.forward(branchLen)
        angle = randint(15, 45)
        t.right(angle/2)
        tree(branchLen-randint(13, 17), t, currentColor+20)
        t.left(angle)
        tree(branchLen-randint(13, 17), t, currentColor+20)
        t.right(angle/2)
        t.color((currentColor, currentColor+100, currentColor))
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.colormode(255)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color((0, 100, 0))
    tree(100, t, 0)
    myWin.exitonclick()


main()
