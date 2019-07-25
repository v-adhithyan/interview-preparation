from collections import defaultdict


def anagram_checker_1(word_1, word_2):
    return sorted(word_1) == sorted(word_2)


def anagram_checker_2(word_1, word_2):
    char_count_word_1 = defaultdict(lambda: 0)
    char_count_word_2 = defaultdict(lambda: 0)

    for char in word_1:
        char_count_word_1[char] += 1

    for char in word_2:
        char_count_word_2[char] += 1

    return char_count_word_1 == char_count_word_2


def main():
    invalid_cases = [('adhithyan', 'abinaya')]
    valid_cases = [('war', 'raw'), ('use', 'sue')]

    for word_1, word_2 in valid_cases:
        assert anagram_checker_1(word_1, word_2)
        assert anagram_checker_2(word_1, word_2)

    for word_1, word_2 in invalid_cases:
        assert not anagram_checker_1(word_1, word_2)
        assert not anagram_checker_2(word_1, word_2)


if __name__ == '__main__':
    main()
