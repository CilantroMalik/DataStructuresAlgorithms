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
    if occupant == 0:  # Infant Child
        return 7  # highest weight since they are newborn and have their entire life to live
    if occupant == 1:  # Small Child
        return 6  # slightly lower than infants but still high for similar reasons
    if occupant == 2:  # Teenage Child
        return 5  # similar progression from the previous two for the same reason
    if occupant == 3:  # Adult
        return 7  # also highest weight because they are productive members of the workforce and contributors to society
    if occupant == 4:  # Elderly Adult
        return 3  # weighted lower because they have already made their contribution and are now a net negative value proposition
    if occupant == 5:  # Small animal
        return 1  # lowest weight because although we do still love our animals, they should be less important than humans
    if occupant == 6:  # Large animal
        return 2  # slightly higher because a large animal could be livestock for example, which has more value in an objective sense


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
        # If the weights for the groups are within 2 of each other, kill the law-breakers; if not, save the higher weighted group
        driveStraight = True if abs(weightsCar - weightsCrosswalk) <= 2 else (weightsCar > weightsCrosswalk)

    # finally, finish off the function
    return (
        "The vehicle will maintain its current course to drive through the intersection" if driveStraight
        else "The vehicle will change its course to drive into the barricade."
    )  # convert the boolean to the corresponding string output for what action the car will take
