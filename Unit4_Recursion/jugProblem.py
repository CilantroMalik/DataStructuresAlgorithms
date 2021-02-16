"""
--- Jug Problem ---
A recursive algorithm for the "jug problem", where we have two jugs of set sizes with no markings on them, and we have to
get a certain number of gallons in one of the jugs. The only way to "measure" is using the full capacity of any jug
since there are no measuring lines with which to ascertain any other amount. For example, a possible configuration could be
jugs of 5 and 3 gallon capacities, and the goal is to get 4 gallons in the larger jug. This would be solved by filling the
large jug, pouring it into the small jug (leaving two gallons in the larger one) then emptying the small one and pouring
into there (leaving two gallons in the small jug) and finally filling the 5 gallon jug and pouring into the small one until
it is full (which will only be 1 more gallon, leaving 4 gallons in the larger jug).
"""


# standard stack implementation
class Stack:
    def __init__(self):
        self.items = []

    def stack(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# assume jugs of size x and y gallons, where x is the larger jug, and let the desired final amount of water be g gallons.
# also let the larger and smaller jugs be named A and B respectively. in order to get g gallons of water in jug A,
# we must first get y-(x-g) gallons in jug B and fill A, then pour A into B; and in order to get the y-(x-g) in B,
# we must get y-(x-g) gallons in A. now recursively set g (our goal amount) equal to y-(x-g), the new desired amount,
# and rerun the algorithm to find how to reach this smaller goal. stop when g is set to x, the maximum capacity of jug A,
# and then we are done since we can trivially reach this goal and we just ride back up the call stack to solve the problem.

moves = Stack()  # each item is [action, jug A water level, jug B water level]


# main function: calls a helper function with more parameters to help with the recursion
def jug(jug_a_capacity, jug_b_capacity, final_desired_amt):
    x = jug_a_capacity
    y = jug_b_capacity
    g = final_desired_amt
    helper(x, 0, x, y, g)  # call helper with the adequate variables

    # once it is done we will have all the moves stored in our stack so we can pop them all off
    finalMoveSet = []
    while not moves.isEmpty():
        finalMoveSet.append(moves.pop())
    finalMoveSet = reverseList(finalMoveSet)  # reverse to get the original order
    # print the information in a readable way
    for move in finalMoveSet:
      if len(move) == 1:  # if this is a base case marker and not a move
        print(move[0])
        continue
      print(f"{move[0]}\nJug A now has {move[1]}\nJug B now has {move[2]}\n------------------")
    print("Finished!")


# globals for the helper function
currentA = 0
currentB = 0


# this function does all the work
def helper(curr_a, curr_b, x, y, g):
    global currentA, currentB
    # update globals with the function parameters
    currentA = curr_a
    currentB = curr_b

    desired = y - (x - g)  # as per the algorithm discussed above
    if currentB != desired and currentA != desired:  # recursive case
        # if neither jug has the desired amount, make a recursive call with the goal being the current desired amount
        # effectively solving a smaller stepping stone of the larger problem
        helper(curr_a, curr_b, x, y, desired)
    if currentB == desired:  # base case 1: jug B has desired amount --> fill A and pour into B and we're done
        moves.push([">> Base case reached."])
        currentA = x  # fill jug A
        moves.push(["A --> full", currentA, currentB])
        currentA, currentB = pour([currentA, x], [currentB, y])  # pour A into B
        moves.push(["A --> B", currentA, currentB])

    elif currentA == desired:  # base case 2: jug A has desired amount --> a bit more complicated
        moves.push([">> Base case reached."])
        # empty B then pour A into B, so now jug B has the desired amount; then just do the same steps as above
        currentB = 0
        moves.push(["B --> empty", currentA, currentB])
        currentA, currentB = pour([currentA, x], [currentB, y])
        moves.push(["A --> B", currentA, currentB])
        # fill A and pour into B and we're done
        currentA = x
        moves.push(["A --> full", currentA, currentB])
        currentA, currentB = pour([currentA, x], [currentB, y])
        moves.push(["A --> B", currentA, currentB])


# works out the pouring of one jug into another. returns a tuple so it can be easily unpacked
def pour(fromJug, toJug):  # each argument is an array of [current amount, max amount]
    delta = toJug[1] - toJug[0]  # how much needs to be poured?
    # if there is enough in the first jug to fill the second, do that
    # or if not, just pour everything from the first jug into the second
    return (fromJug[0]-delta, toJug[0]+delta) if fromJug[0] >= delta else (0, toJug[0]+fromJug[0])


# from ps4_1, in classic recursive fashion for thematic appropriateness
def reverseList(alist):
    if len(alist) == 2:
        return [alist[1], alist[0]]
    else:
        return reverseList(alist[1:]) + [alist[0]]


# testing on a relatively simple configuration of jugs with a clear solution
jug(4, 3, 2)
