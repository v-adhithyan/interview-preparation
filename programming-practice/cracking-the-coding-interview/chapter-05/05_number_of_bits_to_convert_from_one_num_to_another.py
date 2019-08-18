# XOR will give one difference bit between number 1 and 2
def bit_swap_required(num_1, num_2):
    xor_num = num_1 ^ num_2
    count = 0

    while xor_num > 0:
        count += xor_num & 1
        xor_num >>= 1

    return count


def main():
    assert bit_swap_required(31, 14) == 2


if __name__ == '__main__':
    main()