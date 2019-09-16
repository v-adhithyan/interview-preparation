def substr(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)

    for i in range(text_length - pattern_length):
        for j in range(pattern_length):
            if not text[i + j] == pattern[j]:
                break
        else:
            return True, i

    return False, -1


def main():
    assert substr("adhi", "ad") == (True, 0)

    assert substr("dfdfgsfgsf", "ferr44") == (False, -1)


if __name__ == '__main__':
    main()
