from .set import Set


class HashSet(Set):
    # Collisions are not handled.
    def __hashcode(self, key=None) -> int:
        if not key:
            return 0

        hash = 0
        if type(key) is int:
            return key
        for char in str(key):
            hash += ord(char)

        return hash

    def __rehash(self):
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
        hash = self.__hashcode(key)
        return (hash & 0x7FFFFFFF) % len(self.table)

    def add(self, key) -> bool:
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
        self.count = 0
        size = len(self.table)
        self.table = [None] * size
        return True

    def add_all(self, keys) -> bool:
        for key in keys:
            self.add(key=key)

        return True

    def remove_all(self, keys) -> bool:
        for key in keys:
            self.remove(key=key)

        return True
