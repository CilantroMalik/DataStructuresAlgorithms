from linkedList import UnorderedList

"""
--- Stack Implementation using Linked List ---
Creating a stack, a data structure that only allows adding to and removing from one end and works first-in-last-out,
internally using a linked list to store the items.
"""


class Stack:
    # NOTE: the top of the stack is the front (head) of the linked list.
    def __init__(self):
        # create an empty linked list to represent the stack
        self.__stack = UnorderedList()
        self.__length = 0

    def __str__(self):
        return str(self.__stack)

    def push(self, item):
        # add the given item to the beginning of the list (top of the stack)
        self.__stack.add(item)
        # and increment the length
        self.__length += 1

    def pop(self):
        # simply remove and return the first item of the list (and decrement length)
        self.__length -= 1
        return self.__stack.pop()

    def peek(self):
        # an additional method was added to the linked list implementation hat returns the node at the
        # head reference (the top node). then we just return the item contained in that node.
        return self.__stack.getHead().getData()

    def isEmpty(self):
        # simply defer to the linked list isEmpty method
        return self.__stack.isEmpty()

    def size(self):
        # return the length that we have been keeping track of
        return self.__length
