from .stack import Stack

def test_empty():
    s = Stack()
    assert s.is_empty() == True

def test_top():
    s = Stack()
    s.push(1)
    assert s.top() == 1
    
    s.push(2)
    assert s.top() == 2
    assert len(s) == 2

def test_pop():
    s = Stack()
    s.push(1)
    s.push(10)
    
    assert s.pop() == 10
    s.pop()
    
    try:
        s.pop()
    except TypeError as e:
        pass
        #assert str(e) == "Stack is empty"