from .stack import Stack

class Parentheses:
    
    def is_matched(self, expr):
        left = '({['
        right = ')}]'
        s = Stack()
        for c in expr:
            if c in left:
                s.push(c)
            elif c in right:
                if s.is_empty():
                    return False
                if right.index(c) != left.index(s.pop()):
                    return False
        
        return s.is_empty()
