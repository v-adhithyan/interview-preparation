from linked_list import node
from front_back_split import split
from sorted_merge import merge_sort

def sort(source):

    if source is None or source.next is None:
        pass

    a, b = split(source)
    a = sort(a)
    b = sort(b)

    return merge_sort(a, b)

a = node(9)
a.add(node(0))
a.add(node(-1))
a.add(node(52))
a.add(node(7))

sort(a).print_list()