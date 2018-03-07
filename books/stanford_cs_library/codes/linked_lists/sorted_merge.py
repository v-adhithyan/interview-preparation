from linked_list import node

def merge_sort(a, b):
    source = None

    while a is not None and b is not None:
        if a.data <= b.data:
            if source is None:
                source = node(a.data)
            else:
                source.add(node(a.data))
            a = a.next
        else:
            if source is None:
                source = node(b.data)
            else:
                source.add(node(b.data))
            b = b.next

    if a is None:
        while b is not None:
            source.add(node(b.data))
            b = b.next
    if b is None:
        while a is not None:
            source.add(node(a.data))
            a = a.next
    return source

a = node(1)
a.add(node(2))
a.add(node(3))

b = node(-1)
b.add(node(0))

merge_sort(a, b).print_list()