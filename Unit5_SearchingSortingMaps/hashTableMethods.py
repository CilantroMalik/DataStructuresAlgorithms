"""
--- Hash Table: Implementing the Map ADT ---
This is an implementation of the Map abstract data type, which entails a data structure that has keys and values in
pairwise association. This type of implementation has the advantage that getting, setting, and searching are all O(1)
operations in terms of time complexity, and it accomplishes this by using a "hash function", a mathematical function
that transforms any given key into a numerical value, to decide where to locate each key-value pair, which makes it
trivial to find it later — just reapply the hash function and retrieve from that index.
"""

class HashTable:
    # initialize the hash table with a size of 11 (arbitrary) and two empty Python lists to keep track of keys/values
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # put: add an entry to the hash table with the given key and the given value
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))  # apply the hash function to the key, given the size of the list

        if self.slots[hashvalue] is None:  # if the slot prescribed by the hash function is empty...
            self.slots[hashvalue] = key  # simply add in the key and value at that slot in their respective lists
            self.data[hashvalue] = data
        else:  # if it is already full...
            if self.slots[hashvalue] == key:  # if the slot already contains the same key, we want to overwrite the value
                self.data[hashvalue] = data
            else:  # if the slot is already occupied by a different key, we have a conflict
                nextslot = self.rehash(hashvalue, len(self.slots))  # rehash the old hash value to get a new one
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:  # keep rehashing until we find a valid slot
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:  # now once we have our slot, we use the same procedure as the first case above
                    self.slots[nextslot] = key  # if the slot was empty, fill it with our key and value
                    self.data[nextslot] = data
                else:  # if it was not empty it must have contained the same key as the one we are trying to insert
                    self.data[nextslot] = data  # which means we replace the value with the new one

    # hashfunction: the mathematical function that determines the slot that each key will go in
    def hashfunction(self, key, size):
        return key % size  # this is a primitive hash function that simply returns the key (mod 11).

    # rehash: the "fallback" function that is called to find a new hash if there is a conflict with the original one
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size  # again, very primitive: just returns oldhash+1 (mod 11).

    # get: retrieve the value at a given key
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))  # begin searching at the "actual" hash value for this key

        data = None  # will store the value when we find it
        stop = False  # have we gone through the whole table?
        found = False  # have we found what we are looking for?
        position = startslot
        while self.slots[position] is not None and not found and not stop:  # loop through and keep rehashing until we find it
            if self.slots[position] == key:  # if we find it right away, we are done and set the flag accordingly
                found = True
                data = self.data[position]  # as well as store the value so we can return it
            else:  # if this position is not it, rehash the position and try that
                position = self.rehash(position, len(self.slots))  # we basically attempt to trace the same path that "put" used when adding the item
                if position == startslot:  # if we have come all the way back to where we started and haven't found it, the item is not there
                    stop = True  # so signal the loop to stop, and we will return None since data will still be None
        return data  # return either what we have found, or None if we did not find any value for the key

    # interface with Python builtin methods so we can use this like a native dictionary with indexing syntax for get/set
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    # another builtin, returns the length of the hash table
    def __len__(self):
        count = 0  # go through every index, if there is an item there increment the counter by 1
        for item in self.data:
            if item is not None:
                count += 1
        return count  # at the end, return the counter

    # to delete an element, we will want to find it first, then clear its slots in the table
    def __del__(self, key):
        startslot = self.hashfunction(key, len(self.slots))  # the search procedure will be similar to get()

        finalPos = -1  # will store the final position of the item, if we find it
        stop = False  # flag that will stop searching if we have traversed the whole list
        found = False  # flag that will stop searching if we have found the item
        position = startslot  # start the position at the "default" place for the item, as prescribed by the main hash function
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:  # if we have found the item here, set the flag and store its position
                found = True
                finalPos = position
            else:  # if not, we rehash and overwrite position in preparation for the next loop iteration
                position = self.rehash(position, len(self.slots))
                if position == startslot:  # if we have come all the way back to the start and have not found the item, it doesn't exist
                    stop = True  # so we set the flag to stop the loop

        # if we found the item, it will have been overwritten from the initial value of -1 and this bit will run
        if finalPos > 0:
            self.slots[finalPos] = None  # simply just clear out the key and value at this index (delete it)
            self.data[finalPos] = None

    # to check whether an item is in the list, we can just check whether a call to get() returns something or whether it is None
    def __contains__(self, item):
        return self.get(item) is not None
