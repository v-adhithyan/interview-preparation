# Swap odd and even bits of a number
def swap_bits(num):
    return (num & 0xaaaaaaaa) >> 1 | (num & 0x55555555) << 1


def main():
    assert swap_bits(2) == 1


if __name__ == '__main__':
    main()
