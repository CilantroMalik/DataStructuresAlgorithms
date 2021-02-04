from linkedList import UnorderedList

"""
--- Deque Implementation with Linked List ---
Deque (double-ended queue) data structure implemented with a linked list. This combines stacks and queues in a way,
and makes it possible to add to or remove from both ends of the deque (hence double-ended).
"""


class Deque:
    # in this implementation, the front and rear of the deque correspond to the front and rear of the linked list
    def __init__(self):
        self.__deque = UnorderedList()
        self.__length = 0

    def addFront(self, item):
        # use the add method here
        self.__deque.add(item)
        self.__length += 1

    def addRear(self, item):
        # use the append method here
        self.__deque.append(item)
        self.__length += 1

    def removeFront(self):
        # use the pop method here
        self.__length -= 1
        return self.__deque.pop()

    def removeRear(self):
        # unfortunately, with a singly linked list it is difficult to make
        # this method O(1), so this one will be O(n) since it needs a traversal
        self.__length -= 1
        # since we decrement length first, we index self.__length not self.__length-1
        return self.__deque.pop(self.__length)

    def isEmpty(self):
        # defer to the list isEmpty method
        return self.__deque.isEmpty()

    def size(self):
        # defer to the list size method
        return self.__length

    def deque(self):
        # defer to the list string representation method
        return str(self.__deque)
