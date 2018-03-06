class node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


first = node(1)
second = node(2)
third = node(3)

# link all three
first.next = second
second.next = third

# print and check
current = first
while current is not None:
    print current.data
    current = current.next