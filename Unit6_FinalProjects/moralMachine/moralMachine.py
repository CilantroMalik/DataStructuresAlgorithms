"""
--- Moral Machine ---
Thought experiment that implements a prototypical algorithm that a self-driving car would use to decide what to do in a
difficult scenario where all courses of action would involve some loss of life. Morality is entirely subjective even in
the face of seemingly objective, factual information such as laws and perceived expected value to society; therefore,
this algorithm represents one of many paths that a hypothetical AI could take to offering a solution to this problem.
"""


# Converts the given occupant string to an ID number that is easier to work with programmatically
def mapToID(occupant):
    if occupant == "Infant Child":
        return 0
    if occupant == "Small Child":
        return 1
    if occupant == "Teenage Child":
        return 2
    if occupant == "Adult":
        return 3
    if occupant == "Elderly Adult":
        return 4
    if occupant == "Small animal":
        return 5
    if occupant == "Large animal":
        return 6


# main function that encapsulates the algorithm that chooses the action the car will take
def moralBrake(carOccupants: list, crosswalkOccupants: list, greenLight: bool):
    driveStraight = True  # will store the final decision once we make it
    # -- algorithm start --
    # first, process the occupant lists
    for i, entity in enumerate(carOccupants):
        carOccupants[i] = mapToID(entity)
    for i, entity in enumerate(crosswalkOccupants):
        crosswalkOccupants[i] = mapToID(entity)
    # then begin to work through cases one by one
    # TODO: flesh this out

    # finally, finish off the function
    return (
        "The vehicle will maintain its current course to drive through the intersection" if driveStraight
        else "The vehicle will change its course to drive into the barricade."
    )  # convert the boolean to the corresponding string output for what action the car will take
