from linked_list import node

def append(a, b):
    if a is None:
        a = b
    else:
        current = a
        while current.next is not None:
            current = current.next

        current.next = b
    return a


c = node(10)
for i in range(-1, -5, -1):
    c.add(node(i))

d = node(0)
for i in range(10):
    d.add(node(i))

c = append(c, d)
c.print_list()