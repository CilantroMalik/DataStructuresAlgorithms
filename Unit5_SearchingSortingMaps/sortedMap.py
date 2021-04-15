class MapEntry:
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):
        return self._key == other.getKey()

    def __lt__(self, other):
        return self._key < other.getKey()

    def __gt__(self, other):
        return self._key > other.getKey()

    def __le__(self, other):
        return self._key <= other.getKey()

    def __ge__(self, other):
        return self._key >= other.getKey()

    def __str__(self):
        return "(" + str(self._key) + ", " + str(self._value) + ")"

    def getKey(self):
        return self._key

    def getVal(self):
        return self._value

    def setVal(self, newVal):
        self._value = newVal


class SortedMap:
    def __init__(self):
        self._map = []

    def __getitem__(self, k):
        for entry in self._map:
            if entry.getKey() == k:
                return entry.getVal()
            elif entry.getKey() > k:
                break
        raise KeyError("Error: specified key not present in map.")

    def __setitem__(self, k, v):
        for entry in self._map:
            if entry.getKey() == k:
                entry.setVal(v)
                return
            elif entry.getKey() > k:
                return
        self._map.append(MapEntry(k, v))

    def __iter__(self):
        return iter(self._map)

    def __contains__(self, k):
        for entry in self._map:
            if entry.getKey() == k:
                return True
        return False

    def __len__(self):
        return len(self._map)

    def __str__(self):
        return "{" + ", ".join([str(entry) for entry in self._map]) + "}"

    def pop(self, k):
        for i in range(len(self._map)):
            if self._map[i].getKey() == k:
                return self._map.pop(i).getVal()
            elif self._map[i].getKey() > k:
                break
        raise KeyError("Error: specified key not present in map.")

    def popitem(self):
        item = self._map.pop(0)
        return (item.getKey(), item.getVal())

    def clear(self):
        self._map = []

    def keys(self):
        return [entry.getKey() for entry in self._map]

    def values(self):
        return [entry.getVal() for entry in self._map]

    def items(self):
        return [(entry.getKey(), entry.getVal()) for entry in self._map]

    def merge(self, other):
        for item in other:
            for entry in self._map:
                if entry == item:
                    # behavior for conflicting keys
                    break
            else:
                for i in range(1, len(self._map)):
                    if self._map[i - 1] <= item and self._map[i] >= item:
                        self._map.insert(i, item)
                        break
                else:  # edge cases, literally
                    if item < self._map[0]:
                        self._map.insert(0, item)
                        continue
                    if item > self._map[len(self._map) - 1]:
                        self._map.insert(len(self._map), item)
                        continue


testMap = SortedMap()
testMap[1] = "a"
testMap[5] = "e"
testMap2 = SortedMap()
testMap2[2] = "b"
testMap2[3] = "c"
testMap2[6] = "f"
testMap.merge(testMap2)
print(testMap)
