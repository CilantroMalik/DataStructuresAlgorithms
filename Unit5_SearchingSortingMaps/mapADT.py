"""
--- The Map ADT ---
Implementation of a bare-bones Map ADT that includes all the standard operations such as get, set, delete, contains,
length, string, and iterator methods, mostly overridden from Python defaults so it can interface more naturally with
the language. Uses a helper class to encapsulate a map entry, that implements various comparison methods and string.
"""

class MapEntry:
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):
        return self._key == other.getKey()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self._key < other.getKey()

    def __gt__(self, other):
        return self._key > other.getKey()

    def __str__(self):
        return "(" + str(self._key) + ", " + str(self._value) + ")"

    def getKey(self):
        return self._key

    def getVal(self):
        return self._value

    def setVal(self, newVal):
        self._value = newVal

class UnsortedMap:

    def __init__(self):
        self._map = []

    def __len__(self):
        return len(self._map)

    def __getitem__(self, k):
        for entry in self._map:
            if entry.getKey() == k:
                return entry.getVal()
        return None

    def __setitem__(self, k, v):
        for entry in self._map:
            if entry.getKey() == k:
                entry.setVal(v)
                return
        self._map.append(MapEntry(k, v))

    def __contains__(self, k):
        for entry in self._map:
            if entry.getKey() == k:
                return True
        return False

    def __delitem__(self, k):
        for entry in self._map:
            if entry.getKey() == k:
                self._map.remove(entry)
                return True
        return False

    def __str__(self):
        return "{" + ", ".join([str(entry) for entry in self._map]) + "}"

    def __iter__(self):
        return iter(self._map)


# Testing
testMap = UnsortedMap()
testMap[3] = "c"
testMap[3] = "d"
print(3 in testMap)
print(testMap)
