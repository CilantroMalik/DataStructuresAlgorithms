from doublyLinkedList import DoublyLinkedList

"""
--- O(1) Queue ---
Slight modification to previous implementations of the Queue abstract data type, this time utilizing a
doubly linked list to make both enqueue and dequeue O(1) operations. The interface is exactly identical to
the other implementations; the only improvements are that we now use a DLL under the hood to store the items.
"""


# queue implementation using doubly linked list
class Queue:
    # initialize an empty queue (here represented by a doubly linked list)
    def __init__(self):
        self.__queue = DoublyLinkedList()

    def enqueue(self, item):
        # use append since we are adding to the end of the list (rear of queue).
        # append is O(1) for a DLL since we just use the last reference and do not need to traverse the list.
        self.__queue.append(item)

    def dequeue(self):
        # use pop since we are removing from the beginning of the list (front of queue).
        # popping the first element is O(1) for any linked list since we always have reference to the head node.
        return self.__queue.pop()

    def front(self):
        # return the data inside the first (head) node of the list
        return self.__queue.getHead().getData()

    def isEmpty(self):
        # just defer to our list's isEmpty method
        return self.__queue.isEmpty()

    def size(self):
        # defer to our list's size method
        return self.__queue.size()

    def queue(self):
        # defer to our list's string representation method
        return str(self.__queue)
