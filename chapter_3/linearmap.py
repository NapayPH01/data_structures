# Implementation of Map ADT using a single list.
class Map:
    # Creates an empty map instance.
    def __init__(self):
        self._entryList = list()

    # Returns the number of entries in the map.
    def __len__(self):
        return len(self._entryList)

    # Determines if the map contains the given key.
    def __contains__(self,key):
        ndx = self._findPosition(key)
        return ndx is not None
    
    # Adds a new entry to the map if the key does exist. Otherwise,
    # the new value replaces the current value associated with the key
    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None: # if the key was found
            self._entryList[ndx].value = value
            return False
        else: # otherwise add a new entry
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    # Returns the value associated with the key.
    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value

    # Removes the entry associated with the key.
    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        self._entryList.pop(ndx)

    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return _MapIterator(self._entryList)

    # Helper method used to find the index position of a category. If the
    # key is not found, None is required.
    def _findPosition(self, key):
        # Iterate through each entry in the ith entry
        for i in range(len(self)):
            # Is the key stored in the ith entry?
            if self._entryList[i].key == key:
                return i
        # When not found, return None.
        return None

# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class _MapIterator:
    def __init__(self, theSet):
        self._mapRef = theSet
        self._curNdx = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curNdx < len(self._mapRef):
            entry = self._mapRef[ self._curNdx ]
            self._curNdx += 1
            return entry.key
        else:
            raise StopIteration
