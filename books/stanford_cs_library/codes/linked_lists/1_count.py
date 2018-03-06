from  linked_list import node
import random
import unittest

def count_num(head, num):
    current = head
    count = 0

    while current is not None:
        if current.data == num:
            count += 1

        current = current.next

    return count

class test(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive_cases(self):
        self.assertEquals(count_num(head, 0), 1)
        self.assertEquals(count_num(head, rand_num), n)

    def test_negative_cases(self):
        self.assertNotEquals(count_num(head, 0), 10)
        self.assertNotEquals(count_num(head, rand_num), 0)

    def test_extreme_cases(self):
        self.assertNotEquals(count_num(head, -1), 10)
        self.assertEquals(count_num(head, -1), 0)


head = node(10)

n = 5

rand_num = random.randint(1, 100)

for i in range(n):
    head.add(node(rand_num))

head.add(node(0))

unittest.main()
