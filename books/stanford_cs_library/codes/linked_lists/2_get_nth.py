from linked_list import node
import unittest

def get_nth(head, n):
    current = head

    if n < 0 or n > current.size():
        return False

    i = 0
    while current is not None:
        if i == n:
            return current.data

        i += 1
        current = current.next


class test(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive_cases(self):
        self.assertEqual(get_nth(head, 5), 5)
        self.assertEqual(get_nth(head, 99), 99)

    def test_negative_cases(self):
        self.assertNotEquals(get_nth(head, 5), 5+1)

    # negative index
    def test_extreme_cases(self):
        self.assertFalse(get_nth(head, -100))


head = node(0)
for i in range(1, 100):
    head.add(node(i))

#head.print_list()
unittest.main()