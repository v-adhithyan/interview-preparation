def binary_search(input_array, value):
    """Your code goes here."""
    mid = ((len(input_array) + 1) / 2) - 1
    print mid
    while mid >= 0 or mid < len(input_array):
        if input_array[mid] == value:
            return input_array.index(value)
        elif value > input_array[mid]:
            mid = ((mid + len(input_array) + 1) / 2) - 1
        else:
            mid = ((0 + mid - 1) / 2) - 1
        print mid
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)