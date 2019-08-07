def remove_duplicates_1(head):
    # remove duplicates from an unsorted linked list using extra space
    previous = None
    current = head
    seen = set()

    while current:
        if current.data in seen:
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current
        current = current.next


def remove_duplicates_2(head):
    # remove duplicates from an unsorted linked list without extra space
    current = head
    while current:
        runner = head

        while runner != current:
            if runner.data == current.data:
                temp = current.next
                previous.next = temp
                current = temp
                break

            runner = runner.next

        if runner == current:
            previous = current
            current = current.next