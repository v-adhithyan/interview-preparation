def zero_row_and_column_if_val_is_zero(array):
    rows_that_have_zeroes = set()
    cols_that_have_zeroes = set()

    for i, row in enumerate(array):
        for j, val in enumerate(row):
            if val == 0:
                rows_that_have_zeroes.add(i)
                cols_that_have_zeroes.add(j)

    for i, row in enumerate(array):
        for j, _ in enumerate(row):
            if i in rows_that_have_zeroes or j in cols_that_have_zeroes:
                array[i][j] = 0

    return array


def main():
    array_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # arrray has no zeroes, so output should be input array
    assert zero_row_and_column_if_val_is_zero(array_1) == array_1

    array_2_in = [[1, 0, 3], [4, 5, 6], [7, 8, 9]]
    array_2_out = [[0, 0, 0], [4, 0, 6], [7, 0, 9]]
    assert zero_row_and_column_if_val_is_zero(array_2_in) == array_2_out

    array_3_in = [[1, 0, 3], [0, 5, 6], [7, 8, 0]]
    array_3_out = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert zero_row_and_column_if_val_is_zero(array_3_in) == array_3_out


if __name__ == '__main__':
    main()
