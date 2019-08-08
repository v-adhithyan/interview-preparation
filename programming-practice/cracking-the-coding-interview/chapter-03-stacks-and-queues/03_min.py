class Stack(list):
    min = -1

    def push(self, val:int ):
        self.min = self.min if self.min < val else val
        self.append(val)

    def min(self):
        return self.min


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(-5)

    assert s.min() == -5


if __name__ == '__main__':
    main()
