# class BaseMap:
#
#     class _MapEntry:
#         def __init__(self, k, v):
#             self._key = k
#             self._value = v
#
#         def __eq__(self, other):
#             return self._key == other.getKey()
#
#         def __ne__(self, other):
#             return not self == other
#
#         def __lt__(self, other):
#             return self._key < other.getKey()
#
#         def __gt__(self, other):
#             return self._key > other.getKey()
#
#         def __str__(self):
#             return "(" + str(self._key) + ", " + str(self._value) + ")"
#
#         def getKey(self):
#             return self._key
#
#         def getVal(self):
#             return self._value


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
        if k in self._map:
            for entry in self._map:
                if entry.getKey() == k:
                    entry.setVal(v)
        else:
            self._map.append(MapEntry(k, v))

    def __contains__(self, k):
        for entry in self._map:
            if entry.getKey() == k:
                return True
        return False
