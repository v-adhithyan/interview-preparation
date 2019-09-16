'''
Select remaining smallest unsorted element from the array and place at end of sorted position
'''


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main():
    arr = [1, 5 , 4 , 3, 2]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
