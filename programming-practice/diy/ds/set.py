"""My own implementation of set interface inspired from Java."""
from abc import ABC, abstractmethod


class Set(ABC):

    def __init__(self, initial_capacity=16, load_factor=0.75):
        self.count = 0
        self.initial_capacity = initial_capacity
        self.load_factor = load_factor
        self.threshold = self.initial_capacity * self.load_factor
        self.mod_count = 0
        self.table = [[]] * self.initial_capacity
        
        super().__init__()
        
    def size(self) -> int:
        return self.count

    def is_empty(self) -> bool:
        return self.count == 0

    @abstractmethod
    def contains(self, key) -> bool:
        pass

    @abstractmethod
    def add(self, key) -> bool:
        pass

    @abstractmethod
    def remove(self, key) -> bool:
        pass

    @abstractmethod
    def clear(self, key):
        pass

    @abstractmethod
    def add_all(self, keys) -> bool:
        pass

    @abstractmethod
    def remove_all(self, keys) -> bool:
        pass
    
    def __repr__(self):
        v = []
        [v.extend(values) for values in self.table if len(values) > 0]
        return str(v)
