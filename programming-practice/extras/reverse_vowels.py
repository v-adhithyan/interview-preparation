# Given a string, perform a operation such that vowels alone in a string are repacled
# The first vowel should come at the position of last vowel in the string
# The last vowel should come at the position of first vowel in the string
vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


def reverse_vowels(string):
    vowels = [char for char in string if char in vowels_set]

    ans = ''
    for char in string:
        if char in vowels_set:
            ans += vowels.pop()
            continue
        ans += char

    return char


def main():
    assert reverse_vowels('hello') == 'holle'

    assert reverse_vowels('hello world') == 'hollo werld'


if __name__ == '__main__':
    pass
