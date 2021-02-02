"""
--- Implementation of the Unordered List ADT with a Linked List ---
Gives one possible implementation of an unordered list, a data structure where each item holds positional
information as related to the other pieces of information in the list, but is not fundamentally ordered by
the nature of its items. Internally uses a collection of nodes that are "linked" to each other by references.
"""


class UnorderedList:
    # -- inner class for Node --
    class Node:
        # simple class with two fields and their getter and setter methods
        def __init__(self, data=None, nextNode=None):
            self.__data = data
            self.__next = nextNode

        # the node should be represented simply by its data
        def __repr__(self):
            return self.__data

        def getData(self):
            return self.__data

        def getNext(self):
            return self.__next

        def setData(self, newData):
            self.__data = newData

        def setNext(self, newNext):
            self.__next = newNext

    # -- initializes the list with a head reference and a property to keep track of the length
    def __init__(self):
        # NOTE: in this implementation, the head reference points to the Node object of the first node of the list,
        #       and as such its next reference points to the second node of the list. This is different from some
        #       other implementations in which head itself is empty and its next reference points to the first node.
        self.__head = None
        self.__length = 0  # tracks size of our list

    # -- creates the string representation of the list items --
    def __str__(self):
        if self.isEmpty():
            return "[]"  # a simple shortcut for a special case
        output = "["  # start with a bracket - we will build up this string
        current = self.__head
        # traverse the list and add each item to the output string with a comma -> mimic Python's representation
        while current is not None:
            output += f"{current.getData()}, "
            current = current.getNext()
        output = output[:-2] + "]"  # get rid of trailing comma and add closing bracket
        return output

    # -- checks whether the list is empty --
    def isEmpty(self):
        return self.__head is None

    # -- adds an item to the front of the list (at position 0) --
    def add(self, item):
        # create a new node with its next being the current first node (the head)
        # then make the head reference point to this new first node
        temp = self.Node(item, self.__head)
        self.__head = temp
        self.__length += 1  # since we are adding an element, increment length

    # -- appends an item to the end of the list (at position length-1) --
    def append(self, item):
        current = self.__head
        if self.__head is None:  # special case: list is empty
            self.__head = self.Node(item)  # just set the head reference to the new node
            self.__length += 1
            return
        # normal case: traverse until current is the last node (it has no next node)
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(self.Node(item))  # then simply set the next node to the new one
        self.__length += 1  # since we are adding an element, increment length

    # -- inserts an item into the given position in the list --
    def insert(self, pos, item):
        current = self.__head
        previous = None
        # get the two references to be the previous node from the target
        # and the node at the target position itself
        for i in range(pos):
            previous = current
            current = current.getNext()
        # now we set the next reference of the previous node to our new item
        # and the next reference of our new item to what used to be at
        # this position (which is the current node)
        if previous is None:
            self.add(item)  # special case if position is zero: just defer to add method
            return
        # in all other cases, follow procedure above
        temp = self.Node(item, current)
        previous.setNext(temp)
        self.__length += 1  # since we are adding an element, increment length

    # -- returns the size of the list --
    def size(self):
        return self.__length  # we have been keeping track of the size

    # -- checks whether or not the given item is in the list --
    def search(self, item):
        current = self.__head
        found = False
        # traverse the list until we either reach the end or the item is found
        while current is not None and not found:
            if current.getData() == item:
                found = True  # if we ever find the item, change the flag to say so
            else:
                current = current.getNext()
        # finally, return that flag. if the item wasn't in the list,
        # the flag will still be False.
        return found

    # -- returns the index of the given item in the list, or -1 if it is not found --
    def index(self, item):
        # this is a modified version of the given `search` method
        current = self.__head
        index = 0  # add an index variable to keep track of where we are
        while current is not None:
            if current.getData() == item:
                return index
            else:
                current = current.getNext()
                index += 1  # when we've found the item, `index` will store its index
        return -1  # if the item is not found at all; similar behavior to Python list find()

    # -- removes the given item from the list, or does nothing if it is not present in the list --
    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        # traverse the list until we've found the node containing the item to remove
        # (or we've gone through the entire list not having found it)
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:  # if the item is not in the list, do nothing and exit
            return
        # special case: if the node to remove is the first node, we just change the head
        if previous is None:
            self.__head = current.getNext()
        else:
            # in any other case, we just skip over the current node by setting the
            # next reference of the previous to the next of the current
            # which makes the current have no reference pointing to it, which removes it
            previous.setNext(current.getNext())
        self.__length -= 1  # since we are removing a node, decrement length

    # -- removes and returns the first element of the list (position 0) --
    def pop(self):  # default pops the first element
        # just set the head reference to the second node, so the first node
        # now has no external reference pointing to it and so it is removed
        temp = self.__head  # use a temp variable since we have to return the item
        self.__head = temp.getNext()

        self.__length -= 1  # since we are removing a node, decrement length
        return temp.getData()  # then finally return our item

    # -- removes and returns the element at the given position --
    def pop(self, pos=0):
        current = self.__head
        previous = None
        # now get previous and current to point to the node before the target
        # and the target node to remove, based on the position
        for i in range(pos):
            previous = current
            current = current.getNext()
        # once we have the references, just set the next reference of the
        # previous node to the next reference of the current node,
        # effectively skipping over the current node and removing it from
        # the linking chain, which takes it out of the list
        if pos == 0:  # special case for popping first item: no previous node
            self.__head = current.getNext()
        else:  # normal case
            previous.setNext(current.getNext())

        self.__length -= 1  # since we are removing a node, decrement length
        return current.getData()  # then finally return what we need to
