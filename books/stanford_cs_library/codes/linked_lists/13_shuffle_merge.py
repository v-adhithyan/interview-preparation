from linked_list import node

def shuffle_merge(a, b):
    merge = None

    while a is not None or b is not None:
        if a is not None:
            if merge is None:
                merge = node(a.data)
            else:
                merge.add(node(a.data))
            a = a.next


        if b is not None:
            if merge is None:
                merge = node(b.data)
            else:
                merge.add(node(b.data))
            b = b.next
    return merge

a = node(1)
a.add(node(2))
a.add(node(3))

b = node(7)
b.add(node(13))
b.add(node(1))

shuffle_merge(a, b).print_list()