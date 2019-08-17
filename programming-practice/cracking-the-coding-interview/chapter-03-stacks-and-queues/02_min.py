class Stack(list):
    min_val = -1

    def push(self, val):
        self.min_val = min(val, self.min_val)
        super().append(val)

    def min(self):
        return self.min_val


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(-5)

    assert s.min() == -3


if __name__ == '__main__':
    main()
