from linked_list import node
import unittest

def pop(head):
    data = head.data
    head = head.next
    return [head, data]


head = node(0)

for i in range(1, 100):
    head.add(node(i))


pop_1 = pop(head)
head = pop_1[0]

pop_2 = pop(head)
head = pop_2[0]

print pop_1[1]
print pop_2[1]