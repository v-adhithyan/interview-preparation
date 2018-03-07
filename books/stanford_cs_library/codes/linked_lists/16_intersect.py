from linked_list import node

def intersect(a, b):
    result = None
    while a is not None and b is not None:
        if a.data < b.data:
            a = a.next
        elif a.data > b.data:
            b = b.next
        else:
            if result is None:
                result = node(a.data)
            else:
                result.add(node(a.data))

            a = a.next
            b = b.next

    return result

a = node(0)
a.add(node(1))

b = node(0)
b.add(node(1))
b.add(node(2))

intersect(a, b).print_list()