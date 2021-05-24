"""
--- Moral Machine ---
Thought experiment that implements a prototypical algorithm that a self-driving car would use to decide what to do in a
difficult scenario where all courses of action would involve some loss of life. Morality is entirely subjective even in
the face of seemingly objective, factual information such as laws and perceived expected value to society; therefore,
this algorithm represents one of many paths that a hypothetical AI could take to offering a solution to this problem.
"""


# converts the given occupant string to an ID number that is easier to work with programmatically
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


# returns a "weight" corresponding to each occupant ID that encapsulates its relative value when deciding whom to save
def weight(occupant):
    if occupant == 0:
        return 7
    if occupant == 1:
        return 6
    if occupant == 2:
        return 5
    if occupant == 3:
        return 7
    if occupant == 4:
        return 3
    if occupant == 5:
        return 1
    if occupant == 6:
        return 2


# main function that encapsulates the algorithm that chooses the action the car will take
def moralBrake(carOccupants: list, crosswalkOccupants: list, greenLight: bool):
    # -- process the occupant lists --
    for i, entity in enumerate(carOccupants):
        carOccupants[i] = mapToID(entity)
    for i, entity in enumerate(crosswalkOccupants):
        crosswalkOccupants[i] = mapToID(entity)
    # -- create helper variables and store useful quantities --
    driveStraight = True  # keep track of the final decision once we make it; this value will be returned
    # calculate and store the number of humans and animals in each group
    numHumansCar, numHumansCrosswalk = len([0 for i in carOccupants if i <= 4]), len([0 for i in crosswalkOccupants if i <= 4])
    numAnimalsCar, numAnimalsCrosswalk = len([0 for i in carOccupants if i >= 5]), len([0 for i in crosswalkOccupants if i >= 5])
    # calculate the weights of each group of people
    weightsCar, weightsCrosswalk = sum([weight(i) for i in carOccupants]), sum([weight(i) for i in crosswalkOccupants])
    # -- algorithm start --
    # we begin to work through cases one by one
    # -> Case 1: pedestrians abiding by the law
    if greenLight:
        # Sub-case 1a: different numbers of humans and animals differ by at most 1 --> kill less people no matter what
        if numHumansCar != numHumansCrosswalk and abs(numAnimalsCar - numAnimalsCrosswalk) <= 1:
            driveStraight = numHumansCar > numHumansCrosswalk
        # Sub-case 1b: different numbers of humans and animals differ by 2 or more --> use weighting system
        # Sub-case 1c: same numbers of humans --> use weighting system
        if abs(numAnimalsCar - numAnimalsCrosswalk) >= 2 or numHumansCar == numHumansCrosswalk:
            driveStraight = weightsCar > weightsCrosswalk
    # -> Case 2: pedestrians flouting the law
    else:
        # Sub-case 2a: same number of humans & animals
        pass  # TODO finish this

    # finally, finish off the function
    return (
        "The vehicle will maintain its current course to drive through the intersection" if driveStraight
        else "The vehicle will change its course to drive into the barricade."
    )  # convert the boolean to the corresponding string output for what action the car will take
