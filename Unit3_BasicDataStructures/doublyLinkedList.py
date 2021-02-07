"""
--- Doubly Linked List ---
A variation on the idea of a linked list, where instead of each node holding one reference to the next node,
each node holds two references to the next and previous nodes, so the list can be traversed in two directions.
This opens up access from both ends of the list rather than only the front and generally provides more flexibility.
"""


class DoublyList:
    # inner class for a node in the list
    class Node:

        # all the methods are fairly self explanatory: initializer then getters and setters for the three fields
        def __init__(self, data, next=None, back=None):
            self.data = data
            self.next = next
            self.back = back

        def getData(self):
            return self.data

        def getNext(self):
            return self.next

        def getBack(self):
            return self.back

        def setData(self, data):
            self.data = data

        def setNext(self, newnext):
            self.next = newnext

        def setBack(self, previous):
            self.back = previous

    # initializes the list with a head reference for the first node, a last reference, and a length
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    # handles the string representation of the doubly linked list - aims to emulate Python lists' display format
    def __str__(self):
        if self.isEmpty():
            return "[]"  # a simple shortcut for a special case
        output = "["  # start with a bracket - we will build up this string
        current = self.head
        # traverse the list and add each item's data to the output string
        # along with a comma to get the exact format of Python's representation
        while current is not None:
            output += f"{current.getData()}, "
            current = current.getNext()
        output = output[:-2] + "]"  # get rid of trailing comma and add bracket
        return output

    # prints the list in reverse, utilizing the bidirectional traversal capabilities of the list
    def doubly_list_reverse(self):
        if self.isEmpty():
            return "[]"  # a simple shortcut for a special case
        output = "["  # start with a bracket - we will build up this string
        current = self.last
        # traverse the list and add each item's data to the output string along with a comma
        # in order to mimic the exact format of Python's representation
        while True:
            output += f"{current.getData()}, "
            if current == self.head:
                break
            current = current.getBack()
        output = output[:-2] + "]"  # get rid of trailing comma and add bracket
        return output

    # adds an item to the list, handling a few special cases
    def add(self, item):
        temp = self.Node(item)
        # if the list is empty...
        if self.head is None:
            self.head = temp  # set the head reference to our new node
            self.last = self.head  # this is also the last element
            self.head.setBack(self.last)  # set the head to reference the last node
        else:  # if the list is not empty
            temp.setNext(self.head)  # set the new node's next to the current first node
            temp.setBack(self.last)  # the new head now has to point to the last
            self.head.setBack(temp)  # set the old first node's back to the new first node
            self.head = temp  # finally, update the head reference
        self.length += 1  # increment length since we are adding an item

    # searches for an item and returns a boolean for whether or not it is in the list
    def search(self, item):
        # loop through until we find the element or traverse the entire list
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False  # this will only trigger if we never found the element

    # simple convenience method that checks whether the list is empty
    def isEmpty(self):
        return self.head is None  # just check if the head is empty

    # enables access to the length field through a method
    def size(self):
        return self.length  # we have been keeping track of this

    # removes an item from the list, accounting for a number of special cases
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        # search until either current refers to the target node or we've traversed the whole list
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:  # if the item is not present, just do nothing
            return

        # -> if there is only one element, just clear the list out
        if self.head == self.last:
            self.head = None
            self.last = None
        # -> if the target is the first element (i.e. the previous reference was never set)
        elif previous is None:
            # set the second node (the new first node after removal) to point back to the last, as the head shouild
            current.getNext().setBack(self.last)
            self.head = current.getNext()  # then update the head reference
        # -> if the target is the last element
        elif current == self.last:
            previous.setNext(None)  # set the previous node to have no successor
            self.head.setBack(previous)  # update head to point to the new last node
            self.last = previous  # then update the last reference
        # -> in all other cases (i.e. node is somewhere in the middle of the list)
        else:
            previous.setNext(current.getNext())  # skip over the target node
            current.getNext().setBack(previous)  # have to build the connection forward and backward
        self.length -= 1  # finally, decrement length because we are removing a node

    # finds the index of an item in the list, or returns -1 if the item is not present
    def index(self, item):
        pos = 0
        current = self.head
        # loop until we have found the element or traversed the whole list
        while current is not None:
            if current.getData() == item:
                return pos
            else:
                current = current.getNext()
                pos += 1
        return -1  # item not in list

    # removes and returns the element at the given position, or the first element by default
    def pop(self, pos=None):
        # if the list is empty, do nothing
        if self.head is None:
            return
        # if there is only one element
        if self.head == self.last:
            # clear the list, but save the value so we can return it
            temp = self.head.getData()
            self.head = None
            self.last = None
            self.length -= 1  # decrement length since we are removing an element
            return temp
        # no argument means default -> remove first element (special case)
        if pos is None:
            temp = self.head.getData()  # save the data so we can return it
            self.head.getNext().setBack(self.last)  # skip over the first node
            self.head = self.head.getNext()  # update the head reference
            self.length -= 1
            return temp
        # all other cases
        else:
            current = self.head
            previous = None
            # if not first or last position (the "normal" case)
            if 0 < pos < self.length - 1:
                # inchworm until we reach the desired position
                for i in range(pos):
                    previous = current
                    current = current.getNext()
                previous.setNext(current.getNext())  # skip over the node
                current.getNext().setBack(previous)  # have to do it both ways
                self.length -= 1  # decrement length
                return current.getData()
            elif pos == 0:
                return self.pop()  # redundancy
            elif pos == self.length - 1:  # popping at the last position (special case)
                temp = self.last.getData()  # save the data so we can return it later
                self.last.getBack().setNext(None)  # skip over the last node
                self.head.setBack(self.last.getBack())  # update head to point to the new last node
                self.last = self.last.getBack()  # then update the last reference
                self.length -= 1  # decrement length
                return temp
            else:  # this means the index was out of bounds
                return  # so just do nothing (potentially could raise an error)

    # adds the given item to the end of the list
    def append(self, item):
        temp = self.Node(item)
        # if the list is empty, just populate the head and last references
        if self.head is None:
            self.head = temp
            self.last = self.head
            self.head.setBack(self.last)  # and set head to reference last
        else:  # if the list is not empty
            self.last.setNext(temp)  # add the new node onto last
            temp.setBack(self.last)  # and complete the connection the other way
            self.head.setBack(temp)  # then update head to reference the new last node
            self.last = temp  # and update the last reference
        self.length += 1  # increment length

    # inserts the given item into the list at the given position
    def insert(self, pos, item):
        current = self.head
        previous = None
        # loop until `current` references the node at the desired position
        for i in range(pos):
            previous = current
            current = current.getNext()
        # if current is the first element (which means previous will be None)
        if previous is None:
            self.add(item)  # just defer to the add method
            return
        # if current is None, that means we want to insert as the last element
        # (because the index went one further than the end of the list)
        if current is None:
            self.append(item)  # just defer to the append method
            return
        # in all other cases
        temp = self.Node(item, current, previous)  # make the node in between current and previous
        previous.setNext(temp)  # then complete those two connections both ways
        current.setBack(temp)

        self.length += 1  # finally, increment length
