from linked_list import node

def insert_n(original_list,  n, val):
    if n  >= original_list.size():
        print "cannot insert, index out of bounds"
        return False

    if n == 0:
        saved_old = original_list
        new_node  = node(val)
        new_node.next = saved_old
        original_list = new_node

    else:
        current = original_list
        i = 0
        while current is not None and i < n-1:
            current = current.next
            i += 1

        current_next = current.next
        current.next = node(val)
        current.next.next = current_next

head = node(0)

for i in range(1, 10):
    head.add(node(0))

insert_n(head, 0, -1)
head.print_list()
insert_n(head, head.size()-1, head.size()-1)
head.print_list()
insert_n(head, head.size()/2, head.size()/2)
head.print_list()
insert_n(head, head.size()+1, 9)
#head.print_list()

