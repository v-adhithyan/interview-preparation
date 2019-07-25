def is_substr(word_1, word_2):
    # Check if word_2 is a rotation of word_1
    if not (word_1 or word_2):
        return False

    if len(word_1) != len(word_2):
        return False

    return word_2 in word_1 + word_2


def main():
    word = 'adhithyan'
    assert is_substr(word, word[2:] + word[0:2])
    assert is_substr(word, word)
    assert not is_substr('', '')
    assert not is_substr(word, 'msdhoni')


if __name__ == '__main__':
    main()
