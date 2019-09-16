'''
from the remaining elements, pick and insert the smallest element at current position
'''


def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr


def main():
    arr = [2, 1, 4, 3, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
