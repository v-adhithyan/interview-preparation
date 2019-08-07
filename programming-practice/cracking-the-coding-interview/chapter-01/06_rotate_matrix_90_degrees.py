def rotate_90_degrees_1(arr):
    return [
        [col[i] for col in arr[::-1]]
        for i in range(len(arr))
    ]


def rotate_90_degrees_2(arr):
    return list(zip(*arr[::-1]))


def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    out = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate_90_degrees_1(arr) == out

    arr = [[1, 2], [3, 4]]
    assert rotate_90_degrees_1(arr) == [[3, 1], [4, 2]]


if __name__ == '__main__':
    main()
