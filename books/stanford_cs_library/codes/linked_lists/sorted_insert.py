from linked_list import node

def sorted_insert(original_list, new_node):

    if original_list is None:
        original_list = new_node
        return original_list
    elif new_node.data <= original_list.data:
        save_old = original_list
        original_list = new_node
        original_list.next = save_old
        return original_list
    else:
        current = original_list
        temp = current
        prev = None
        while current.next is not None:
            if new_node.data <= current.next.data:
                current_next = current.next
                current.next = new_node
                new_node.next = current_next
                return original_list

            #original_list.print_list()
            prev = current
            current = current.next

        if new_node.data >= current.data:
            current.next = new_node
        else:
            prev.next = new_node
            new_node.next = current
            current.next = None
        return original_list

