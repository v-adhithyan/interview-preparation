from linked_list import node

def remove_duplicates(source):

    if source is not None:

        current = source
        while current.next is not None:
            if current.data == current.next.data:
                next_next = current.next.next
                current.next = next_next
            else:
                current = current.next
        return current


a = node(1)
for i in range(4):
    a.add(node(1))

remove_duplicates(a).print_list()