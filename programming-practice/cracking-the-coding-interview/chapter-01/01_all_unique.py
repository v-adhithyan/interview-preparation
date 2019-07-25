def has_unique_chars(word):
    charset = {}

    for char in word:
        if charset.get(char):
            return False
        charset[char] = True

    return True


def has_unique_chars_bitwise(word):
    checker = 0

    for char in word:
        val = ord(char) - ord('a')

        if checker & (1 << val):
            return False

        checker |= 1 << val

    return True


def main():
    valid_cases = ['adhi']
    invalid_cases = ['adhithyan']

    for word in valid_cases:
        assert has_unique_chars(word)
        assert has_unique_chars_bitwise(word)

    for word in invalid_cases:
        assert not has_unique_chars(word)
        assert not has_unique_chars_bitwise(word)


if __name__ == '__main__':
    main()
