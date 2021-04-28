"""
--- Sorted Map ---
Modified implementation of the Map ADT that preserves sorting of its keys and includes a few additional methods such as
merging two maps together. The sorted properties enable some extra optimizations when searching for a key, which happens
often in many methods of the map. Also includes a MapEntry class that encapsulates a key/value pair and comparison methods.
"""


# MapEntry class that holds information for one entry in the map, a key and a value
class MapEntry:
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):  # equality is decided by key since keys should be unique
        return self._key == other.getKey()  # _key is a protected property, so we access the other's key with the getter

    def __lt__(self, other):  # again, comparisons are all based off of the key
        return self._key < other.getKey()

    def __gt__(self, other):  # analogous to all the other comparisons
        return self._key > other.getKey()

    def __le__(self, other):
        return self._key <= other.getKey()

    def __ge__(self, other):
        return self._key >= other.getKey()

    def __str__(self):  # returns a tuple-like view of the key and value of the entry
        return "(" + str(self._key) + ", " + str(self._value) + ")"

    def getKey(self):  # getter method for the protected property _key; this never changes so it does not need a setter
        return self._key

    def getVal(self):  # getter method for the protected property _value
        return self._value

    def setVal(self, newVal):  # setter method for _value since it could be modified
        self._value = newVal


# SortedMap class that implements a sorted version of the Map ADT that maintains its keys in order.
# Methods interface with default Python syntax because of the overridden implementations of builtin methods.
class SortedMap:
    def __init__(self):
        self._map = []  # initialize an empty map

    def __getitem__(self, k):  # retrieve the item with the given key, or throw an error if the key does not exist
        for entry in self._map:  # have to search every entry until the key is found or we are sure it does not exist
            if entry.getKey() == k:  # found the key --> return the corresponding value
                return entry.getVal()
            elif entry.getKey() > k:  # current key is greater than target one: take advantage of sorted properties --> key cannot exist
                break
        raise KeyError("Error: specified key not present in map.")  # if this point is reached without returning, we throw an error

    def __setitem__(self, k, v):  # add a new key-value pair, or modify an existing one
        for entry in self._map:  # again, find the relevant entry by its key, similar to above
            if entry.getKey() == k:
                entry.setVal(v)  # if an existing key, we set the value to the provided one
                return
            elif entry.getKey() > k:  # and if we have reached a larger key, we know it is not there (because the keys are sorted)
                break
        self._insert(MapEntry(k, v))  # if the key does not yet exist, create the key-value pair and insert it at the correct position to preserve sorting

    def __iter__(self):  # makes it so that we can iterate over the map like a normal data structure
        return iter(self._map)  # just iterate over our internal list of entries

    def __contains__(self, k):  # check whether an entry with the given key exists in the list
        for entry in self._map:  # just search the list for the relevant key
            if entry.getKey() == k:
                return True
            elif entry.getKey() > k:  # as always, leverage the sorted nature of the map to optimize the search
                break
        return False

    def __len__(self):  # just a wrapper for the default length method so we can call len() on our map
        return len(self._map)  # similar idea to the iterator, just pass it off to our internal list

    def __str__(self):  # returns a dictionary-like representation of the items of the map, leveraging MapEntry's str()
        return "{" + ", ".join([str(entry) for entry in self._map]) + "}"

    def pop(self, k):  # remove and return the element with the given key
        for i in range(len(self._map)):  # iterate over indices since we are modifying the list
            if self._map[i].getKey() == k:  # search for key as normal
                return self._map.pop(i).getVal()  # if found, defer to the list's pop() method
            elif self._map[i].getKey() > k:
                break
        raise KeyError("Error: specified key not present in map.")  # if we get here, the key did not exist and we throw an error

    def popitem(self):  # alias that just pops the first element
        item = self._map.pop(0)  # just call the pop method of the list on the first element
        return item.getKey(), item.getVal()  # then return this entry's key and value as a tuple

    def clear(self):  # simple interface method that empties the internal map
        self._map = []

    def keys(self):  # simply returns a list of all the keys in the map
        return [entry.getKey() for entry in self._map]

    def values(self):  # similarly, returns a list of all the values int he map
        return [entry.getVal() for entry in self._map]

    def items(self):  # returns a list of key-value pairs in the map, as tuples
        return [(entry.getKey(), entry.getVal()) for entry in self._map]

    def _insert(self, item):  # internal helper function that inserts an item at the correct position to preserve sorting
        if not self._map:  # if the map is empty, just append the element and that's all
            self._map.append(item)
            return
        for i in range(1, len(self._map)):  # we will be modifying, so loop through indices only
            if self._map[i - 1] <= item <= self._map[i]:  # if the item is in the correct place...
                self._map.insert(i, item)  # defer to the list's insert method
                break
        else:  # edge cases, literally: if the item is the smallest or largest in the list
            if item < self._map[0]:  # smallest item --> insert at beginning
                self._map.insert(0, item)
            elif item > self._map[len(self._map) - 1]:  # largest item --> insert at end
                self._map.insert(len(self._map), item)

    def merge(self, other):  # merges two maps together, accounting for possible conflicts
        for item in other:  # go through every item in the other map and insert them one by one
            for entry in self._map:  # for each item, check our map first to see if there is a key conflict
                if entry == item:  # for conflicting keys, keep the value from this map: here, that means do nothing
                    break  # this just prevents the else clause from triggering since we don't want to insert anything
            else:  # if the loop exited normally, without breaking (i.e. if a conflict was not found)
                self._insert(item)  # then insert the item into this map with our helper method


# -- Testing --
testMap = SortedMap()
testMap[1] = "a"
testMap[5] = "e"
print(testMap)
testMap2 = SortedMap()
testMap2[2] = "b"
testMap2[3] = "c"
testMap2[6] = "f"
print(testMap2)
testMap2[6] = "g"
testMap2[4] = "d"
print(testMap2)
testMap.merge(testMap2)
print(testMap)
