
class Stack:
    
    def __init__(self):
        self.__stack = []
    
    def push(self, val):
        self.__stack.append(val)
    
    def __len__(self) -> int:
        return len(self.__stack)
    
    def is_empty(self) -> bool:
        return len(self.__stack) == 0
    
    def top(self):
        if self.is_empty():
            raise "Stack is empty"
        
        return self.__stack[-1]
    
    def pop(self):
        if self.is_empty():
            raise "Stack is empty"
        
        return self.__stack.pop()