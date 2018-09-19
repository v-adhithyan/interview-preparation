from .hash_set import HashSet


# use pytest package for unit testing
def test_init():
    h = HashSet()
    assert h.size() == 0


def test_add():
    # Test all elements are added to system by calling contains
    h = HashSet()
    h.add(1)
    h.add("1")
    h.add("hello world")
    h.add("-1")
    h.add(-1)
    h.add("3.14")

    assert h.size() == 6
    assert h.contains(1) == True
    assert h.contains("1") == True
    assert h.contains("hello world") == True
    assert h.contains("-1") == True
    assert h.contains(-1) == True
    assert h.contains("3.14") == True
    
    # assert non presence
    assert h.contains("234") == False

def test_addall():
    h = HashSet()
    keys = [i for i in range(5)]
    keys.extend([3.235, "adhithyan", "diy", "d", 12345])
    h.add_all(keys)
    
    for k in keys:
        assert h.contains(k) == True

def test_contains():
    h = HashSet()

    assert h.contains(0) == False
    
    h.add("contains")
    assert h.contains("contains") == True
    assert h.contains(0) == False

def test_remove():
    h = HashSet()
    
    assert h.remove("a") == False # returns false for non elements
    
    h.add("a")
    assert h.remove("a") == True

def test_removeall():
    h = HashSet()
    keys = [i for i in range(5)]
    keys.extend([3.235, "adhithyan", "diy", "d", 12345])
    h.add_all(keys)
    for k in keys:
        assert h.contains(k) == True
        
    assert h.size() == len(keys)
    h.remove_all(keys)
    assert h.size() == 0
    for k in keys:
        assert h.contains(k) == False

def test_clear():
    h = HashSet()
    keys = [i for i in range(5)]
    h.add_all(keys)
    for k in keys:
        assert h.contains(k) == True
    
    assert h.size() == len(keys)
    h.clear()
    assert h.size() == 0
    for k in keys:
        assert h.contains(k) == False

def test_rehash():
    # initial capacity is 16
    # default load factor is always 0.75
    # when the entries are 12, it will be resized to 32
    # now capacity is 32
    # when the entries are 24, it will be resized to 128
    
    h = HashSet()
    
    ten_entries = [i for i in range(10)]
    thirteen_entries = [i for i in range(13)]
    twenty_five_entries = [i for i in range(26)]
    
    h.add_all(ten_entries)
    assert h.size() == len(ten_entries)
    assert len(h.table) == 16
    
    h.clear()
    assert h.size() == 0
    
    h.add_all(thirteen_entries)
    assert h.size() == len(thirteen_entries)
    assert len(h.table) == 16 << 1 
    
    h.clear()
    assert h.size() == 0
    
    h.add_all(twenty_five_entries)
    assert h.size() == len(twenty_five_entries)
    assert len(h.table) == 32 << 2

def test_add_after_remove():
    # make sure you are able to add to same bucket after removing
    h = HashSet()
    h.add(1)
    assert h.contains(1) == True
    h.remove(1)
    assert h.contains(1) == False
    h.add(1)
    assert h.contains(1) == True

def test_add_after_clear():
    # make sure you are able to add to same bucket after removing
    h = HashSet()
    keys = [i for i in range(5)]
    h.add_all(keys)
    for i in keys:
        assert h.contains(i) == True
    
    h.clear()
    assert h.size() == 0
    
    h.add_all(keys)
    for i in keys:
        assert h.contains(i) == True
    
