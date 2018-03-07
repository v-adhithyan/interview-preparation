from linked_list import node


# pop head from second node and add at the front of first list
def move_node(first, second):
    if second is not None:
        second_next = second.next
        second.next = first
        first = second
        second = second_next

        return first, second
