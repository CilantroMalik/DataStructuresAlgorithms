"""
--- Flex Insertion Sort ---
Implementation of the Insertion Sort algorithm that also includes an argument
dictating whether to sort in ascending or descending order at the user's choice.
"""


def flexInsertionSort(alist, direction):
    if not (direction == "+" or direction == "-"):
        raise ValueError("Invalid direction argument, can only be + or -")
    # go through every index past the first one and insert that element into the
    # sorted sublist that starts with the first item
    for index in range(1, len(alist)):
        # store the value and position of the currently focused element
        currentValue = alist[index]
        position = index
        # try every position before that index until you find the place that the value fits
        # (i.e. where the previous element is less than it, or greater if sorting in descending order)
        if direction == "+":
            while position > 0 and alist[position - 1] > currentValue:
                alist[position] = alist[position - 1]  # move the other elements over
                position -= 1
        elif direction == "-":
            while position > 0 and alist[position - 1] < currentValue:
                alist[position] = alist[position - 1]  # move the other elements over
                position -= 1

        alist[position] = currentValue  # set the desired position to our focused element

    return alist  # finally, return the sorted list
