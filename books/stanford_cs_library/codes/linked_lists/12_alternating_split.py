from linked_list import node

def alt_split(source):

    first = None
    second = None
    while source is not None:
        if first is None and second is None:
            first = node(source.data)
            if source.next is not None:
                second = node(source.next.data)
        else:
            first.add(node(source.data))
            if source.next is not None:
                second.add(node(source.next.data))

        if source.next is not None:
            source = source.next.next
        else:
            break

    return first, second

a = node(0)
for i in range(1, 3):
    a.add(node(i))
f, s = alt_split(a)
f.print_list()
s.print_list()
