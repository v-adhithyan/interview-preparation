from .balance_parentheses import Parentheses

def test_match():
    p = Parentheses()
    assert p.is_matched('()(()){([()])}') == True
    assert p.is_matched('()') == True
    assert p.is_matched('(') == False
    assert p.is_matched('((()))') == True