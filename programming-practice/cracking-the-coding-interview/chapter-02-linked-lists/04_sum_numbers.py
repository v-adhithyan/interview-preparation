from collections import deque
'''
You have two numbers represented by a linked list, where each node contains a sin- gle digit The digits are stored in reverse order, such that the 1’s digit is at the head of the list Write a function that adds the two numbers and returns the sum as a linked list
EXAMPLE
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
'''


def lsum(list_1, list_2):
    ans = deque()
    carry = 0
    while list_1 and list_2:
        sum = list_1.popleft() + list_2.popleft() + carry
        ans.append(sum % 10)
        carry = sum / 10

    if list_1:
        sum = list_1.popleft() + carry
        ans.append(sum % 10)
        carry = sum / 10

    if list_2:
        sum = list_2.popleft() + carry
        ans.append(sum % 10)
        carry = sum / 10

    if int(carry) > 0:
        ans.append(carry)

    return list(map(int, ans))


def main():
    list_1 = deque([3, 1, 5])
    list_2 = deque([5, 9, 2])
    assert lsum(list_1, list_2) == [8, 0, 8]

    list_3 = deque([1])
    list_4 = deque([2, 3])
    assert lsum(list_3, list_4) == [3, 3]

    list_5 = deque([9])
    list_6 = deque([9, 9])
    assert lsum(list_5, list_6) == [8, 0, 1]


if __name__ == '__main__':
    main()
