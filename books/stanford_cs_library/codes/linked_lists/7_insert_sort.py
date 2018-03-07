from linked_list import node
from sorted_insert import sorted_insert

def insertion_sort(old_list):
    new_list = None

    while old_list is not None:
        next = old_list.next
        new_list = sorted_insert(new_list, old_list)
        old_list = next

    return new_list


head = node(4)
head.add(node(-1))
head.add(node(0))
head.add(node(2))
head.add(node(5))
head = insertion_sort(head)
head.print_list()