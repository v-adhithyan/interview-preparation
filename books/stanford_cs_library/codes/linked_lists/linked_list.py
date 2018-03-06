
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self._count = 1

    def add(self, newnode):
        if self.next is None:
            self.next = newnode
            self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = newnode

        self._count += 1

    def print_list(self):
        current = self
        while current is not None:
            print current.data
            current = current.next

    def size(self):
        return int(self._count)


def test():
    head = node(1)

    for i in range(1500):
        head.add(node(i))

    head.print_list()

    print "the size of list is {}".format(head.size())