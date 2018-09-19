"""My own implementation of HashSet inspired from Java."""
from .set import Set


class HashSet(Set):
    """Class HashSet."""

    def __hashcode(self, key=None) -> int:
        """Get hashcode of the key."""
        if not key:
            return 0

        hash = 0
        if type(key) is int:
            return key
        for char in str(key):
            hash += ord(char)

        return hash

    def __rehash(self):
        """Increase the table size if the threshold is reached.

        mod_count  variable will contain the count of number of times
        the table is resized. Initially it will be 0 and our default initial
        capacity is 16. When the number of entries in table is 12 (75 % of 16)
        the add method calls the rehash method internally. On entering this
        method mod count will be incremented, now mod count is 1, and our
        initial capacity (16) will be left shifted by mod_count (1) times i.e
        16 << 1 == 32. Now the table size will be 32. After resizing copy the
        values from old table, calculate new index for each value and add the
        value to new index.
        """
        old_table = self.table
        self.mod_count += 1
        new_size = len(old_table) << self.mod_count
        new_table = [None] * new_size

        for val in old_table:
            if not val:
                continue
            hash = self.__hashcode(val)
            new_index = (hash & 0x7FFFFFFF) % new_size
            new_table[new_index] = val

        self.threshold = new_size * self.load_factor
        self.table = new_table

    def __index(self, key):
        """Get index of a key.

        First get hashcode of the key.then do a bitwise and with
        2147483647 and take mod with table length to prevent overflow. This
        value will be the index.
        """
        hash = self.__hashcode(key)
        return (hash & 0x7FFFFFFF) % len(self.table)

    def add(self, key) -> bool:
        """Add : takes a key as a parameter and adds to the set.

        If the entries reach the threshold value, resize the table.
        If the entry is already present, just return True.
        Otherwise get index of key.
        If there is an entry at the current index, create a list and append the
        key to it. Otherwise set the key at the index
        """
        if self.size() == self.threshold:
            self.__rehash()

        if self.contains(key):
            return True

        index = self.__index(key)

        if self.table[index] is None:
            self.table[index] = key
        else:
            if type(self.table[index]) is not list:  # chaining didn't happen
                self.table[index] = [self.table[index], key]
            else:
                self.table[index] = self.table[index].append(key)

        self.count += 1

        return True

    def remove(self, key) -> bool:
        """Remove : takes  key as a parameter and removes from the set.

        If the size of table is zero or key is not present, return False.
        Otherwise get the index of key. If the type of value at the index is a
        list iterate and match with value to remove or if the value is not list
        set the value of index to None.
        """
        if self.count == 0 or not self.contains(key):
            return False

        index = self.__index(key)
        value = self.table[index]
        if value is not None and type(value) is not list:
            self.table[index] = None
            self.count -= 1
            return True

        for i, val in enumerate(value):
            if val == key:
                del value[i]
                self.count -= 1

                if len(value) == 0:
                    value = None

                self.table[index] = value
                return True

        return False

    def contains(self, key) -> bool:
        """Check if the key is present in the set."""
        index = self.__index(key)
        value = self.table[index]
        if value is not None:
            if type(value) is not list:
                return value == key
            else:
                for v in value:
                    if v == key:
                        return True

        return False

    def clear(self) -> bool:
        """Set the size to zero and replace all values of table with none."""
        self.count = 0
        size = len(self.table)
        self.table = [None] * size
        return True

    def add_all(self, keys) -> bool:
        """Add all value to the set. For each value call the add method."""
        for key in keys:
            self.add(key=key)

        return True

    def remove_all(self, keys) -> bool:
        """For each value of input call the remove method."""
        for key in keys:
            self.remove(key=key)

        return True
