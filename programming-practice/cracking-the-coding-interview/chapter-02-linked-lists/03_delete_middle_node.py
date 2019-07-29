# given access to only one node in a linked list delete that node alone.


def delete_node(node):
    # edge case given node is last node in list
    if not node or node.next:
        return False

    temp = node.next
    node.data = temp.data
    node.next = temp.next.next

    return True

