from linked_list import node
import unittest

def delete(head):
    del head

    return None

class test(unittest.TestCase):
    def setUp(self):
        pass

    def test_del(self):
        self.assertIsNone(delete(head))

head = node(0)

for i in range(1, 100):
    head.add(node(i))

unittest.main()