from linkedList import UnorderedList

"""
--- Queue Implementation using Linked List ---
Implementation of the queue, this time using a linked list instead of a native Python list. All functionality is
the same, as are the time complexities of all the methods, so on the surface the two implementations look identical.
"""


class Queue:
    # NOTE: front of queue is beginning of linked list
    def __init__(self):
        # represent the queue with a linked list
        self.__queue = UnorderedList()
        self.__length = 0

    def enqueue(self, item):
        # add item to end of queue (that means append to linked list) and increment length
        self.__queue.append(item)
        self.__length += 1

    def dequeue(self):
        # remove item from front of queue (that means pop from linked list) and decrement length
        self.__length -= 1
        return self.__queue.pop()

    def front(self):
        # return the data of the first node in the list
        return self.__queue.getHead().getData()

    def isEmpty(self):
        # defer to the isEmpty method of the list
        return self.__queue.isEmpty()

    def size(self):
        # we have been keeping track of this
        return self.__length

    def queue(self):
        # defer to the linked list string representation
        return str(self.__queue)
