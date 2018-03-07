from  linked_list import node
from move_node import move_node

def reverse(source):
    result = None

    while source is not None:
        result, source = move_node(result, source)

    return result

a = node(1)
for i in range(2, 5):
    a.add(node(i))

reverse(a).print_list()