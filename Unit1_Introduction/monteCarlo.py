"""
--- Monte Carlo Simulation: Calculating π ---
Uses a brute-force "Monte Carlo" method to calculate π by finding the ratio between the area of a circle of radius 1
and that of a square with side length 2 by randomly placing points in the square and seeing how many land in the circle.
This ratio is π/4, so we can approximate π from there. Simple method, but inefficient and takes a while to become accurate.
"""

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

    # use list comprehension to select only the points that are within the circle (i.e. 1 unit or less away from origin)
    # using a simplified distance formula to test all the points.
    # Then simply take the length of that list to find the number of points in the circle
    num_in_circle = len([point for point in pts if (point[0] ** 2) + (point[1] ** 2) <= 1])

    # final calculations and outputs
    pi = 4 * num_in_circle / num_points

    print("Points in circle:", num_in_circle, "out of", num_points)
    print("Approximation: π =", pi)
