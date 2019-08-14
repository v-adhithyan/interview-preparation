'''
Implement queue using 2 stacks.

Add the item to stack 1,
Peek and pop from stack 2, if stack 2 is empty remove elements from stack 1
and push to stack 2
'''


class MyQueue:

    def __init__(self):
        self.stack_1 = list()
        self.stack_2 = list()

    def __len__(self):
        return len(self.stack_1) + len(self.stack_2)

    def add(self, val):
        self.stack_1.append(val)

    def _transfer_and_pop(self):
        while len(self.stack_1) > 0:
            self.stack_2.append(self.stack_1.pop())

        return self.stack_2[-1]

    def peek(self):
        if len(self.stack_2) > 0:
            return self.stack_2[-1]

        return self._transfer_and_pop()

    def remove(self):
        if len(self.stack_2) > 0:
            return self.stack_2.pop()

        return self._transfer_and_pop()


def main():
    q = MyQueue()
    q.add(1)
    q.add(2)

    assert q.peek() == 1
    assert q.remove() == 1
    assert q.peek() == 2
    assert q.remove() == 2

    q.add(5)
    q.add(-1)
    q.add(3)

    assert len(q) == 3
    assert q.peek() == 5


if __name__ == '__main__':
    main()
