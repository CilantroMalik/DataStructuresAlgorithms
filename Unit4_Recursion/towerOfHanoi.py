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


pole1 = Stack()  # start
pole2 = Stack()  # finish
pole3 = Stack()  # auxiliary


# main function
def solveHanoi(numDisks):
    # initial setup: put disks on starting pole
    for i in range(numDisks, 0, -1):  # shift index so disks are 1, 2, 3, ...
        pole1.push(i)

    # print starting position
    print("------------------")
    print("-- Objective: move tower from left to middle using right --")
    print("------------------")
    print("Left:", pole1.stack())
    print("Middle:", pole2.stack())
    print("Right:", pole3.stack())
    print("------------------")

    # helper function does the actual work
    moveTower(numDisks, pole1, pole2, pole3)


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fr, to):
    print("Moving disk from", pole(fr), "to", pole(to))
    to.push(fr.pop())
    print("Left:", pole1.stack())
    print("Middle:", pole2.stack())
    print("Right:", pole3.stack())
    print("------------------")


# identifies the pole passed in as a parameter as Left/Middle/Right
def pole(aPole):
    return "left" if aPole == pole1 else ("middle" if aPole == pole2 else "right")


solveHanoi(4)  # can test for any number of disks, but for the computer's sake, don't go too high.
