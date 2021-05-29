STACK_EMPTY = "Stack is empty"


class Empty(Exception):
    pass


class Stack(object):
    
    def __init__(self):
        self._stack = []
    
    def push(self, val):
        self._stack.append(val)
    
    def __len__(self) -> int:
        return len(self._stack)
    
    def is_empty(self) -> bool:
        return len(self._stack) == 0
    
    def top(self):
        if self.is_empty():
            raise Empty(STACK_EMPTY)
        
        return self._stack[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty(STACK_EMPTY)
        
        return self._stack.pop()
