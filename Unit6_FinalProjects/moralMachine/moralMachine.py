"""
--- Moral Machine ---
Thought experiment that implements a prototypical algorithm that a self-driving car would use to decide what to do in a
difficult scenario where all courses of action would involve some loss of life. Morality is entirely subjective even in
the face of seemingly objective, factual information such as laws and perceived expected value to society; therefore,
this algorithm represents one of many paths that a hypothetical AI could take to offering a solution to this problem.
"""

# TODO write an enum for the possible types of occupants


# main function that encapsulates the algorithm that chooses the action the car will take
def moralBrake(carOccupants: list, crosswalkOccupants: list, greenLight: bool):
    driveStraight = True
    # implement algorithm
    return (
        "The vehicle will maintain its current course to drive through the intersection" if driveStraight
        else "The vehicle will change its course to drive into the barricade."
    )
