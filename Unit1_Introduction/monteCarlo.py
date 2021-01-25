# TODO add docstring and clean up comments

import random

while True:
    # ask for number of points, or quit
    num_points = input("Number of points to generate (or q to quit): ")
    if num_points == "q":
        break
    else:
        num_points = int(num_points)

    # create a list of length num_points of random pairs of coordinates from -1 to 1, then prepare to print them
    pts = [(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(num_points)]

    print("Generated coordinates:")
    print("-----------------")

    # TODO optimize algorithm?
    # which points are in the circle?
    num_in_circle = 0
    for pt in pts:  # might as well print the points at the same time as you iterate through them to check if they are in the circle
        print(pt)
        if pt[0] ** 2 + pt[1] ** 2 <= 1:  # simplified distance formula if we consider the center as the origin of our coordinate system
            num_in_circle += 1

    # final calculations and outputs
    pi = 4 * num_in_circle / num_points

    print("-----------------")
    print("Points in circle:", num_in_circle)
    print("Approximation: π =", pi)
