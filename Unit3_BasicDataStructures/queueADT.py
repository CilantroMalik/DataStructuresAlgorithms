"""
--- Implementation of the Queue Abstract Data Type using Python Native Lists ---
A straightforward implementation of a queue, a data structure that allows adding items on one end only
and removal on the other end, like a real-world queue. Items in a queue follow a "first-in-first-out" paradigm.
"""


class Queue:

    # constructor: make an empty list to hold the queue items
    def __init__(self):
        self.items = []

    # return a string representation of the queue
    def queue(self):
        return str(self.items)

    # check if the queue is empty
    def isEmpty(self):
        return self.items == []

    # return the number of items in the queue
    def size(self):
        return len(self.items)

    # (note: these two methods could be swapped so that the rear of the queue is the beginning of the list, which would
    # also in turn swap the time complexities, but one will always be O(1) and the other O(n), so the choice is arbitrary.)

    # append an item to the rear of the queue (here represented by the end of the list)
    def enqueue(self, item):
        self.items.append(item)  # O(1)

    # remove an item from the front of the queue (i.e. beginning of the list)
    def dequeue(self):
        return self.items.pop(0)  # O(n)
