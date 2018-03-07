from linked_list import node

def split(original):
    n = original.size()

    slow = original
    fast = original.next

    front = original
    back = None

    if n > 2:

        while fast is not None:
            fast = fast.next

            if fast is not None:
                slow = slow.next
                fast = fast.next

        back = slow.next
        slow.next = None


    return front, back

