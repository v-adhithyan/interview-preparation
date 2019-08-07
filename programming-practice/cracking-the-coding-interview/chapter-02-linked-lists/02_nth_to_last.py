def nth_to_last_element(head, n):
    # find the length of linked list
    # return n - len + 1
    curr = head
    length = 0
    while curr:
        curr = curr.next
        length += 1

    if n > length:
        return False

    curr = head
    for i in range(0, length - n):
        curr = curr.next

    return curr.data