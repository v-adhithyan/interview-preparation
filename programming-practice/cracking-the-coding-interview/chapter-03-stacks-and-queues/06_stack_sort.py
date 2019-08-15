def stack_sort(stack):
    temp = list()

    while len(stack) > 0:
        current = stack.pop()
        while len(temp) > 0 and temp[-1] > current:
            stack.append(temp.pop())

        temp.append(current)

    return temp


def main():
    s = [4, 5, 2, 1, 3]
    assert stack_sort(s) == [1, 2, 3, 4, 5]

    s = list(range(5))
    assert stack_sort(s) == list(range(5))

    assert stack_sort([]) == []

    assert stack_sort([0] * 5) == [0] * 5


if __name__ == '__main__':
    main()
