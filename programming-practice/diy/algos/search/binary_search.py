"""Binary search in python."""


def binary_search(array, target, left, right) -> bool:
    """Recursive implementation of binary search."""
    if left > right:
        return False

    mid = (left + right) // 2

    if target == array[mid]:
        return True
    elif target < target[mid]:
        return binary_search(array, target, left, mid - 1)
    else:
        return binary_search(array, target, mid + 1, right)


def main():
    """Main."""
    array = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    binary_search(array, 2, 0, len(array-1))


if __name__ == "__main__":
    main()
