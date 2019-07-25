def remove_duplicate_chars(word):
    if not word:
        return ''

    seen_characters = {}
    output = ''

    for char in word:
        if not seen_characters.get(char):
            output += char
            seen_characters[char] = True

    return output


if __name__ == '__main__':
    assert remove_duplicate_chars(None) == ''
    assert remove_duplicate_chars('abcd') == 'abcd'
    assert remove_duplicate_chars('aaaa') == 'a'
    assert remove_duplicate_chars('aaabbb') == 'ab'
